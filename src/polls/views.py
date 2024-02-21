from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import (
    HttpRequest,
)
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.views import View
from django.contrib import messages
from django.db.models.functions import DenseRank
from django.db.models import (
    F,
    Count,
    Window,
)

# Create your views here.
from .models import (
    Question,
    Poll,
    UserResponse,
    AnswerQuestion,
)
from .forms import AnswerQuestionForm


class PollsView(LoginRequiredMixin, View):

    def get(self, request: HttpRequest):
        polls = Poll.objects.all()
        ctx = {
            'polls': polls,
        }
        return render(request, 'polls/polls.html', ctx)


class PollView(LoginRequiredMixin, View):

    def get(self, request: HttpRequest, poll_pk: int):
        first_question = (
            AnswerQuestion.objects
            .select_related('question')
            .filter(question__poll__pk=poll_pk)
            .first()
        )
        if first_question:
            return redirect('polls:question', question_pk=first_question.question.pk)
        messages.add_message(request, messages.INFO, "For this polling doesn\'t exists questions.")
        return redirect('polls:list')


class QuestionView(LoginRequiredMixin, View):

    def get(self, request: HttpRequest, question_pk: int):
        question = get_object_or_404(Question, pk=question_pk)
        form = AnswerQuestionForm(question_id=question_pk)
        ctx = {
            'question': question,
            'form': form,
        }
        return render(request, 'polls/question.html', ctx)

    def post(self, request: HttpRequest, question_pk: int):
        question = get_object_or_404(Question, pk=question_pk)

        form = AnswerQuestionForm(request.POST, question_id=question_pk)
        if form.is_valid():
            user = request.user
            answer_question = form.cleaned_data['answer_question']

            UserResponse.objects.create(user=user, answer_question=answer_question)

            if not answer_question.new_question_id:
                messages.add_message(request, messages.INFO, 'You have completed the poll')
                return redirect('polls:statistic', poll_pk=question.poll_id)

            return redirect('polls:question', question_pk=answer_question.new_question_id)

        messages.add_message(request, messages.ERROR, form.errors)
        return redirect('polls:question', question_pk=question_pk)


class StatisticView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, poll_pk: int):
        poll = get_object_or_404(Poll, pk=poll_pk)

        total_participants = (
            UserResponse.objects
            .filter(answer_question__question__poll__pk=poll_pk)
            .values('user')
            .distinct()
            .count()
        )

        total_respondents_perc = (
            Question.objects
            .filter(poll__pk=poll_pk)
            .values('pk', 'title')
            .annotate(
                count_resp=Count('questions__userresponse__user__pk', distinct=True),
                perc=F('count_resp') * 100 / total_participants,
            )
        )

        rank_questions = (
            total_respondents_perc
            .annotate(rank=Window(expression=DenseRank(), order_by=F('count_resp').desc()))
        )

        total_respondents_on_every_question = (
            AnswerQuestion.objects
            .filter(question__poll__pk=poll_pk)
            .values('pk')
            .annotate(count_resp=Count('userresponse__user', distinct=True))
            .annotate(perc=F('count_resp') * 100 / Count('question'))
        )

        ctx = {
            'poll': poll,
            'total_participants': total_participants,
            'total_respondents_perc': total_respondents_perc,
            'rank_questions': rank_questions,
            'total_respondents_on_every_question': total_respondents_on_every_question,
        }

        return render(request, 'polls/statistic.html', ctx)

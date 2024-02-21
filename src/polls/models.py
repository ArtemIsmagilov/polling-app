from django.contrib.auth.models import User
from django.db import models
from django.db.models import (
    CheckConstraint,
    UniqueConstraint,
    Q,
    F,
)


class Poll(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return 'Poll(pk={} title={})'.format(
            self.pk, self.title,
        )


class Question(models.Model):
    title = models.CharField(max_length=255, unique=True)

    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)

    def __str__(self):
        return 'Question(pk={}, title={} poll_pk={})'.format(
            self.pk, self.title, self.poll_id,
        )


class Answer(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return 'Answer(pk={}, title={})'.format(
            self.pk, self.title,
        )


class AnswerQuestion(models.Model):
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='questions')
    new_question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='new_questions')

    class Meta:
        constraints = (
            UniqueConstraint(fields=('answer', 'question'), name='unique_answer_for_question'),
            UniqueConstraint(fields=('question', 'new_question'), name='unique_question_for_new_question'),
            CheckConstraint(check=~Q(question=F('new_question')), name="question_ne_new_question"),
        )

    def __str__(self):
        return 'AnswerQuestion(pk={}, answer_pk={} question_pk={} new_question_pk={})'.format(
            self.pk, self.answer_id, self.question_id, self.new_question_id,
        )


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_question = models.ForeignKey('AnswerQuestion', on_delete=models.CASCADE)

    # class Meta:
    #     constraints = (
    #         UniqueConstraint(fields=('user', 'answer_question'), name='unique_answer_question_for_user'),
    #     )

    def __str__(self):
        return 'Answer(pk={}, user_pk={} answer_question_pk={})'.format(
            self.pk, self.user_id, self.answer_question_id,
        )

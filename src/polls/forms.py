from django import forms

from .models import AnswerQuestion


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj: AnswerQuestion):
        return obj.answer.title


class AnswerQuestionForm(forms.Form):
    answer_question = MyModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        queryset = (
            AnswerQuestion.objects
            .select_related('answer')
            .filter(question_id=kwargs.pop('question_id'))
        )
        super().__init__(*args, **kwargs)
        self.fields['answer_question'].queryset = queryset

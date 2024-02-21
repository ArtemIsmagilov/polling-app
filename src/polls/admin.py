from django.contrib import admin

# Register your models here.

from .models import (
    Poll,
    Question,
    Answer,
    AnswerQuestion,
    UserResponse,
)


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("pk", "title",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("pk", "title",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("pk", "title",)


@admin.register(AnswerQuestion)
class AnswerQuestionAdmin(admin.ModelAdmin):
    list_display = ("pk", "answer", "question", "new_question")


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "answer_question")

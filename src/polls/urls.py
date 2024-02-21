from django.urls import path

from .views import (
    PollsView,
    PollView,
    QuestionView,
    StatisticView,
)

app_name = 'polls'
urlpatterns = [
    path("", PollsView.as_view(), name="list"),
    path("<int:poll_pk>/", PollView.as_view(), name='poll'),
    path("question/<int:question_pk>/", QuestionView.as_view(), name="question"),
    path("<int:poll_pk>/statistic/", StatisticView.as_view(), name="statistic"),
]

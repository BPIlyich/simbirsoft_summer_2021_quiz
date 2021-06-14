from django.urls import path

from .views import QuizFormView, QuizListView, QuizResultView


urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_list'),
    path('<str:quiz_id>/', view=QuizFormView.as_view(), name='quiz'),
    path('<str:pk>/result', view=QuizResultView.as_view(), name='quiz_result'),
]
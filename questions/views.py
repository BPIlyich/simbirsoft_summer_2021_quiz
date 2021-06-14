from typing import List

from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import FormView, ListView, DetailView

from quiz.dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from quiz.services import QuizResultService

from questions.models import Quiz
from questions.forms import QuestionForm


class QuizFormView(FormView):
    """
    View для викторины
    """
    form_class = QuestionForm
    template_name = 'questions/question.html'

    def dispatch(self, request, *args, **kwargs):
        quiz = get_object_or_404(Quiz, id=self.kwargs['quiz_id'])
        self.quiz_dto = quiz.get_quiz_dto()
        self.init_session()

        self.question_step = int(self.request.GET.get('step', 0))
        self.question = self.quiz_dto.questions[self.question_step]
        self.is_last_step = len(
            self.quiz_dto.questions) == self.question_step + 1
        return super().dispatch(request, *args, **kwargs)

    def init_session(self):
        quiz_uuid = self.quiz_dto.uuid
        if quiz_uuid not in self.request.session:
            self.request.session[quiz_uuid] = {}
        if 'answered_questions' not in self.request.session[quiz_uuid]:
            self.request.session[quiz_uuid]['answered_questions'] = {}
        self.request.session[quiz_uuid].pop('result', None)

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        selected_fields = self.request.session[self.quiz_dto.uuid][
            'answered_questions'].get(self.question.uuid, [])
        form_kwargs.update(
            question=self.question,
            selected_fields=selected_fields
        )
        return form_kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = self.question
        context['is_last_step'] = self.is_last_step

        if self.question_step:
            context['previous_question_uri'] = (
                reverse(
                    'quiz',
                    kwargs={'quiz_id': self.quiz_dto.uuid}
                )
                + f'?step={self.question_step - 1}'
            )
        context['quiz'] = self.quiz_dto
        return context

    def form_valid(self, form):
        self.request.POST = {}
        guess = dict(form.data).get('answers', [])
        answered_questions = self.request.session[self.quiz_dto.uuid]['answered_questions']
        answered_questions[self.question.uuid] = guess
        self.request.session[self.quiz_dto.uuid]['answered_questions'] = dict(
            answered_questions
        )
        return super().form_valid(form)

    def get_success_url(self):
        if self.is_last_step:
            self.write_result_score_to_session()
            return reverse(
                'quiz_result',
                kwargs={'pk': self.quiz_dto.uuid}
            )
        return (
            reverse('quiz', kwargs={'quiz_id': self.quiz_dto.uuid})
            + f'?step={self.question_step + 1}'
        )

    def write_result_score_to_session(self):
        answers = [
            AnswerDTO(question_uuid, choice)
            for question_uuid, choice
            in self.request.session[self.quiz_dto.uuid][
                'answered_questions'].items()
        ]
        quiz_result_service = QuizResultService(
            self.quiz_dto,
            AnswersDTO(self.quiz_dto.uuid, answers)
        )
        self.request.session[self.quiz_dto.uuid]['answered_questions'] = {}
        self.request.session[self.quiz_dto.uuid][
            'result'
        ] = quiz_result_service.get_result()


class QuizListView(ListView):
    """
    View со списком викторин
    """
    model = Quiz


class QuizResultView(DetailView):
    """
    View для вывода результата викторины
    """
    model = Quiz
    template_name = 'questions/result.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        quiz_id = str(self.object.pk)
        if quiz_id not in self.request.session:
            raise Http404('Викторина не найдена')
        if 'result' not in self.request.session[quiz_id]:
            kwargs['error'] = 'Викторина не пройдена'
        else:
            kwargs['result'] = self.request.session[quiz_id]['result']
        return kwargs

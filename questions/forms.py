from typing import List
from django import forms

from quiz.dto import QuestionDTO


class QuestionForm(forms.Form):
    """
    Динамически генерируемая форма вопроса викторины
    """

    def __init__(self, question: QuestionDTO, selected_fields: List[str], *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['answers'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=[(choice.uuid, choice.text) for choice in question.choices],
            initial=selected_fields,
        )

    # Рассчет результа викторины проводится в методе get_result
    # класса quiz.services.QuizResultService
    def is_valid(self):
        return True

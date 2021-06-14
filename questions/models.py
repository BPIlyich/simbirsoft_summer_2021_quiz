from django.db import models

from quiz.dto import ChoiceDTO, QuestionDTO, QuizDTO


class Quiz(models.Model):
    """
    Модель викторины
    """
    title = models.CharField(max_length=50, verbose_name='Викторина')

    def __str__(self):
        return self.title

    def get_quiz_dto(self) -> QuizDTO:
        return QuizDTO(
            str(self.id),
            self.title,
            [question.get_question_dto() for question in self.questions.all()]
        )


class Question(models.Model):
    """
    Модель вопроса
    """
    text = models.CharField(
        max_length=250,
        verbose_name='Вопрос',
        blank=True,
        null=True
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        verbose_name='Викторина',
        related_name='questions'
    )

    def __str__(self):
        return self.text

    def get_question_dto(self) -> QuestionDTO:
        return QuestionDTO(
            str(self.id),
            self.text,
            [choice.get_choice_dto() for choice in self.choices.all()]
        )


class Choice(models.Model):
    """
    Модель ответа
    """
    text = models.CharField(
        max_length=250,
        verbose_name='Вариант ответа',
        blank=True,
        null=True
    )
    is_correct = models.BooleanField(verbose_name='Ответ корректен?')
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос',
        related_name='choices'
    )

    def __str__(self):
        return f'{self.text} ({self.is_correct})'

    def get_choice_dto(self) -> ChoiceDTO:
        return ChoiceDTO(
            str(self.id),
            self.text,
            self.is_correct
        )

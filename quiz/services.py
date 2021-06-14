from .dto import QuizDTO, AnswersDTO


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        """
        Возвращает результат прохождения викторины (от 0 до 1)
        """
        correct_answers_dict = {
            question.uuid: {
                choice.uuid
                for choice in filter(lambda x: x.is_correct, question.choices)
            }
            for question in self.quiz_dto.questions
        }

        correct_answers_counter = sum(
            set(answer.choices) == correct_answers_dict[answer.question_uuid]
            for answer in self.answers_dto.answers
        )

        return round(correct_answers_counter / len(correct_answers_dict), 2)

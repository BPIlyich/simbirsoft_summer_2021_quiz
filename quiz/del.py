from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO

ch1_1 = ChoiceDTO('1-1-1','список', False)
ch1_2 = ChoiceDTO('1-1-2','множество', True)
ch1_3 = ChoiceDTO('1-1-3', 'кортеж', False)
ch1_4 = ChoiceDTO('1-1-4', 'словарь', False)

ch2_1 = ChoiceDTO('1-2-1', 'dir(x)', True)
ch2_2 = ChoiceDTO('1-2-2', 'info(x)', False)
ch2_3 = ChoiceDTO('1-2-3', 'help(x)', False)
ch2_4 = ChoiceDTO('1-2-4', '?x', False)

ch3_1 = ChoiceDTO('1-3-1','x', True)
ch3_2 = ChoiceDTO('1-3-2', 'w', False)
ch3_3 = ChoiceDTO('1-3-3', 'r', False)
ch3_4 = ChoiceDTO('1-3-4', 'Никакой. Нужна предварительная проверка os.path.exists()', False)

ch4_1 = ChoiceDTO('1-4-1', 'Имена принимаемых классом аргументов.',False)
ch4_2 = ChoiceDTO('1-4-2', 'Имена аргументов, принимаемых методом __init__.', False)
ch4_3 = ChoiceDTO('1-4-3', 'Имена суперклассов, если класс наследуется от одного или нескольких классов.', True)
ch4_4 = ChoiceDTO('1-4-4', 'Имена классов, порождаемых данным классом.', False)

ch5_1 = ChoiceDTO('1-5-1', 'Использовать метод input()', True)
ch5_2 = ChoiceDTO('1-5-2', 'Использовать метод read()', False)
ch5_3 = ChoiceDTO('1-5-3', 'Использовать метод get()', False)
ch5_4 = ChoiceDTO('1-5-4', 'Использовать метод cin()', False)

choices1_1 = [ch1_1, ch1_2, ch1_3, ch1_4]
choices1_2 = [ch2_1, ch2_2, ch2_3, ch2_4]
choices1_3 = [ch3_1, ch3_2, ch3_3, ch3_4]
choices1_4 = [ch4_1, ch4_2, ch4_3, ch4_4]
choices1_5 = [ch5_1, ch5_2, ch5_3, ch5_4]

q1 = QuestionDTO('1-1','Необходимо собрать и вывести все уникальные слова из строки рекламного текста. Какой из перечисленных типов данных Python подходит лучше всего?', choices1_1)
q2 = QuestionDTO('1-2',' Как вывести список методов и атрибутов объекта x?', choices1_2)
q3 = QuestionDTO('1-3', 'С помощью Python нужно записать данные в файл, но только в том случае, если файла ещё нет. Какой режим указать в инструкции open()?', choices1_3)
q4 = QuestionDTO('1-4', ' При объявлении класса с помощью оператора class что пишется в круглых скобках после имени класса?', choices1_4)
q5 = QuestionDTO('1-5', 'Как получить данные от пользователя?', choices1_5)

a1 = AnswerDTO('1-1', ['1-1-2'])
a2 = AnswerDTO('1-2', ['1-2-1'])
a3 = AnswerDTO('1-3', ['1-3-1'])
a4 = AnswerDTO('1-4', ['1-4-3'])
a5 = AnswerDTO('1-5', ['1-5-1'])


questions = [q1, q2, q3, q4, q5]
answers = [a1, a2, a3, a4, a5]
quiz = QuizDTO('1', 'Python test', questions)
answers = AnswersDTO('1', answers)
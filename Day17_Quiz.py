from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in range(0, len(question_data)):
    # print(question_data[question]["text"])
    # print(question_data[question]["answer"])
    question_text = question_data[question]["text"]
    answer_text = question_data[question]["answer"]
    quiz = Question(question_text, answer_text)
    question_bank.append(quiz)

# print(question_bank[0].text)

quiz = QuizBrain(question_bank)

for q in range(1, len(question_bank)):
    print(quiz.question_list)




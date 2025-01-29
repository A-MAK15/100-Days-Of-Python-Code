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

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz, your final score is {quiz.score} / {quiz.question_number}")



class QuizBrain:
    def __init__(self,  q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number} : {current_q.text} (True or False) : ")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
            print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score} / {self.question_number}")
        print("\n")

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

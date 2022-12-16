from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"],item["correct_answer"]))

new_quiz = QuizBrain(question_bank)
while new_quiz.still_has_questions() == True:
    new_quiz.next_question()

print("You have completed the quiz")
print(f'Your final score was {new_quiz.score}/{new_quiz.question_number}')

# This is the Quiz Project

# I used geography questions from the Open Trivia Database API

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    element = Question(q_text=item["question"], q_answer=item["correct_answer"])
    question_bank.append(element)

quiz = QuizBrain(question_bank)

# if quiz still has questions remanining
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
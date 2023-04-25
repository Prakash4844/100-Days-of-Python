from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from API_Data import API_data

question_bank = []

# Either use API_data or question_data
for data in API_data:
    q_text = data["question"]
    a_text = data["answer"]
    question_entry = Question(ques=q_text, ans=a_text)
    question_bank.append(question_entry)

quiz = QuizBrain(question_bank)

while quiz.still_have_ques():
    quiz.next_question()

print("You've Completed the quiz!!!")
print(f"Your Final Score: {quiz.score}/{quiz.ques_no}")

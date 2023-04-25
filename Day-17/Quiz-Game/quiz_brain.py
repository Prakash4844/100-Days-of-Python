class QuizBrain:
    def __init__(self, ques_list):
        self.ques_no = 0
        self.ques_list = ques_list
        self.score = 0

    def next_question(self):
        current_ques = self.ques_list[self.ques_no]
        self.ques_no += 1
        user_answer = input(f"Q.{self.ques_no} - {current_ques.question}? (True/False): ")
        self.check_answer(user_answer, current_ques.answer)

    def still_have_ques(self):
        return self.ques_no < len(self.ques_list)

    def check_answer(self, user_ans, actual_ans):
        if user_ans.lower() == actual_ans.lower():
            print("You've got it right!")
            self.score += 1
        else:
            print("You've got it wrong!")
        print(f"Correct Answer is: {actual_ans}")
        print(f"Your Current Score: {self.score}/{self.ques_no}")
        print("\n")

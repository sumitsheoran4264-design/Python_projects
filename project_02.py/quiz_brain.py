class Quizbrain:
    

    def __init__(self, q_list):
        self.question_number  = 0
        self.score = 0
        self.question_list = q_list
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    
    def next_question(self):
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q {self.question_number }: {next_question.text} (True/False)?: ")
        self.check_answer(choice, next_question.answer)
    
    
    def check_answer(self, user_answer, correct_answer):
        '''Check the user choice right or wrong'''

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print("Sorry, wrong answer.")
        print(f"Right answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    

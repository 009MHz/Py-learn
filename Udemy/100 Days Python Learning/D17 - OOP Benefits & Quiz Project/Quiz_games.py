from data import question_data

class Question:
    """Data List converter to CLass object"""
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
        
        
class QuizBrain:
    """Main Quiz Flow"""
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.point = 0
        
    def proceed(self):
        last = len(self.question_list)
        return self.question_number == last
    
    def next_q(self):
        while not self.proceed():
            current = self.question_list[self.question_number]
            user_answer = input(f"Q.{self.question_number + 1}: {current.text} (True/False) ")
            self.answer_check(user_answer, answer_text)
            self.question_number += 1
            
    def answer_check(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("\nBINGO")
            self.point += 1
        else:
            print("Uh-Oh")
        print(f"The correct answer is: '{correct_answer.upper()}'")
        print(f"Your score is {self.point}/{self.question_number + 1}\n\n")


question_bank = []
for x in question_data:
    question_text = x['text']
    answer_text = x['answer']
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)
    

quiz = QuizBrain(question_bank)
quiz.next_q()

print("You've completed the quiz")
print(f"Your final score is: {quiz.point}/{quiz.question_number}")
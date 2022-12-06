class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
        
        
from data import question_data

question_bank = []
for x in question_data:
    question_text = x['text']
    answer_text = x['answer']
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)
    

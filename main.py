from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# create an empty list
question_bank = []

# Store questions in the question_bank list
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

# Create a QuizBrain object and initialize the UI
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

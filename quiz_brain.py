class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {current_question.text} (True/False) > ")

        self.check_answer(choice, current_question.answer)

    def check_answer(self, choice, answer):
        if choice.lower() == answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong")

        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score} / {len(self.question_list)}\n")

    def result(self):
        print("You have completed the quiz")
        print(f"Your final score was: {self.score} / {len(self.question_list)}")



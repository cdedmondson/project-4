class Question:
    # Constructor
    def __init__(self, question_t='', correct_r='', response=''):
        self.question_text = question_t
        self.correct_response = correct_r
        self.response = response

    # Set question to be asked
    def setText(self, question_text):
        self.question_text = question_text

    # Set correct answer
    def setAnswer(self, correct_response):
        self.correct_response = correct_response

    # Check if user response is correct by comparing with correct answer
    def checkAnswer(self, response):
        self.response = response
        if self.correct_response == response:
            return True

    # Display whether or not user's answer is correct
    def display(self):
        print(self.question_text)
        if self.checkAnswer(self.response):
            print(self.response, "is correct!")
        else:
            print(self.response, "is incorrect")


class ChoiceQuestion(Question):
    # Constructor
    def __init__(self):
        # Override
        Question.__init__(self)
        self.choice = []  # Initialize choice list

    # Append multiple choice questions to choice list
    # and whether or not they are correct
    def addChoice(self, choice, correct):
        self.choice.append(choice)
        # If correct is True set answer to correct choice
        if correct:
            self.setAnswer(choice)

    # Display whether or not user's answer is correct
    def display(self):
        print(self.question_text)
        print(self.choice)
        if self.checkAnswer(self.response):
            print(self.response, "is correct!")
        else:
            print(self.response, "is incorrect")


# Tests
question = Question()

question.setText("In which country was the inventor of Python born?")
question.setAnswer("Netherlands")
question.checkAnswer("Canada")
question.display()

choice_question = ChoiceQuestion()
print()
choice_question.setText("In which country was the inventor of Python born?")
choice_question.addChoice("Australia", False)
choice_question.addChoice("Canada", False)
choice_question.addChoice("Netherlands", True)
choice_question.addChoice("United States", False)
choice_question.checkAnswer("Netherlands")
choice_question.display()

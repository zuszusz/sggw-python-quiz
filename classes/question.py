class Question(object):
    def __init__(self, text, answers,correctAnswersValues):
        self.text = text
        self.answers = answers
        self.correctAnswersValues = correctAnswersValues
        
    def __str__(self):
        return self.text
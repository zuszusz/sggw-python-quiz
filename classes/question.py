class Question(object):
    def __init__(self, text, answers,correctAnswers):
        self.text = text
        self.answers = answers
        self.correctAnswers = correctAnswers
        
    def __str__(self):
        return self.text
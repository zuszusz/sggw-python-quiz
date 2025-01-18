class Answer(object):
    def __init__(self, text,value):
        self.text = text
        self.value = value
        
    def __str__(self):
        return self.text

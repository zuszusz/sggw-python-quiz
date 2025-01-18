from classes.answer import Answer
from classes.question import Question

def readQuestions(filePath):
    questions=[]
    with open(filePath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line.strip()
            if(len(line)>3):
                if(line[1]=='?'):
                    questionText = line[3:]
                    currentQuestion = Question(questionText,[],[])
                    questions.append(currentQuestion)
                if(line[1]=='F' or line[1]=='T'):
                    trueOrFalse = line.split(']')[0] + ']'
                    value = line.split(']')[0].split('[')[1]
                    text = line.split(']')[2].strip()
                    
                    if(value==''):
                            value = text
                    
                    answer=Answer(text,value)
                    currentQuestion.answers.append(answer)
                    
                    if(trueOrFalse=='[T]'):
                        currentQuestion.correctAnswers.append(answer)
        
    return questions
from classes.answer import Answer
from classes.question import Question
from fileImports import readQuestions 
from classes.window import window


a1= Answer("Stest","stoks")
a2= Answer("Stest","stoks1")
a3= Answer("Stest","stoks2")
a4= Answer("Stest","stoks3")

q1= Question("Qtest",[a1,a2,a3,a4],[a1,a2])

list = readQuestions("D://Projects//sggw-python-quiz//questions//question.txt")
print(list)
window()




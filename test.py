from classes.answer import Answer
from classes.question import Question
from fileImports import readQuestions 
from classes.window import window
from classes.questionGenerator import *


a1= Answer("Stest","stoks")
a2= Answer("Stest","stoks1")
a3= Answer("Stest","stoks2")
a4= Answer("Stest","stoks3")

q1= Question("Qtest",[a1,a2,a3,a4],[a1,a2])


list = Generator.generateQuestions()

print(len(list[0].answers[0].value))
print(len(list[0].answers[0].text))
window(list)




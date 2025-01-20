from tkinter import *
from classes.answer import Answer
from points import checkAnswers
class window:
        def __init__(self, lista):
                self.questions=lista
                self.selectedAnswerValue=None
                self.selectedAnswerMultipleValue=[]
                self.i=0
                self.punkty=0
                
                self.okno = Tk()
                self.okno.title("Quiz")
                self.okno.geometry("700x400")
                
                self.initialize()
                self.okno.mainloop()


        def initialize(self):
                self.welcomeLabel=Label(text="Test z informatyki", font=("Arial", 20, "bold"))
                self.welcomeLabel.pack(padx=10, pady=10)
                
                self.startBtn=Button(width=10, text="Rozpocznij", command=self.start, bg="#93bf85")
                self.startBtn.pack(padx=10, pady=10)
                
                self.quitBtn=Button(width=10, text="Wyjdź", command=self.okno.quit, bg="#ff5656")
                self.quitBtn.pack()

        def start(self):
                self.welcomeLabel.destroy()
                self.startBtn.destroy()
                self.quitBtn.destroy()

                self.i=0
                self.displayQuestion(self.i)

        def displayQuestion(self,index):
                # delete old widgets

                if hasattr(self, 'questionIndexLabel'):
                        self.questionIndexLabel.destroy()
                if hasattr(self, 'questionText'):
                        self.questionText.destroy()
                if hasattr(self, 'answersFrame'):
                        self.answersFrame.destroy()
                if hasattr(self, 'nextBtn'):
                        self.nextBtn.destroy()

                currentQuestion=self.questions[index]
                
                self.questionIndexLabel=Label(text=f"Pytanie {index+1} z {len(self.questions)}")
                self.questionIndexLabel.grid(row=0,column=0, sticky="WN")
                
                self.questionText=Label(text=currentQuestion.text, font=("Arial", 16, "bold"))
                self.questionText.grid(row=3,column=0, sticky="N")

                self.answersFrame=Frame(self.okno, width=200)
                self.answersFrame.grid(row=4,column=0, sticky="N")

                # for single answer questions
                if len(currentQuestion.correctAnswers)==1:
                        
                        if len(currentQuestion.userAnswers)>0:
                                self.selectedAnswerValue=StringVar(self.okno,currentQuestion.userAnswers[0])
                        else:
                                self.selectedAnswerValue=StringVar(self.okno,currentQuestion.answers[0].value)
                        
                        for i in range(0, len(currentQuestion.answers)):
                                currentAnswer=currentQuestion.answers[i]
                                radioBtn=Radiobutton(self.answersFrame, text=currentAnswer.text, value=currentAnswer.value,variable=self.selectedAnswerValue)
                                radioBtn.pack(anchor=W)
                else:
                        if len(currentQuestion.userAnswers)>0:
                                self.selectedAnswerMultipleValue=[]
                                for i in range(0, len(currentQuestion.answers)):
                                        self.selectedAnswerMultipleValue.append(StringVar(self.okno,currentQuestion.userAnswers[i]))
                        else:
                                self.selectedAnswerMultipleValue=[]
                                for i in range(0, len(currentQuestion.answers)):
                                        self.selectedAnswerMultipleValue.append(StringVar(self.okno,"0"))

                        for i in range(0, len(currentQuestion.answers)):
                                currentAnswer=currentQuestion.answers[i]
                                currentQuestion.userAnswers.append(currentAnswer.value)
                                checkBtn=Checkbutton(self.answersFrame, text=currentAnswer.text,onvalue=currentAnswer.value, variable=self.selectedAnswerMultipleValue[i]).pack(anchor=W)


                self.nextBtn=Button(width=10, text="Dalej", command=lambda: self.nextQuestion(index), bg="#88b7d5")
                self.nextBtn.grid(row=5,column=0, sticky="WN", pady=10)

                if index>0 and index<=len(self.questions)-1:
                        self.previousBtn=Button(width=10, text="Poprzednie", command=lambda: self.previousQuestion(index), bg="#88b7d5")
                        self.previousBtn.grid(row=6,column=0, sticky="WN", pady=10)

                if index==len(self.questions)-1:
                        self.nextBtn.config(text="Zakończ", command=self.finishScreen)

        def saveAnswer(self,index):
                if len(self.questions[index].correctAnswers)==1:
                        self.questions[index].userAnswers=[self.selectedAnswerValue.get()]
                else:
                        self.questions[index].userAnswers=[]
                        for i in range(0, len(self.selectedAnswerMultipleValue)):
                                self.questions[index].userAnswers.append(self.selectedAnswerMultipleValue[i].get())


        def nextQuestion(self,index):
                self.saveAnswer(index)
                self.i+=1
                if self.i<len(self.questions):
                        self.displayQuestion(self.i)
        def previousQuestion(self,index):
                self.saveAnswer(index)
                self.i-=1
                if self.i>=0:
                        self.displayQuestion(self.i)

        def finishScreen(self):
                self.saveAnswer(self.i)
                self.questionIndexLabel.destroy()
                self.questionText.destroy()
                self.answersFrame.destroy()
                self.nextBtn.destroy()
                self.previousBtn.destroy()
                
                self.welcomeLabel = Label(text="Koniec testu", font=("Arial", 20, "bold"))
                self.welcomeLabel.grid(row=0, column=0, padx=10, pady=10)

                points = checkAnswers(self.questions)
                self.pointsLabel = Label(text=f"Ilość punktów: {points} na {len(self.questions)}", font=("Arial", 20, "bold"))
                self.pointsLabel.grid(row=1, column=0, padx=10, pady=10)

                self.quitBtn = Button(width=10, text="Wyjdź", command=self.okno.quit, bg="#ff5656")
                self.quitBtn.grid(row=2, column=0, padx=10, pady=10)

from tkinter import *

#clasees

class Answer(object):
    def __init__(self, text="",value=""):
        self.text = text
        self.value = value
        if value=="":
            self.value=text
        
    def __str__(self):
        return self.text

class Question(object):
    def __init__(self, text, answers,correctAnswers):
        self.text = text
        self.answers = answers
        self.correctAnswers = correctAnswers
        self.userAnswers = []
        
    def __str__(self):
        return self.text

#methods 

def checkAnswers(questions):
    points=0             
    for question in questions:
        for i in range(len(question.userAnswers) - 1, -1, -1):
            if question.userAnswers[i] == '0':
                del question.userAnswers[i]
                  
        areAnswersOk=True
        if(len(question.correctAnswers)!=len(question.userAnswers)):
            areAnswersOk=False
        else:
            for i in range(0,len(question.correctAnswers)):
                corerctAnswer=question.correctAnswers[i].value
                if(not corerctAnswer in question.userAnswers):
                    areAnswersOk=False
                    break
        if(areAnswersOk):
            points+=1

    return points


def checkMark(points, maxPoints):
    if points >= maxPoints * 0.91:
        return "5"
    elif points >= maxPoints * 0.81:
        return "4.5"
    elif points >= maxPoints * 0.71:
        return "4"
    elif points >= maxPoints * 0.61:
        return "3.5"
    elif points >= maxPoints * 0.51:
        return "3"
    else:
        return "2"

class Generator(object):
    def __init__(self):
        pass

    @staticmethod
    def generateQuestions():
        questions = []

        questions.append(Question(
            "Który z poniższych elementów nie jest częścią komputera?", 
            [Answer("a) Klawiatura"), Answer("b) Monitor"), Answer("c) Silnik samochodowy")], 
            [Answer("c) Silnik samochodowy")]
        ))

        questions.append(Question(
            "Co oznacza skrót URL?", 
            [Answer("a) Universal Resource Locator"), Answer("b) Uniform Resource Locator"), Answer("c) Unique Resource Locator")], 
            [Answer("b) Uniform Resource Locator")]
        ))

        questions.append(Question(
            "Który z poniższych jest przykładem przeglądarki internetowej?", 
            [Answer("a) Adobe Photoshop"), Answer("b) Google Chrome"), Answer("c) Microsoft Excel")], 
            [Answer("b) Google Chrome")]
        ))

        questions.append(Question(
            "Co to jest bootowanie?", 
            [Answer("a) Proces uruchamiania systemu"), Answer("b) Instalacja systemu"), Answer("c) Formatowanie dysku")], 
            [Answer("a) Proces uruchamiania systemu")]
        ))

        questions.append(Question(
            "Który z poniższych języków służy do tworzenia stron internetowych?", 
            [Answer("a) Python"), Answer("b) HTML"), Answer("c) C++")], 
            [Answer("b) HTML")]
        ))

        questions.append(Question(
            "Które z poniższych to funkcje systemu operacyjnego?", 
            [Answer("a) Zarządzanie plikami"), Answer("b) Edytowanie zdjęć"), Answer("c) Zarządzanie pamięcią")], 
            [Answer("a) Zarządzanie plikami"), Answer("c) Zarządzanie pamięcią")]
        ))

        questions.append(Question(
            "Które z poniższych urządzeń są używane do przechowywania danych?", 
            [Answer("a) Pendrive"), Answer("b) Procesor"), Answer("c) Dysk twardy")], 
            [Answer("a) Pendrive"), Answer("c) Dysk twardy")]
        ))

        questions.append(Question(
            "Które z poniższych są językami znaczników?", 
            [Answer("a) HTML"), Answer("b) CSS"), Answer("c) XML")], 
            [Answer("a) HTML"), Answer("c) XML")]
        ))

        questions.append(Question(
            "Które z poniższych programów są używane do edycji tekstu?", 
            [Answer("a) Microsoft Word"), Answer("b) Notepad"), Answer("c) Microsoft Excel")], 
            [Answer("a) Microsoft Word"), Answer("b) Notepad")]
        ))

        questions.append(Question(
            "Które z poniższych są przykładami pamięci masowej?", 
            [Answer("a) HDD"), Answer("b) SSD"), Answer("c) RAM")], 
            [Answer("a) HDD"), Answer("b) SSD")]
        ))

        return questions

# window

class window:
        def __init__(self, lista):
                self.questions=lista
                self.selectedAnswerValue=None
                self.selectedAnswerMultipleValue=[]
                self.i=0
                self.punkty=0
                
                self.okno = Tk()
                self.okno.title("Quiz")
                self.okno.geometry("750x350")
                
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
                self.questionIndexLabel.grid(row=0,column=0, sticky="WN", padx=10)
                
                self.questionText=Label(text=currentQuestion.text, font=("Arial", 16, "bold"))
                self.questionText.grid(row=3,column=0, sticky="N")

                self.answersFrame=Frame(self.okno, width=200)
                self.answersFrame.grid(row=4,column=0, sticky="W", padx=25)

                # for single answer questions
                if len(currentQuestion.correctAnswers)==1:
                        
                        if len(currentQuestion.userAnswers)>0:
                                self.selectedAnswerValue=StringVar(self.okno,currentQuestion.userAnswers[0])
                        else:
                                self.selectedAnswerValue=StringVar(self.okno,"Unselected")
                        
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
                                checkBtn=Checkbutton(self.answersFrame, text=currentAnswer.text,onvalue=currentAnswer.value, variable=self.selectedAnswerMultipleValue[i]).pack(anchor=W)


                self.nextBtn=Button(width=10, text="Dalej", command=self.nextQuestion, bg="#88b7d5")
                self.nextBtn.grid(row=5,column=0, sticky="WN", pady=10, padx=25)

                if index>0 and index<=len(self.questions)-1 and (hasattr(self, 'previousBtn')==False or self.previousBtn==None):
                        self.previousBtn=Button(width=10, text="Poprzednie", command=self.previousQuestion, bg="#88b7d5")
                        self.previousBtn.grid(row=6,column=0, sticky="WN", pady=10, padx=25)
                elif index == 0:
                        if self.previousBtn!=None:
                            self.previousBtn.destroy() 
                            self.previousBtn=None

                        

                if index==len(self.questions)-1:
                        self.nextBtn.config(text="Zakończ", command=self.finishScreen,bg="#93bf85")

        def saveAnswer(self,index):
                if len(self.questions[index].correctAnswers)==1:
                        self.questions[index].userAnswers=[self.selectedAnswerValue.get()]
                else:
                        self.questions[index].userAnswers=[]
                        for i in range(0, len(self.selectedAnswerMultipleValue)):
                            self.questions[index].userAnswers.append(self.selectedAnswerMultipleValue[i].get())


        def nextQuestion(self):
                self.saveAnswer(self.i)
                self.i=self.i+1
                if self.i<len(self.questions):
                        self.displayQuestion(self.i)
        def previousQuestion(self):
                self.saveAnswer(self.i)
                if(self.i>0):
                    self.i=self.i-1
                if self.i>=0:
                        self.displayQuestion(self.i)

        def finishScreen(self):
                self.saveAnswer(self.i)
                self.questionIndexLabel.destroy()
                self.questionText.destroy()
                self.answersFrame.destroy()
                self.nextBtn.destroy()
                self.previousBtn.destroy()
                
                for widget in self.okno.grid_slaves():
                    widget.destroy()
                self.okno.grid_columnconfigure(0, weight=1)
                self.okno.grid_rowconfigure(0, weight=1)
                self.okno.grid_rowconfigure(1, weight=1)
                self.okno.grid_rowconfigure(2, weight=1)
                self.okno.grid_rowconfigure(3, weight=1)
                
                self.welcomeLabel = Label(text="Koniec testu", font=("Arial", 20, "bold"))
                self.welcomeLabel.grid(row=0, column=0, padx=10, pady=10)

                points = checkAnswers(self.questions)
                self.pointsLabel = Label(text=f"Ilość punktów: {points} na {len(self.questions)}", font=("Arial", 15, "bold"))
                self.pointsLabel.grid(row=1, column=0, padx=10, pady=10)

                mark=checkMark(points, len(self.questions))
                self.mark=Label(text=f"Ocena: {mark}", font=("Arial", 13, "bold"))
                self.mark.grid(row=2, column=0, padx=10, pady=10)

                self.quitBtn = Button(width=10, text="Wyjdź", command=self.okno.quit, bg="#ff5656")
                self.quitBtn.grid(row=3, column=0, padx=10, pady=10)

window(Generator.generateQuestions())

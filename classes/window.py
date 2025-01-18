from tkinter import *

class window:
    def __init__(self):
            self.okno = Tk()
            self.okno.title("Quiz")
            self.okno.geometry("500x500")
            self.budujokno()
            self.okno.mainloop()

    def budujokno(self):
            self.etykieta1=Label(text="Test z informatyki")
            self.etykieta1.grid(row=0,column=0, sticky=W) 
            self.odp1=Button(width=10, text="Odpowiedź 1")

            
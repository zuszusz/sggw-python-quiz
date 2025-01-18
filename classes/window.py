from tkinter import *

class window:
        def __init__(self, lista):
                self.okno = Tk()
                self.okno.title("Quiz")
                self.okno.geometry("700x400")
                self.budujokno()
                self.okno.mainloop()
                self.lista=lista

        def budujokno(self):
                self.okno.grid_columnconfigure(0, weight=1) 
                self.etykieta1=Label(text="Test z informatyki", font=("Arial", 20, "bold"))
                self.etykieta1.grid(row=0,column=0, sticky="n") 
                self.przycisk1=Button(width=10, text="Rozpocznij", command=self.budujpytania)
                self.przycisk1.grid(row=1,column=0, sticky="N")
                self.przycisk2=Button(width=10, text="Wyjdź", command=self.okno.quit)

        def budujpytania(self):
                        self.etykieta1.destroy()
                        self.przycisk1.destroy()
                        self.przycisk2.destroy()

                        self.etykieta2=Label(text="Treść pytania?", font=("Arial", 20, "bold"))
                        self.etykieta2.grid(row=0,column=0, sticky="NSEW")

                        x=IntVar()
                        x.set(0)

                        self.odp1=Radiobutton(text="Odpowiedź 1", variable=x, value=1)
                        self.odp1.grid(row=1,column=0, sticky="NSEW")
                        self.odp2=Radiobutton(text="Odpowiedź 2", variable=x, value=2)
                        self.odp2.grid(row=2,column=0, sticky="NSEW")
                        self.odp3=Radiobutton(text="Odpowiedź 3", variable=x, value=3)
                        self.odp3.grid(row=3,column=0, sticky="NSEW")

                        self.przycisk3=Button(width=10, text="Dalej", command=self.budujpytania)
                        self.przycisk3.grid(row=0,column=3, sticky=NSEW)
                        self.przycisk4=Button(width=10, text="Wyjdź", command=self.okno.quit)
                        self.przycisk4.grid(row=2,column=3, sticky=NSEW)
           
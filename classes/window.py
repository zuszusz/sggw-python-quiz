from tkinter import *

class window:
        def __init__(self, lista):
                self.okno = Tk()
                self.okno.title("Quiz")
                self.okno.geometry("700x400")
                self.list=lista
                self.i=0
                self.tresc_pytania = None
                self.odp = []
                self.budujokno()
                self.okno.mainloop()


        def budujokno(self):
                #self.okno.grid_columnconfigure(0, weight=1) 
                self.etykieta1=Label(text="Test z informatyki", font=("Arial", 20, "bold"))
                self.etykieta1.grid(row=0,column=0, sticky="n") 
                self.przycisk1=Button(width=10, text="Rozpocznij", command=self.budujpytania)
                self.przycisk1.grid(row=1,column=0, sticky="N")
                self.przycisk2=Button(width=10, text="Wyjdź", command=self.okno.quit)

        def budujpytania(self):
                        self.etykieta1.destroy()
                        self.przycisk1.destroy()
                        self.przycisk2.destroy()

                        x=IntVar()
                        x.set(0)

                        self.etykietaKtorePytanie=Label(text=f"Pytanie {self.i+1} z {len(self.list)}")
                        self.etykietaKtorePytanie.grid(row=2,column=2, sticky="N")

                        self.budujWidokPytania()

                        self.przyciskDalej=Button(width=10, text="Dalej", command=self.budujWidokPytania)
                        self.przyciskDalej.grid(row=0,column=2, sticky="N")
                        self.przyciskWyjdz=Button(width=10, text="Wyjdź", command=self.okno.quit)
                        self.przyciskWyjdz.grid(row=1,column=2, sticky="N")
     

        def budujEkranKoncowy(self):
                self.etykietaKoniec = Label(text="Koniec quizu", font=("Arial", 20, "bold"))
                self.etykietaKoniec.grid(row=0,column=0, sticky="N")
                self.tresc_pytania.destroy()
                self.przyciskDalej.destroy()
                self.przyciskWyjdz.destroy()
                for i in range(0, len(self.odp)):
                        self.odp[i].destroy()
                self.odp=[]
                self.przyciskWyjdz=Button(width=10, text="Wyjdź", command=self.okno.quit)
                self.przyciskWyjdz.grid(row=1,column=2, sticky="N")


        def budujWidokPytania(self):
                if self.i<len(self.list):
                        if self.tresc_pytania is not None:
                                self.tresc_pytania.destroy() #usuwanie poprzedniego pytania
                                self.tresc_pytania=None #czyszczenie zmiennej
                        if len(self.odp)>0:
                                for i in range(0, len(self.list[self.i].answers)):
                                        self.odp[i].destroy() #usuwanie poprzednich odpowiedzi
                                self.odp=[] #resetowanie listy odpowiedzi
                       
                        self.etykietaKtorePytanie.config(text=f"Pytanie {self.i+1} z {len(self.list)}")
                        self.tresc_pytania=Label(text=self.list[self.i].text, font=("Arial", 20, "bold"))
                        self.tresc_pytania.grid(row=0,column=0, sticky="N")

                        for j in range(0, len(self.list[self.i].answers)):
                               radiobutton = Radiobutton(text=self.list[self.i].answers[j].text, value=j)
                               radiobutton.grid(row=j + 1, column=0, sticky="N")
                               self.odp.append(radiobutton)  # Dodawanie do listy odp
                elif self.i==len(self.list):
                        self.budujEkranKoncowy()
                
                self.i+=1
        

        




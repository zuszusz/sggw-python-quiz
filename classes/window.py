from tkinter import *

class window:
        def __init__(self, lista):
                self.okno = Tk()
                self.okno.title("Quiz")
                self.okno.geometry("700x400")
                self.list=lista
                self.i=0
                self.punkty=0
                self.tresc_pytania = None
                self.odp = []
                self.budujokno()
                self.okno.mainloop()


        def budujokno(self):
                self.etykieta1=Label(text="Test z informatyki", font=("Arial", 20, "bold"))
                self.etykieta1.pack(padx=10, pady=10)
                self.przycisk1=Button(width=10, text="Rozpocznij", command=self.budujpytania, bg="#93bf85")
                self.przycisk1.pack(padx=10, pady=10)
                self.przycisk2=Button(width=10, text="Wyjdź", command=self.okno.quit, bg="#ff5656")
                self.przycisk2.pack()

        def budujpytania(self):
                        self.etykieta1.destroy()
                        self.przycisk1.destroy()
                        self.przycisk2.destroy()

                        x=IntVar()
                        x.set(0)
                        self.okno.columnconfigure(0, weight=1)
                        self.okno.columnconfigure(1, weight=1)
                        self.etykietaKtorePytanie=Label(text=f"Pytanie {self.i+1} z {len(self.list)}")
                        self.etykietaKtorePytanie.grid(row=3,column=1, sticky="WN")

                        self.frame=Frame(self.okno, width=200)  # ramka na odpowiedzi
                        self.frame.grid(row=1,column=0, sticky="N", rowspan=3)


                        self.budujWidokPytania()


                        #przycisk DALEJ
                        self.przyciskDalej=Button(width=10, text="Dalej", command=self.budujWidokPytania, bg="#88b7d5")
                        self.przyciskDalej.grid(row=1,column=1, sticky="WN", pady=10)
                        #przycisk WYJDŹ
                        self.przyciskWyjdz=Button(width=10, text="Wyjdź", command=self.okno.quit, bg="#ff5656")
                        self.przyciskWyjdz.grid(row=2,column=1, sticky="WN", pady=10)
     

        def budujEkranKoncowy(self):
                #niszczenie poprzednich widgetów
                self.tresc_pytania.destroy()
                self.przyciskDalej.destroy()
                self.przyciskWyjdz.destroy()
                self.etykietaKtorePytanie.destroy()
                self.frame.destroy()
                for i in range(0, len(self.odp)):
                        self.odp[i].destroy()
                self.odp=[]

                #budowanie ekranu końcowego
                self.etykietaKoniec = Label(text="Koniec quizu", font=("Arial", 20, "bold"))
                self.etykietaKoniec.grid(row=0,column=0, sticky="N", pady=10)

                self.etykietaKoniec2 = Label(text="Dziękujemy za udział w teście", font=("Arial", 10))
                self.etykietaKoniec2.grid(row=1,column=0, sticky="N", pady=10)

                self.etykietaIlePunktow = Label(text=f"Ilość punktów: {self.punkty}", font=("Arial", 10))
                self.etykietaIlePunktow.grid(row=2,column=0, sticky="N", pady=10)

                self.etykietaOcena = Label(text="Ocena: 6", font=("Arial", 10, "bold"))
                self.etykietaOcena.grid(row=3,column=0, sticky="N", pady=10)

                self.przyciskWyjdz=Button(width=10, text="Wyjdź", command=self.okno.quit, bg="#ff5656")
                self.przyciskWyjdz.grid(row=4,column=0, sticky="N", pady=10)


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
                        self.tresc_pytania.grid(row=0,column=0, sticky="N", pady=15)

                        for j in range(0, len(self.list[self.i].answers)):
                               radiobutton = Radiobutton(self.frame, text=self.list[self.i].answers[j].text, value=j, anchor="w", padx=30)
                               radiobutton.grid(row=j + 1, column=0, sticky="SENW")
                               self.odp.append(radiobutton)  # Dodawanie do listy odp
                elif self.i==len(self.list):
                        self.budujEkranKoncowy()
                
                self.i+=1
        

        




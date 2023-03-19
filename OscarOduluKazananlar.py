

from tkinter import *
class Oscars:
    def __init__(self):
        pencere =Tk()
        pencere.title("Oscar Odulu Kazananları")
        Label(pencere,text="Turler").grid(row=0,column=0)
        Label(pencere,text="Film").grid(row=0,column=1)
        dosya=open('oscars.txt','r')
        self._turset={satır.split(',')[1].rstrip()for satır in dosya}
        dosya.close()
        self.L=list(self._turset)
        self.L.sort()

        self._conOflstTur=StringVar()
        self.lstTur=Listbox(pencere,width=9,height=len(self.L),listvariable=self._conOflstTur)
        self.lstTur.grid(row=1,column=0,padx=10,sticky=N)
        self._conOflstTur.set(tuple(self.L))
        self.lstTur.bind("<<ListBoxSelect>>",self.flims)
        yscroll=Scrollbar(pencere,orient=VERTICAL)
        yscroll.grid(row=1,column=2,sticky=NS)

        self._conOflstFilm=StringVar()
        lstFilmler=Listbox(pencere,width=45,height=len(self.L),listvariable=self._conOflstFilm,yscrollcommand=yscroll.set)
        lstFilmler.grid(row=1,column=1,sticky=NSEW)
        yscroll["command"]=lstFilmler.yview
        pencere.mainloop()

    def flims(self):
        tur=self.lstTur.get(self.lstTur.curselection())
        F=[line.split(',')[0] for line in open('oscars.txt','r')if line.split(',')[1].rstrip(()==tur)]
        self._conOflstFilm.set(tuple(F))
Oscars()

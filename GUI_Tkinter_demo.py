
'''
SCROLLBAR YAPIMI

from tkinter import *
class ScrollText:
   def __init__(self):
       pencere = Tk()
       pencere.title('Kaydirma Çubuğu Örneği')
       frame1 = Frame(pencere)
       frame1.pack()
       scrollbar = Scrollbar(frame1)
       scrollbar.pack(side = 'left',fill=Y)
       metin = Text(frame1,width = 40, height = 10, wrap = WORD,yscrollcommand = scrollbar.set)
       metin.pack()
       metin.insert(END,"")
       scrollbar.config(command = metin.yview)
       pencere.mainloop()
ScrollText()

'''

'''
PENCERE KONUMLANDIRMA

from tkinter import *
class PencereKonumlandirma:
    def __init__(self):
        pencere = Tk()
        pencere.title('Koordinat KonumlandÄ±rma')
        Label(pencere,text = "M A V Ä°", fg = "white",bg = "blue").place(x= 50, y= 50)
        Label(pencere,text = "S A R I", fg = "yellow", bg = "red").place(x= 50, y= 150)
        Label(pencere,text = "K Ä° T A P", fg ="blue", bg="yellow").place(x= 50, y=250)
        pencere.mainloop()
PencereKonumlandirma()

'''
'''
GENİŞLEYİP DARALAN ÇEMBER

from tkinter import *
class CemberHareketi:
    def __init__(self):
        self.boyut = 50
        pencere = Tk()
        pencere.title('Ã‡ember daralÄ±yor geniÅŸliyor')
        self.alan = Canvas(pencere,bg = "light blue", width = 300, height =200)
        self.alan.pack()
        self.alan.create_oval(100-self.boyut,100-self.boyut,100+self.boyut,100+self.boyut,width =2,tags="oval")
        self.alan.bind("<Button-1>",self.buyut)
        self.alan.bind("<Button-3>",self.kucult)
        pencere.mainloop()
    def buyut(self,event):
        self.alan.delete("oval")
        if self.boyut < 100:
            self.boyut += 4
        self.alan.create_oval(100-self.boyut,100-self.boyut,100+self.boyut,100+self.boyut,width =2,tags="oval")
    def kucult(self,event):
        self.alan.delete("oval")
        if self.boyut > 2:
            self.boyut -= 4
        self.alan.create_oval(100-self.boyut,100-self.boyut,100+self.boyut,100+self.boyut,width =2,tags="oval")
CemberHareketi()

'''
'''
LABEL YAPIMI

from tkinter import *
class labeldemo:
    def __init__(self):
        pencere = Tk()
        pencere.title("Etiket Rengini DeÄŸiÅŸtir")
        frame1 = Frame(pencere)
        frame1.pack()
        self.etiket1 = Label(frame1, text = "Programlama Bizim Ä°ÅŸimiz")
        self.etiket1.pack()
        frame2 = Frame(pencere)
        frame2.pack()
        etiket2 = Label(frame2,text = "YazÄ±yÄ± giriniz: ")
        self.msg1 = StringVar()
        entry = Entry(frame2,textvariable=self.msg1)
        btDegistirYazi = Button(frame2,text="YazÄ±yÄ± deÄŸiÅŸtir", command = self.butonabas)
        self.msg2 = StringVar()
        rbRed = Radiobutton(frame2,text = "SarÄ±", bg= "yellow",variable = self.msg2,value = 'Y', command = self.calistirradio)
        rbYellow = Radiobutton(frame2,text = "Mavi", bg= "blue",variable = self.msg2,value = 'B', command = self.calistirradio)
        etiket2.grid(row = 1, column = 1)
        entry.grid(row = 1, column = 2)
        btDegistirYazi.grid(row = 1, column = 3)
        rbRed.grid(row=1, column = 4)
        rbYellow.grid(row = 1, column = 5)
        pencere.mainloop()
    def calistirradio(self):
        if self.msg2.get() == 'Y':
            self.etiket1["fg"] = "red"
            self.etiket1["bg"] ="yellow"
        elif self.msg2.get() == 'B':
            self.etiket1["fg"] = "blue"
            self.etiket1["bg"] ="black"
    def butonabas(self):
        self.etiket1["text"] = self.msg1.get()

labeldemo()

'''
'''
FARE BUTONU OLAYI

from tkinter import *
class MouseKeyEvent:
    def __init__(self):
        pencere = Tk()
        pencere.title("Event DEMO")
        alan = Canvas(pencere,bg = 'light blue',width = 200,height = 100)
        alan.pack()
        alan.bind("<Button-1>",self.farehareketi)
        alan.bind("<Key>",self.tushareketi)
        alan.focus_set()
        pencere.mainloop()
    def farehareketi(self,event):
        print('TÄ±klandÄ±: ',event.x,event.y)
        print('Ekrandaki konumu: ',event.x_root,event.y_root)
        print('Hangi butona tÄ±klandÄ±',event.num)
    def tushareketi(self,event):
        print('Anahtar?',event.keysym)
        print('Karakter?',event.char)
        print('Anahtar Kodu?',event.keycode)
MouseKeyEvent()

'''
'''
EYALETLER VE SENATÖRLERİ

from tkinter import *
class Senators:
    def __init__(self):
        pencere = Tk()
        pencere.title("Eyaletler SenatÃ¶rleri")
        Label(pencere,text = "Eyalet: ",width=5).grid(row=0,column=0,sticky=E)
        self.state = StringVar()
        entState = Entry(pencere,textvariable=self.state)
        entState.grid(row=0, column=1, sticky=W)
        entState.focus_set()
        entState.bind("<Button-1>",self.clearBoxes)

        btnDisplay = Button(text = "SenatÃ¶rleri GÃ¶ster", command=self.senate)
        btnDisplay.grid(row=1, columnspan=2,pady=10)
        self.L=[]
        self.listContents = StringVar()
        self.listContents.set(tuple(self.L))
        lstSenators = Listbox(pencere, height = 2, width=21,listvariable=self.listContents)
        lstSenators.grid(row=2,column=0,columnspan=2,padx=44,pady=2)
        pencere.mainloop()
    def clearBoxes(self,e):
        self.state.set("")
        self.listContents.set(tuple([]))
    def senate(self):
        self.L = []
        result = self.state.get()
        dosya = open('senate.txt','r')
        for satir in dosya:
            temp = satir.split(',')
            if temp[1]== result:
                self.L.append(temp[0] + " " + temp[2])
                self.listContents.set(tuple(self.L))
        dosya.close()
Senators()

'''
'''
OSCAR ÖDÜLÜ KAZANAN TÜRLER
from tkinter import *
class Oscars:
    def __init__(self):
        pencere = Tk()
        pencere.title("Oscar Ã–dÃ¼lÃ¼ Kazananlar")
        Label(pencere, text = "TÃœR").grid(row=0, column=0)
        Label(pencere, text="Filmler").grid(row=0,column=1)
        dosya = open('oscars.txt','r')
        self._genreSet = {satir.split(',')[1].rstrip()for satir in dosya}
        dosya.close()
        self.L = list(self._genreSet)
        self.L.sort()

        self._conOFlstGenres = StringVar()
        self._lstGenres = Listbox(pencere,width=9,height=len(self.L),listvariable=self._conOFlstGenres)
        self._lstGenres.grid(row=1,column=0,padx=10,sticky=N)
        self._conOFlstGenres.set(tuple(self.L))
        self._lstGenres.bind("<<ListboxSelect>>",self.films)
        yscroll = Scrollbar(pencere,orient=VERTICAL)
        yscroll.grid(row=1,column=2,sticky=NS)
        self._conOFlstFilms = StringVar()
        lstFilms = Listbox(pencere,width=45, height=len(self.L),listvariable = self._conOFlstFilms,yscrollcommand=yscroll.set)
        lstFilms.grid(row=1,column=1,sticky=NSEW)
        yscroll["command"] = lstFilms.yview
        pencere.mainloop()

    def films(self,e):
        genre = self._lstGenres.get(self._lstGenres.curselection())
        F = [line.split(',')[0] for line in open('oscars.txt','r') if line.split(',')[1].rstrip() == genre]
        self._conOFlstFilms.set(tuple(F))
Oscars()

'''
'''
YILLARA GÖRE OSCARLAR
from tkinter import *
class Oscars:
    def __init__(self):
        pencere = Tk()
        pencere.title("YÄ±llara GÃ¶re Oscarlar")
        caption = "YÄ±l (1928 - 2013): "
        Label(pencere,text=caption).grid(row=0,column=0)
        self._conOFentYear = StringVar()
        self.entYear = Entry(pencere, width = 4,textvariable=self._conOFentYear)
        self.entYear.grid(row=0,column=1,sticky=W)
        caption = "En iyi Film"
        btnAra = Button(pencere,text=caption,command=self.gosterFilm)
        btnAra.grid(row=1,column=1,pady=2)
        Label(pencere,text="Film: ").grid(row=2,column=0,sticky=E)
        Label(pencere,text="TÃ¼r:  ").grid(row=3,column=0,pady=5,sticky=E)
        self._conOFentFilm = StringVar()
        self.entFilm = Entry(pencere,width =30,state="readonly",textvariable=self._conOFentFilm)
        self.entFilm.grid(row=2,column=1,padx=5,sticky=W)
        self._conOFentGenre = StringVar()
        self.entGenre = Entry(pencere,width=30,state="readonly",textvariable=self._conOFentGenre)
        self.entGenre.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        pencere.mainloop()
    def gosterFilm(self):
        dosya = open('oscars.txt','r')
        for i in range(int(self._conOFentYear.get())-1928):
            dosya.readline()
        satir = dosya.readline().rstrip()
        dosya.close()
        data = satir.split(',')
        self._conOFentFilm.set(data[0])
        self._conOFentGenre.set(data[1])
Oscars()

'''
'''
ANİMASYON KONTROLÜ

from tkinter import *
class ControlAnimation:
    def __init__(self):
        pencere = Tk()
        pencere.title("Animasyonda Kontrol Bende !")
        self.width =250
        self.alan = Canvas(pencere,bg='Light Yellow',width=self.width,height=50)
        self.alan.pack()
        frame1 = Frame(pencere)
        frame1.pack()
        btStop = Button(frame1,text = "Durdur", command = self.stop)
        btStop.pack(side=LEFT)
        btDevam = Button(frame1,text = "Devam", command = self.devam)
        btDevam.pack(side=LEFT)
        btFaster = Button(frame1,text = "HÄ±zlandÄ±r", command = self.faster)
        btFaster.pack(side=LEFT)
        btYavaslat = Button(frame1,text = "YavaÅŸlat", command = self.yavaslat)
        btYavaslat.pack(side=LEFT)
        btSil = Button(frame1,text = "Siliver", command = self.sil)
        btSil.pack(side=LEFT)
        self.giris = Entry(frame1)
        self.giris.pack(side=LEFT)
        self.alan.bind("<Enter>",self.gonder)
        self.x = 0
        self.sleepTime = 100
        self.alan.create_text(self.x,30,text=self.giris.get(),tags='text')
        self.dx = 3
        self.isStopped = False
        self.animate()
        pencere.mainloop()
    def gonder(self,event):
        self.animate()
    def stop(self):
        self.isStopped = True
    def devam(self):
        self.isStopped = False
    def faster(self):
        if self.sleepTime > 5:
            self.sleepTime -=20
    def yavaslat(self):
        self.sleepTime +=20
    def sil(self):
        self.alan.delete("text")
    def animate(self):
        while not self.isStopped:
            self.alan.move("text",self.dx,0)
            self.alan.after(self.sleepTime)
            self.alan.update()
            if self.x < self.width:
                self.x += self.dx
            else:
                self.x = 0
                self.alan.delete("text")
                self.alan.create_text(self.x,30,text=self.giris.get(),tags="text")
  ControlAnimation()

'''
'''
POPUP MENU

from tkinter import *
class PopupMenu:
    def __init__(self):
        pencere = Tk()
        pencere.title("Popup MenÃ¼ Denemeleri")

        self.menu = Menu(pencere,tearoff = False)
        self.menu.add_command(label="Ã‡izgi Ã‡iz",command = self.displayLine)
        self.menu.add_command(label="Oval Ã‡iz",command = self.displayOval)
        self.menu.add_command(label="DikdÃ¶rtgen Ã‡iz",command = self.displayRect)
        self.menu.add_command(label="Temizle",command = self.temizle)
        self.menu.add_separator()
        self.menu.add_command(label="Ã‡Ä±kÄ±ÅŸ",command = pencere.destroy)

        self.alan = Canvas(pencere, width=200,height= 100,bg ='light blue')
        self.alan.pack()

        self.alan.bind("<Button-3>",self.popup)
        pencere.mainloop()

    def displayRect(self):
        self.alan.create_rectangle(10,10,190,90,tags = 'rect')
    def displayOval(self):
        self.alan.create_oval(10,10,190,90,tags = 'oval')
    def displayLine(self):
        self.alan.create_line(10,10,190,90,tags = 'line')
        self.alan.create_line(10,90,190,10,tags = 'line')
    def temizle(self):
        self.alan.delete('rect','oval','line')
    def popup(self,event):
        self.menu.post(event.x_root,event.y_root)
PopupMenu()

'''
'''
BASİT HESAP MAKİNESİ
from tkinter import *
class menu:
    def __init__(self):
        pencere = Tk()
        pencere.title("Basit Hesap Makinesi")

        menubar = Menu(pencere)
        pencere.config(menu = menubar)
        menuislem = Menu(menubar, tearoff = 1)
        menubar.add_cascade(label = "Ä°ÅŸlem SeÃ§", menu= menuislem)
        menuislem.add_command(label = "Topla", command = self.topla)
        menuislem.add_command(label = "Ã‡Ä±kart", command = self.cikart)
        menuislem.add_separator()
        menuislem.add_command(label = "Ã‡arp", command = self.carp)
        menuislem.add_command(label = "BÃ¶l", command = self.bol)

        cikismenu = Menu(menubar,tearoff = -100)
        menubar.add_cascade(label = "Ã‡Ä±kÄ±ÅŸ", menu= cikismenu)
        cikismenu.add_command(label = "Ã‡Ä±k", command = pencere.destroy)

        frame0 = Frame(pencere)
        frame0.grid(row = 1, column=1,sticky = W)

        plusImage = PhotoImage(file = "plus.gif")
        minusImage = PhotoImage(file = "minus.gif")
        timesImage = PhotoImage(file = "times.gif")
        divideImage = PhotoImage(file = "divide.gif")

        Button(frame0, image= plusImage, command = self.topla).grid(row=1, column= 1)
        Button(frame0, image= minusImage, command = self.cikart).grid(row=1, column= 2)
        Button(frame0, image= timesImage, command = self.carp).grid(row=1, column= 3)
        Button(frame0, image= divideImage, command = self.bol).grid(row=1, column= 4)

        frame1 = Frame(pencere)
        frame1.grid(row = 2, column=1,pady =10)
        Label(frame1,text = "SayÄ± 1: ").pack(side=LEFT)
        self.v1 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v1, justify= RIGHT).pack(side = LEFT)
        Label(frame1,text = "SayÄ± 2: ").pack(side=LEFT)
        self.v2 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v2, justify= RIGHT).pack(side = LEFT)
        Label(frame1,text = "SonuÃ§: ").pack(side=LEFT)
        self.v3 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v3, justify= RIGHT).pack(side = LEFT)

        frame2 = Frame(pencere)
        frame2.grid(row = 3, column = 1,pady = 10, sticky = E)
        Button(frame2,text = "ToplayÄ±Ver", command = self.topla).pack(side= LEFT)
        Button(frame2,text = "Ã‡Ä±karÄ±Ver", command = self.cikart).pack(side= LEFT)
        Button(frame2,text = "Ã‡arpÄ±Ver", command = self.carp).pack(side= LEFT)
        Button(frame2,text = "BÃ¶lÃ¼Ver", command = self.bol).pack(side= LEFT)

        mainloop()
        #pencere.mainloop()

    def topla(self):
        self.v3.set(eval(self.v1.get()) + eval(self.v2.get()))
    def cikart(self):
        self.v3.set(eval(self.v1.get()) - eval(self.v2.get()))
    def carp(self):
        self.v3.set(eval(self.v1.get()) * eval(self.v2.get()))
    def bol(self):
        self.v3.set(eval(self.v1.get()) / eval(self.v2.get()))
menu() 

'''
'''
BÜYÜK ŞEHİRLER

from tkinter import *
def displayData(e):
    lake = lstLakes.get(lstLakes.curselection())
    conOFentArea.set{"{0:,d}".format(lakesDict[lake])}
window = Tk()
window.title("BÃ¼yÃ¼k ÅŸehirler")
global lakesDict
lakesDict = {"Istanbul":2300,"Ankara":3000,"Izmir":1500,"KÄ±rsehir":5000}
lakeList = list((lakesDict).keys())
lakeList.sort()
conOFlstLakes = StrnigVar()
global lstLakes
lstLakes = Listbox(windoq,height=5iwidth=9,listvarible=conOFlstLakes)
lstLakes.grid(row=0,column=0,padx=5,pady=5,rowspan=5,sticky=NSEW)
conOFlstLakes.set(tuple(lakeList))
lstLake.bind("<<ListboxSelect>>",displayData)
Label(window,text="YÃ¼z Ã¶lÃ§Ã¼mÃ¼(km2):"),grid(row=2,column=1,sticky=E)
conOFenContinent = StringVar()
conOfentArea = StringVar()
entArea = Enrty(window,width=7,state="readonly",textvarible=conOFentArea)
entArea.gridrow=2,column=2,padx=5)
window.mainloop()

'''
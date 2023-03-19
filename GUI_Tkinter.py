from tkinter import*
# from tkcalendar import DateEntry
master=Tk()

canvas=Canvas(master,height=450,width=750)
# konumu tk ya eklemek ıcın kulllandıgımız komutlar (pack,place,grid)
canvas.pack()

frame_ust=Frame(master,bg='#add8e6')
frame_ust.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)


frame_alt_sol=Frame(master,bg='#add8e6')
frame_alt_sol.place(relx=0.1,rely=0.21,relwidth=0.23,relheight=0.5)


frame_alt_sag=Frame(master,bg='#add8e6')
frame_alt_sag.place(relx=0.34,rely=0.21,relwidth=0.56,relheight=0.5)

hatirlatma_tipi_etiket=Label(frame_ust,bg='#add8e6',text="Hatırlatma Tipi:",font="verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10,pady=10,side=LEFT)

hatirlatma_tipi_opsiyon=StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("\t") # degult bı deger atadık .set ıle

hatirlatma_tipi_acilir_menu=OptionMenu(
    frame_ust,
    hatirlatma_tipi_opsiyon,
    "dogum gunu",
    "alisveris",
    "odeme")
hatirlatma_tipi_acilir_menu.pack(padx=10,pady=10,side=LEFT)

# hatirlatma_tarih_secici=DateEntry(frame_ust,width=12,background='orange',foreground='black',borderwidth=1,locale='de_DE')
# hatirlatma_tarih_secici._top_cal.overriderederedirect(False)
# hatirlatma_tarih_secici.pack(padx=10,pady=10,side=RIGHT)

hatirlatma_tipi_etiket=Label(frame_ust,bg='#add8e6',text="Hatırlatma Türü:",font="verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10,pady=10,side=LEFT)

Label(frame_alt_sol,text="Hatirlatma Yöntemi",bg='#add8e6',font="verdana 10 bold").pack(padx=10,pady=10,anchor=NW) 
# normalde label'ı degısken olarak tanımlasaydık deg=label(frame_alt_sag,text="hatırlatma yontemı",bg='#add8e6',font="verdana 12 bold")
# deg.pack() yazmamız gerekırdı ama bellekte ayrı bır yer kaplamaması ıcın label'ım sonuna .pack() ekledık buna yol ustunde tanımlama denır 

var=IntVar()       

r1=Radiobutton(frame_alt_sol,text="Sisteme kaydet",variable=var,value=1,bg='#add8e6',font="verdana 10 bold")
r1.pack(padx=15,pady=5,anchor=NW)
# radıobutton lar bırbırıyle alakalı oldugu ıcın bırını seı-cınce dıgerının degısmesı lazım 
# bunu da var degerı atayarak ogrenıyoruz var=IntVar() degerını tanımladık
#  radıobuttonlarda var degerını varıable degerıne atıyoruz value degerı ıle de aldıgı degerı degıstıryoruz .
r2=Radiobutton(frame_alt_sol,text="E-posta gonder",variable=var,value=2,bg='#add8e6',font="verdana 10 bold")
r2.pack(padx=15,pady=5,anchor=NW) #anchor capa degerı tabloda hangı tarafa yatkın olcagını secıyoruz padx,pady ıle de kenarlar arası mesafeyı ayalıyoruz.

var1=IntVar()
c1=Checkbutton(frame_alt_sol,text="bir hafta once",variable=var1,onvalue=1,offvalue=0,bg='#add8e6',font="verdana 10 ")
c1.pack(padx=25,pady=2,anchor=NW)

var2=IntVar()
c2=Checkbutton(frame_alt_sol,text="bir gun once",variable=var2,onvalue=1,offvalue=0,bg='#add8e6',font="verdana 10 ")
c2.pack(padx=25,pady=2,anchor=NW)

var3=IntVar()
c3=Checkbutton(frame_alt_sol,text="ayni gun",variable=var3,onvalue=1,offvalue=0,bg='#add8e6',font="verdana 10 ")
c3.pack(padx=25,pady=2,anchor=NW)

from tkinter import messagebox

def gonder(): #normalde 80. satırda yazan dommand=master.detroy'un yerınde command=gonder olması onunda bradakı fonk. ıcerısındekılerı yapması gerekıyo gostermelık olsun dıye yaptım.
  son_mesaj=""
  try:
    if var.get():
        if var.get()==1:
            son_mesaj+="Veriniz basariyla sisteme kaydedilmistir."           

            tip=hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon.get()=='' else "Genel"
            # tarih=hatirlatma_tarih_secici.get()
            mesaj=metin_alani.get("1.0","end")

            with open("hatirlatma.txt","w")as dosya:
                dosya.write(
                    '{} katagorisinde,{} notuyla hatirlatma'.format(
                    tip,
                    # tarih,
                    mesaj
                    ))   
                dosya.close()        

        elif var.get()==2:
            son_mesaj+="E-posta yoluyla hatirlatma size ulasacaktir."
        messagebox.showinfo("Basarili islem",son_mesaj)
        # buradakı basarılı islem mesaj kutusunun baslıgı olacak son_mesaj da hangı value degerını alırsa o
    else:
        son_mesaj+="Gerekli alanlari doldurdugunuzdan emin olun."
        messagebox.showwarning("Yetersiz Bilgi",son_mesaj)
  except:
        son_mesaj+="islem basarisiz oldu'."
        messagebox.showerror("Basarisiz islem",son_mesaj)
  finally:
    master.destroy()
    return


Label(frame_alt_sag,text="Hatirlatma Mesaji",bg='#add8e6',font="verdana 10 bold").pack(padx=10,pady=10,anchor=NW) 

metin_alani=Text(frame_alt_sag,height=9,width=50)
metin_alani.tag_configure('style',foreground='#bfbfbf',font="verdana 13 bold ")
metin_alani.pack()

karsilama_metni="mesajini buraya gir.."
metin_alani.insert(END,karsilama_metni,'style') # karsılama metnını ınsert ıle metın alanının ıcıne koyduk

gonder_butonu=Button(frame_alt_sag,text="Gonder",command=gonder) #gonder butonuna bastıgı zaman komple butun master'ı sekmeyı kapatır.
gonder_butonu.pack(anchor=S,pady=4)


master.mainloop()


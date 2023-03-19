

from base64 import encode
from operator import truediv

def not_hesapla(satır):
   satır=satır[:-1] # satrı aralarında boslukları aldık.
   liste=satır.split(':') # isim ile notları ':' isaretinden sonra split ile ayırdık
   ogrencı_adı=liste[0] # ayırdıgımız ısım ile notları index numaraları ile ögrencı adı ve notlar olarak atadık
   notlar=liste[1].split(',') # 3 adet notu ayrı ayrı ıslem yapabılmek ıcın tekrar splıt ıle ayırdık.

   not1=int(notlar[0]) # ilk girilen not
   not2=int(notlar[1])
   not3=int(notlar[2])

   ortalama=(not1+not2+not3)/3

   if ortalama>=90 and ortalama<=100:
    harf='AA'
   elif ortalama>=85 and ortalama<=89:
    harf='BB'
   elif ortalama>=80 and ortalama<=84:
    harf='BA'
   elif ortalama>=75 and ortalama<=79:
    harf='CB'
   elif ortalama>=70 and ortalama<=74:
    harf='CC'
   elif ortalama>=65 and ortalama<=69:
    harf='DC'
   elif ortalama>=60 and ortalama<=64:
    harf='DD'
   elif ortalama>=50 and ortalama<=59:
    harf='FD'
   else:
    harf='FF'

   return ogrencı_adı+' :'+harf+ '\n'   # return ile not_hesaplaya gerı dondu.

        
def ortalamaları_oku():
    file=open('sınav_notları.txt','r',encoding='utf-8')
    for satır in file:
        print(not_hesapla(satır))


def not_gir():
    ad=input('ögrenci adı:')
    soyad=input('ögrenci soyadı:')
    not1=input('not1:')
    not2=input('not2:')
    not3=input('not3:')

    file=open('sınav_notları.txt','a',encoding='utf-8')
    file.write(ad+' '+soyad+':'+not1+' ,'+not2+' ,'+not3+'\n') # input olarak aldıgımız ısım soyısım not bılgılerını write ile doyaya yazdık.
    file.close()


def notları_kaydet():
    file=open('sınav_notları.txt','r',encoding='utf-8')
    liste=[] # bos bır lıste olusturduk gelen bılgılerı yazıp kaydetmek ıcın

    for i in file:
        liste.append(not_hesapla(i)) # not_hesapla ıcerısıne return ıle gelen bılgılerı al
        #append ıle olusturdugumuz lıstenın ıcerısıne at dedık

    file2=open('sonuclar.txt','w',encoding='utf-8') # yenı bır dosya actık ve buraya listenın 
    # ıcıne atmıs oldugumuz isim ve not bılgısını al yazdır dedık. bu bıze sonuclar adında bır dosya ıle gelecek.
    for i in liste: 
        file2.write(i) 
    file2.close()     


while True:
    islem=input('1-notları oku\n2-not gir\n3-notları kaydet\n4-cıkıs\n')
    if islem=='1':
        ortalamaları_oku()
    elif islem=='2':
        not_gir()
    elif islem=='3':
        notları_kaydet()
    else:
        break
        
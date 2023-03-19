'''
Daıre Alanı : πr2
Daıre Cevre :2πr

*Kullanıcıdan alınan yarıcap uzunlugu ıle daıre alan ve cevreyı hesaplayınız(π=3.14)

'''

r=float(input("yarıcap: ")) 
# r=float(ınput("yarıcap: ")) yaparak strıng olarak aldıgımız yaarı cap bılgıısını float turune cevırmıs olduk.

pi=3.14

daırealan=pi*r**2 ##carpı ıslemını yanı * ıkı sefer kullandıgımızda ussu anlamına gelır
print("Daıre Alan:",daırealan)
daırecevre=2*pi*r
print("Daıre Cevre:",daırecevre)
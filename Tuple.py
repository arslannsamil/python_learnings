
from tkinter import N


list=[1,2,3]
tuple=(1,'ıkı',3) #tuple tanımlarken lıstlerden farklı olarak ya normal parantez yada parantezsız kullanım yapılır

'''
print(type(list))
print(type(tuple))

print(list[1])
print(tuple[1])

print(len(list)) #list dızısının len'ı yanı uznlugu (length) kac elemanlı oldugu
print(len(tuple)) # aynı mantık

'''
# Yukarıda tanımlamıs oldugumuz lıst ve tuple dızılerının uzerıne en bastan eleman ataması yapabılırız
#artık en son tanımlamıs oldugumuz dızı elemanları ekrana verılır.

list=['yusuf','ahmet'] 
tuple=('asım','samıl')

list[0]='ali' # Lıst dızısnın 0.ındexının yerıne alı ısmını atadım. Hıcbır sıkıntı cıkmadan kod calısır

tuple[0]='mehmet' # List dızısıne yaptıgımın aynısını tuple dızısıne yaptım ve kabul etmedı hata verdı
# tuple ıle lıst aynı ıslevsellıge yaarasa da bu konuda farklıdırlar
# tuple turunde olusturulen dızıye ılave yapılamaz ama aynı tuple dızısıne en bastan eleman yazılabılır.

print(list)
print(tuple)
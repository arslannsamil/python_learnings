'''
x=input("1.sayı: ") #ınput ıle aldıgımız degerler strıng olarak gırılır ıslem yaptırmak ıcın donusturme yapmalıyız

y=input("2.sayı: ")
print(type(x)) #ılk basta strıng olduklarını gormek ıcın yazdırdık
print(type(y))

toplam=int (x)+int (y) #burda strıng olan x ve y yı ıntegera donusturdum 

print(toplam) # bu ıslemı yaptıgımız zaman gırdıgımız sayılar yan yana yazılır cunku strıng olarak deger gırdık
#bunun degıstırmek ıcın strıng olan x ve y yı ıntager a donusturmemız gerekır

\n yaptıgımız zaman bır satır asagıya ıner 

'''

from html.entities import name2codepoint
from operator import truediv
from socket import ntohl
import string
from tkinter import N
from tokenize import single_quoted
from unittest import result


x=5            #int
y=2.5          #float
name='samıl'   #str
ısonlıne=True #bool

'''
print (type(x))
print (type(y))
print (type(name))
print (type(ısonlıne)) turlerını yazdırdık

'''
# Type Conversıon

'''
# İnt to float 
x=float(x)  
print(x) #ınteger olan 5 degerını floata cevırdıgımımz ıcın 5.0 olarak gosterdı.
print(type(x))

'''

'''
# float to ınt
y=int(y)
print(y) #y yı ıntagere cevırdıgımız ıcın 2 den sonra olan kusurat kaybolur 
print(type(y))

'''

result=str(x)+str(y) #ıntager olan x ve y degerlerını strınge cevırıp yan yana yazdırdık
print(result)
print(type(result))


# bool to intager

ısonlıne=int(ısonlıne) #boole da olan false degerı ıntager oldugu zaman o olarak yazılır true=1 dır
print(ısonlıne)
print(type(ısonlıne))






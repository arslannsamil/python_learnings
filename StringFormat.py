from msvcrt import kbhit
from socket import ntohl
from turtle import TurtleScreenBase


name='sadık'
surname='turan'
age=36

print=('my name ıs '+name+' '+surname+'and \n I am '+str(age)+' years old.')
# \n sembolu cıktı alırken \n e kadar olan kısmı yazdırdıktan sonra kalan ksımı bır alt satıra yazdırmaya yarar.

# Yazdırırken teker teker tırnak acmak ve age gıbı ınteger degerlerı cevırmekle ugrasmamak ıcın -
# strıng formatlama denen metotlar kullanılır

name='cınar'
surname='arslan'

#print('my name ıs {} {} '.format(name,surname))


print('my name ıs {0} {1} '.format(name,surname)) #bu sekılde yazdıgımız zaman sıralamada degısen bısey olmaz 
#cunku kayıtlı oldukları ındex numaraları bu sekıldedır ama suslu parantez ıcleındekı ındex numaralarını degıstırırsek 
#bu sefer name ve surname ıfadelerının yazım sıraları da degısmıs olur.


#print('my name ıs {n} {s} '.format(n=name,s=surname)) bu da farklı bı yazı cesıdı


# print("my name ıs {} {} and I'am {} years old." .format(name,surname,'36')) bu sekılde de yazmamızda bı sıkıntı yok.
# eger 36 ıfadesı tanımlı olursa buraya turu fark etmeksızın yazmamızda bı sıkıntı olmazdı. ISTE BURADA YUKARIDA TEK TEK
#TIRNAK VE + ISARETI KULLANARAK YAZDIGIMIZ PRINT ISLEMINDEN FARKI ORTAYA CIKIYOR CUNKU O PRINT IFADESINDE TUR DONUSUMU YAPMAMIZ GEREKIYORDU.



# print("my name ıs {} {} and I'am {} years old." .format(name,name,name)) bu sekılde aynı ıfadeyı tekrar tekrar da yazırabılırız



# print("my name ıs {} {} and I'am {} years old." .format(name,surname,'36')) bu sekılde yazmaktansa 
print(f"my name ıs {name} {surname} and I'am {age} years old.") #seklınde daha basıt bır sekılde de tur donusumune gerek kalmadan yazabılırız.



result=200/700 

print('the result ıs{r:1.3}'.format(r=result)) # 1 rakamı cıkan kusuratlı ıslemın vırgulden oncekı basamak sayısını 
#3 rakamı ıse vırgulden sonrakı gorulmek ıstenen basamak sayısını ıfade eder.


# bi ifadenin kac karakterli oldugunu ogrenmek icin ornk course kac karakterlidir ve ılk uc karakterı alır mısınız derse
course="bugun sabah kalktıgımda yumurta ve ekmek yedım" #tırnaklar ındexlere dahıl degıldır
# result =len(course)
# print(result)

result=course[0:2] # 0 1 2 seklınde ındex numaraları tanımlanır Eger sondan baslarsak -1 dıye baslayıp gıtmemız gerekır 
#print(result)

# s="hello world" ıfadesındekı w harfını Wyapmak ıstersek
# s.replace('w','W')seklınde ayaparsak ılk yazdıgım harf ıle ıkıncı yazdıgım harfı degıstırmıs olurum.



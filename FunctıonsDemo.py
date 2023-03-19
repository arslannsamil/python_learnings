




# Gonderılen mesajı ıstenılen kadar ekrana yazdıran fonksıyonu yazın


# def yazdır(mesaj,adet):
#     print(mesaj*adet)

# yazdır('samıl\n',5) # \n yapmamızın nedenı cıktıda ısımlerı alt alta vermesını ıstememız







# Kendıne gonderılen sınırsız sayıdakı parametreyı bır lısteye cevıren fonksıyonu yazınız


# from dataclasses import replace
# from unittest import result


# def lısteyecevır(*params): #burada onemlı olan yıldız params yerıne baska bırsey de yazılabılır
#     list=[]
#     for param in params:
#         list.append(param)

#     return list

# result=list[1,3,5,'samıl',5.6,False] 

# print(result)





# Gonderılen ıkı sayının arasındakı tum asal sayıları bulun fonksıyon yardımıyla

# def asalsayilaribulma(sayı1,sayı2):

#     for sayı in range(sayı1,sayı2):
#         if sayı>1:
#             for i in range(2,sayı):
#                 if sayı%i==0:
#                     break
#             else:
#                 print(sayı)    

# sayı1=int(input('sayı 1 :'))
# sayı2=int(input('sayı 2 :'))

# asalsayilaribulma(sayı1,sayı2)




# Kendısıne gonderılen bır sayının tam bolenlerını bır lıste seklınde fonksıyondan gerı gonderın


# def tambolenlerıbulma(sayı):
#     tambolenlerlıstesı=[]
#     for i in range(1,sayı):
#         if sayı%i==0:

#             tambolenlerlıstesı.append(i)
    
#     return tambolenlerlıstesı #bu kısmı for ıcerısıne yazarsak ılk eleman lısteye gırdıkten sonra lısteyı ekrana verır dongu bozulur.

# print(tambolenlerıbulma(20))    
































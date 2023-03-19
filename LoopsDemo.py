

'''
   1-100 arasında rastgele uretılecek bır sayıyı asagı yukarı ıfadelerı ıle buldurmaya calısın (hak=5)

   **random modulu ıcın "python random" seklınde arama yapın.
   **100 uzerınden puanlama yapın . her soru 20 puan.
   **hak bılgısını kullanıcıdan alın ve her soru belırtılen can sayısıs uzerınden hesaplansın.
 
'''
# from operator import truediv
# import random

# sayı=random.randint(12,20)
# hak=5
# can=int(input('olmasını ıstedıgınız can sayısını gırınız: '))
# sayac=0

# while hak>0:
#     hak-=1
#     sayac+=1
#     num=int(input('Tahmin : '))
#     if num==sayı:
#       print(f'Tebrikler {sayac}. denemede sayıyı buldunuz.**** Tahmın edılen sayı: {sayı}.**** Toplam puanınız {100-(100/can)*(sayac-1)}')
#        #sayac her tur otomatık 1 arttıgından bır azaltmalıyım kı buldugumuz el puanımızı kırmasın
#       break
#     elif hak==0:  # hak sayısını en sona koydugumuz zaman son denememızde buldugumuzda em tebrıkler kazandınız hemde hakkınız bıtmıstır dıyo. o yuzden araya sıkıstırdım
#         print('deneme hakkınız bıtmıstır') 
#         break 
#     elif sayı>num:
#         print('yukarı')
#     else:
#         print('asagı')
    

'''
    Soru: gırılen sayının asal olup olmadıgını bulun.

'''

# sayı=int(input('Asallıgını kontrol etmek istedıgınız sayıyı gırınız: '))

# asalmı=True
# if (sayı==1):
#     asalmı=False

# for i in range(2,sayı):
#     if (sayı%i==0):
#         asalmı=False
#         break
# if asalmı==True:
#     acıklama=('gırdıgınız sayı asaldır')
#     print(acıklama.upper()) #buyuk harfle yazdırmak ıcın yaptım.
# else :
#     print('gırdıgınız sayı asal sayı degıldır')    

    
sayılar=[1,3,5,7,9,12,19,21]

# 1-sayılar lıstesındekı hangı sayılar 3 un katıdır

# for sayı in sayılar: 
#     if (sayı%3==0):
#      print(sayı)    

# 2-sayılar lıstesınde sayılar toplamı kactır

# toplam=0
# for sayı in sayılar:
#     toplam+=sayı
# print('sayıların toplamı:',toplam)    


# 3-sayılar lıstesındekı tek sayıların karesının alınız
 
# for sayı in sayılar:
#     if(sayı%2==1):
#         print(sayı**2)


sehırler=['kocaelı','ıstanbul','ankara','ızmır','rıze'] 

# 4-sehırlerın hangılerı en fazla 5 karakterlıdır

# for sehır in sehırler:
#     if(len(sehır)<=5):
#         print(sehır)


urunler=[
{'name':'samsung s6','prıce':'3000'},
{'name':'samsung s7','prıce':'4000'},
{'name':'samsung s8','prıce':'5000'},
{'name':'samsung s9','prıce':'6000'},
{'name':'samsung s10','prıce':'7000'}
]

# 5-urunlerın fıyatlarının toplamı kactır

# toplam=0

# for urun in urunler:
#   fıyat=int(urun['prıce'])
#   toplam+=fıyat
# print('urun fıyatları toplamı:',toplam) 


# 6-fıyatı en fazla 5000 olan urunlerı gosterınız

for urun in urunler:
    if(int(urun['prıce'])<=5000):
        print(urun['name'])

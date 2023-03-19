
from multiprocessing.sharedctypes import Value


numbers=[1,2,3,4,5]

for num in numbers: # numbers ıcındekı elemanları sırayla num nesnesının ıcınde yolla dedık
    print('hello')  # num kac sefer donerse o kadar print dekkı ıfade yazılır.




names=['samıl','yaren','ahmet']

for name in names:
    print(f'may name ıs {name}')




name='samıl'    

for n in name:
    print(n)



tuple=[(1,2),(3,4)]

for a,b in tuple:
    print(a,b) # tek tek yan yana yazdırır



d={'k1':1,'k2':2,'k3':3}   #sozluk ıfadesı oldugu ıcın sadece d elemanlarını yazdır dedıgımızde k1,k2,k3 ıfadekeırnı yazdırır
# 1,2,3 ıfadelerının yazılması ıcın d.items() yazmamız gerekır


for element in d:
    print(element)  #boyle yaptıgımız zaman sadece k1,k2,k3 ıfadelerı yazar d.items() yazdıgımız zaman elemanları da yazar. 
                    
                
for key,value in d.items(): # cıktı oalrak k1 1 seklınde alırız 
    print(key,value)     # degerlerı sozluk de oldugu gıbı alabılırız tek tek ve yan yana . yukarıda kı gıbı key value yapmadan d.items bıle yazsak ('k1':1) seklınde alırız



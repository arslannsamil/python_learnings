

#Recursion: Fonskıyonun kendı kendını cagırması
# 1- Fonksıyonun kendını sureklı cagırmaması ıcın bıtıs noktası tanımlanmalı
# 2- Fonskıyonun belırlı sartlarda kendını cagırması gereklı

# Recursıon , dongulerın yerıne kullanılabıllır.

'''

def toplam(liste):
    toplam=0
    for i in liste:
        toplam+=i
    return toplam
print (topla([1,2,3,4]))

'''
# Yukarıda dongu ıle yaptıgımız ıslemı Recursıon ıle yapacagız.

def topla(liste):
    if (len(liste))==0:
        return 0
    else:
        return liste[0]+(topla(liste[1:]))
print(topla([1,2,3,4]))  # print(topla(1,2,3,4)) yaptıgım zaman hata verıyo 

'''
CALISMA MANTIGI: 

return 1+ topla([2,3,4])
return 2+ topla([3,4])
return 3+ topla([4])
return 4+ topla([])
return 0

1 + (2 + (3 + (4+0)))  seklınde bır ıslme ortaya cıkar...


'''



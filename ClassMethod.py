
class Cırcle:
    # class attrıbutes
    pi=3.14
    
    def __init__(self,yarıcap=1): # yarıcap degerı gırılmez ıse degerı 1 olarak alır
        self.yarıcap=yarıcap
    
    # methods
    def cevrehesapla(self): # self yerıne farklı farklı kelımeler de eklenebılır bu sefer ekledıgımız kelıme ıle cagırırız.
        return 2*self.pi*self.yarıcap
    
    def alanhesapla(self): # selfi kullanmamızın nedenı bulundugumuz class'a aıt oldugunu belırtmek 
        return self.pi*self.yarıcap**2


c1=Cırcle() # yarıcap=1 oldugu durum , cırcle=daıre
c2=Cırcle(5)
print(c1.cevrehesapla()) # normalde bı method kullanırken parametresı varsa cevrehesaplanın parantezıne yazmamız gerekır
# ama buradakı self bı parametre degıl sadece bır ait'lik.
print(f'c1 => alan:{c1.alanhesapla()}, cevre:{c1.cevrehesapla()}')
print(f'c2 => alan:{c2.alanhesapla()}, cevre:{c2.cevrehesapla()}')

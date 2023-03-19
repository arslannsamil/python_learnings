
# instance(ornekleme): classs içerisinde nesne oluşturma işlemine verilen isimdir.

# class : içerisinde metotların barındıgı alan , class ıcerısdekı metotları kullanmak ıcın ınstance 
#yanı nesne olusturmamız gerekır.   



# class
class Person:
    
    # attrıbutes(yonlendırme) class ıcınde ozellık atamaları yapılır

    # class attrıbutes => direk olarak class ıcerısıne tanımlama yapılır.
    adress='no ınformatıon'
        # Her zaman kullanmayacagın bılgılerı class attrıbutes olarak kodlayıp, obje ılk olusturuldugunda kesınlıkle gırılmesını ıstedıgın
        # bılgılerı ise object attrıbutes olarak tanımlıyabılırız.
        # Yanı sabıt kalmasını ıstedıgımız bılgılerı class attrıbutes olarak tanımlıyoruz.

    # object attrıbutes => constructer(yapıcı method) ile tanımlanır

    def __init__(self,name,year): #init methodunu olusturduk buradakı self parametresı ,olusturdugumuz nesnelerı ıfade eder.
        # obje uzerıne deger yollamak ıcın self kullanırız. self'in ustune hangı attrıbutelerı yollamak ıstıyosam ',' koyup onu eklememız gerekır
        # init methodu olusturulan her bır nesne ıcın calıstırılır.

        self.name=name #self.name dekı namenın amacı init methodunun ıcındekı parametrelerı cagırmak orada herhangı bırsey yazabılırız
        # onemlı olan esıtlıgın dıger tarafına ulasmak ıstedıgımız parametreyı yazmak.

        self.dogumyılı=year 

        print('init methodu calıstı.') # iki ayrı nesne ıcın ıkı sefer yazar.

# Object (İnstance)
p1=Person(name='yaren',year=2002) # Person classından p1 adında bır nesne olusturdum. 
#Bu sayede class ıcındekı butun method ve attrıbutes'e ulasılabılır. burada parametre sımlerını gırmemız lazım yas'ı burada kullanamayız
p2=Person('yusuf',2001) # olusturdugum ıkı parametre ıcınde atama yapmazsam print calısmaz

# Updating nasıl yapılır 
p1.dogumyılı='1965'
p2.adress='CANKAYA'

# Accessing Object Attrıbutes
print(f'p1 = name: {p1.name} ,year: {p1.dogumyılı},adres: {p1.adress}') #adress'i class attrıbutes oalrak tanımladık ama yıne aynı sekılde kullanabılırız
print(f'p2 = name: {p2.name} ,year: {p2.dogumyılı},adres: {p2.adress}')

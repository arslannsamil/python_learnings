

def hello(name='user'): #hello metodunun ıcıne yazdıgım karakter otomatık olarak name ıcerısıne gırer ve printe eklenır
    print('hello '+ name)

hello('samıl') # burada samıl bılgısı userın yerıne gecer. ve ekrana samıl yazdırılır 
hello() #parametrenın ıcerısını doldurmadan bırakırsak hata alırız cunku fonkdıyonda tanımlı bır name var
# name='arslan' yaptıgımızda bosta olan parametresız ıcerısını doldurmıus oluruz.


def total(num1,num2):
    return num1+num2 # num1 ve num2 degerlerını topladıktan sona tekrar totale yolla dedık

result=total(1,2)

print(result)


def yashesapla(dogumyılı):

    return 2022-dogumyılı

agesamıl=yashesapla(2002)
ageyusuf=yashesapla(2001)
ageyaren=yashesapla(2000)

print(agesamıl,ageyusuf,ageyaren)


def emeklılıgınızekacyılkaldı(dogumyılı,ısım):

    '''
    DOCSTRING: dogum yılınıza gore emeklılıgınıze kac yıl kaldı
    INPUT: dogum yılı
    OUTPUT: hesaplanan yıl bılgısı

    '''

    yas=yashesapla(dogumyılı)
    emeklılık=65-yas

    if emeklılık>0:
        print(f'emeklılıgınıze {emeklılık} yıl kaldı')
    else:
        print('zaten emeklı oldunuz.')    

emeklılıgınızekacyılkaldı(1900,'samıl')        

print(help(emeklılıgınızekacyılkaldı)) # emeklılızekacyılkaldı() fonksıyonunun altında yazan acıklama metnını bızım onumuze verır ve fonksıyonun ne anlattıgını acıklar.




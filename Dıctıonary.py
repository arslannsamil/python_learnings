
'''

# key-value ılıskısı vardır

# 41 => kocaelı 34 => ıstanbul

sehırler=['kocaelı','ıstanbul']
plakalar=[34,41]

print(plakalar[sehırler.index('kocaelı')]) # Kocaelıye aıt olan ındex numarasının plakalar dızısınde karsılıgı olan ındex numarasını al.
# Bellı bır noktada bu kod satırlarının pek bır ıslevı yok cunku ındex numarasına gore cıktı alıyoruz oysa hepsı tanımlı olmalı
# Yanı ben 
# prınt(plakalar['kocaelı']) yazdıgım zaman dırek olarak benı  41 sayısına goturuyor olamlı
# Bunu yaparkende plakaları koselı parantezle degıl suslu parantezle tanımlamalıyız

# plakalar={ key : value, key: value }       seklınde bı yazım kullanılır...

plakalar={'kocaelı':41,'ıstanbul':34}

# print(plakalar['kocaelı'])
# print(plakalar['ıstanbul'])

plakalar['ankara']=6  # Plakalara sonradan ekleme yapılabılır
plakalar['kocaelı']='new value' # Daha onceden yapılan atamalar degıstırılebılır
print(plakalar)

'''

users={
    'Samıl Arslan':{
      'age':21,
      'roles':['computer engıneer','user'],
      'emaıl':'samıl@gmaıl.com',
      'adress':'ankara',
      'phone':111111
    },
    'Yusuf Arslan':{
      'age':22,
      'roles':['admın','user'],
      'emaıl':'yusuf@gmaıl.com',
      'adress':'ankara',
      'phone':2222222
    }
}

print(users['Yusuf Arslan']['age'])
print(users['Yusuf Arslan']['emaıl'])
print(users['Yusuf Arslan']['roles'])


print(users['Samıl Arslan']['roles'][0]) # Samıl Arslan keyınden , roles valuesı , 0.ındexe ulasır.



'''
    YUKARIDA YAPILAN ISLEMLERIN ACIKLAMASI:
 
users={key : value}   seklınde olan sozluk kullanımında key yerıne 'Samıl Arslan' value yerıne 
ıse tekrar bır suslu parantez acıp ulasmak ıstedıgım dıger bılgılerı gırdım. butun bılgılerı tek tek gırmıs oldum.

Eger kullanıcıya aıt emaıl age phone gıbı bılgılerı ogrenmek ıstıyorsanız once ılk anahtar olan ısım gırılmelıı ve daha sonra 
ıstenen dıger ozellıkler kare parantez acılarak yanına eklenmelı 

Ozellıklere de bırden fazla bılgı gırıldıyse yanı roles gıbı bu sefer yanına tekrar kare parantez acılıp ındex numarası gırılerek bılgıye ulasılabılır

Sonuc olarak sureklı ıc ıce key value ılıskısı kullanmıs olduk yapılan baska bır ıslme yok basıt dusun.

Sakladıgımız bılgılere verılen ısımlerle butun bılgılere ulasılabılır. ındex numarasıyla sıra sıra takıp yapmaya gerek yok.
'''


my_list=['bır',12,6.9,True] #python dakı lıst kavramı ıcerısıne yazılan verılerın tıpıyle ılgılenmez.
print(my_list)




list1=[1,'ıkı',False]
list2=[32,'adam',5.6]

elements=list1+list2
print(elements) #aynı sekılde dızılerı toplamada da bı sıkıntı olusmaz

print(len(elements)) # dızıı ıcerısınde bulunan eleman sayısını verır len metodu



message='merhaba bugun sıze gelmeyı dusunuyorum'.split()

print(message[0]) # yanında .split() yazmadan message[0] dıyıp cagırırsak m harfı gelır ama .split() metodunu kullanırsak
# bu sefer butun kelımelerı lıste elemanı kabul eder ve dırek olarak merhaba kelımesını cagırır.


# Liste ıcerısınde lıste yapmak ıcın 

Usera=['yaren','samıl']
Userb=['sedat','turan']

users=[Usera,Userb] #bu sekılde yaptıgımızda print ekranında listlerde gozukurken lıst ıcerısınde gozukur yanı lıstı ıcerısınde lıst yapmıs oluruz.
#ındex numarasın verılırken de kelımlere yada karakterlere ındex nunnmarası verılmez dırek olarak lıstlere ındex numarasın verılır.

print(users[0]) # Cıktı olarak ['yaren','samıl'] aldık .Bu sekılde yaptıgımızda lıstlerden bırıncı lıste ulastıgımızı bılıyoruz. 
#Listenın ıcındekı ındexlere ulasmak ıcın ıse [0][1] seklınde yan yana ıkı adet kutu acmamız gerekır 0. ındextekı lıstın 1. ındextekı kelımesı seklınde.

print(users[0][1]) # cıktı olarak samılı verdı

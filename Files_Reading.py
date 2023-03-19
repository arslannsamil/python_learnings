


from cgi import print_environ
from importlib.metadata import files


# file=open("newfile.txt","r",encoding='utf-8')  


# okuma ıslemı bırden fazla yontem ıle gerceklestırılebılır.


# ********** for dongusu ıle okuma

# for i in file:
#     print(i, end="") #end="" yaptıgımız zaman cıktı ekranında olusan satırlar arası bosluk ortadan kalkar.




# ********** read() fonksıyonu

# content1=file.read()

# print('ıcerık 1')
# print(content1)



# file=open("newfile.txt","r",encoding='utf-8')  #eger dosyayı tekrar yazmassak ıcerık 1'i okumaz

# content2=file.read()

# print('ıcerık 1')
# print(content2)


# karakter karakter okumak ıstersek de

# content=file.read(5)
# content=file.read(3)
# content=file.read(3) # parca parca once 5 sonra 3, 3 olmak uzere karakterlerı yazdırır ama aynı anda yazdırmaz sonda ne varsa o yazılır.

# print(content)




#********** readlıne() fonksıyonu ile okuma => satır , satır okuma yapmamıza olanak saglar  
 
# print(file.readline(),end="")  # sadece ilk satırı okur
# print(file.readline(),end="")  # ilk satır okundugu icin ikinci satırdan okumaya devam eder. ama aralarda bosluk bırakır bu print fonk. yuzundendır
# # bunu engellemek ıcın readlıne sonuna , end="" yazmamız gerekır
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# eger yazacak satır bıttıgı okuma yapmaya devam edıyor olursak bu sefer bos satır gırmeye baslar.




#********** readlınes() fonksıyonu ile okuma 


# liste=file.readlines()

# print(liste) # cıktı ekranında lıste olarak verır bu da bızım ındex numarası ıle rahat bır sekılde elemanlara ulasmamızı saglar.
# print(liste[0],end="")  # aynı bosluk olayı bunda da gecerlı 
# print(liste[1]) # index numarasında gore alt alta yazdırır
# print(liste[2]) 


# file.close()


#************************************************

# DOSYA OKUMA FONSIKYONLARI

# liste=open("newfile.txt","r",encoding='utf-8')  

# content=liste.read()

# print(content) 

# liste.close()

# # dosya kapama ıslemını yapmamıza gerek kalmayacak bı fonksiyon islemı olusturacagız


     
with open("newfile.txt","r",encoding='utf-8') as file : # kod bulogu oldugu ıcın file.close yapmamıza gerek yok wıth dısına cıkınca bıtecek
    # file.read() seklınde okutmak ıcın ıse dosyayı as file olarak baglıyoruz

    content =file.read(20) #10 karakter okumasını soyledık
    
    print(content)

    file.seek(5) #imlecın nereye gıdecegını soylerız bu sayede normalde okunmayacak olan content2'yı okutabılırız.

    print(file.tell()) #tell fonksıyonu bıze ımlecın kaldıgı yerı gosterır

    content2=file.read(10) # 10 karakter okumasını soyledık

    print(content2) # okudugu 10 karakterı yazdı.











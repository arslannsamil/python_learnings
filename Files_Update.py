

'''
with open("newfile.txt","r+",encoding='utf-8') as file : # r+ modu dosyaya hem yazar hemde okur "w" dan farkı
    # yazarken dosyanın ıcındekılerı sılmez
    file.seek(1) # 1. karakterden sonra yazmaya baslar yazılı olanın ustune yazama gıbı bır olay da var. bu fonksıyon bıze ıstedıgımız 
    #yerde guncelleme yapmamıza olanak saglar
    file.write('deneme')


with open("newfile.txt","r+",encoding='utf-8') as file :
    print(file.read()) 

'''

#*********** Sayfanın Sonunda GUuncelleme ıslemı Nasıl Yapılır ***********

'''
with open("newfile.txt","a",encoding='utf-8') as file : # sayfa sonunda ıslem yapacagımız ıcın append methodunu kullnabılırız.
    print(file.write("\n yarenn karatas")) 

    
with open("newfile.txt","r",encoding='utf-8') as file :
    print(file.read()) 

'''

#*********** Sayfanın Basında Guncelleme Islemı Nasıl Yapılır ***********

'''
with open("newfile.txt","r+",encoding='utf-8') as file : 
   content=file.read()

   content="yusuf asım arslan\n"+content
   file.seek(0)
   file.write(content)

    
with open("newfile.txt","r",encoding='utf-8') as file :
    print(file.read())

'''

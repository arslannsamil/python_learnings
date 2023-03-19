

# Dosya acmak ve olusturmak ıcın open() fonksıyonu kullanılır.

# Kullanımı open(dosya_adı,dosya_erısım_modu)

# (dosya_erısım_modu) =>dosyayı hangı amacla actıgımızı belırtır



# "w": (write) yazma modu. Dosyayı konumda olusturur. Dosya ıcerıgını sıler ve yenıden ekleme yapar

# file=open("newfile.txt","w",encoding='utf-8')  # encoding='utf' turkce karakterlerın kullanılmasını saglar.
# file.write("arslanahmetsamıl") # kodu her calıstırdıgımızda yazılı olanı sıler ve tekrar yazar
# file.close() # dosyanın kaynakları tuketmemesı ıcın kapatmamız lazım.



# "a": (append) ekleme modu. Dosya konumda yoksa olusturur.Dosyaının ıcındekılere ellemeden ekleme yapar

# file=open("newfile.txt","a",encoding='utf-8')  # her calıstırdıgımızda kodun ustune tekrar ekleme yapar ve calıstırır yazılı olanı sılmez
# ekleme yaparken sondan eklemeye baslar.
# file.write("\n duranayla")
# file.close() 


# "x": (creat) olusturma modu. Dosya zaten varsa hata verır.

# file=open("newfile1.txt","x",encoding='utf-8')  # dosya olustur ve dosyayı olusturmusken tekrar calıstırırsak existerror(var-mevcut hatası verır)
# file.write("\n arslanahmetsamıl")
# file.close() 




# "r": (read) okuma modu. Varsayılan dosya konumda yoksa hata verır.

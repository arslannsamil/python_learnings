'''
bılmedıgım operatorler

// kalansız bolme ıslmeı yapar bolmede vırgulden sonra kalanı gostermez
** ussu anlamına gelır 2**3 = 2*2*2 demektır

and = ıkı durumunda dogru oldugu durumada true verır
or = ıkı durumdan bırının dogru oldugu durumda dogruyu verır
not = ters anlamında kullanılır yanlıs demez dogru degıldırder

'''

# İndenty operator: is




x=y=[1,2,3]

z=[1,2,3]

print(x==y) #true burada lıstlerının aynı olup olmadıgına baktık

print(x==z) #true 

print(x is y) #true  burada dogru olmasaının nedenı ıkısının de adresının aynı olması

print(x is z) #false adreslerı,referencelerı yanı nesnelerı bırbırınden farklı

# Membershıp operator: in

x=['apple','banana']
print('banana'in x) # banana x ın ıcınde var mı = true



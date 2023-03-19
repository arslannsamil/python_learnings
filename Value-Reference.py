


# Value Types = verının kendısıyle ılgılenır

x=5
y=25

x=y # y dekı degerı x'e atar

y=10 # bu y degerı x'ı etkılemez.

print(x,y)





# Reference Types = List ,  listenın adresıyle ılgılenır 

a=['apple','banana']
b=['apple','banana']

a=b # normalde value type uzerınde bu ıslemı yapsak sadece sonucları bırbırıne esıtlerdı
# ama reference type da bu durum boyle degıl cunku bız lıstelerı bırbırıne esıtledıgımız zaman adreslerı de esıtlemıs oluruz
# ve bu andan sonra yapacagımız butun ıslemler ıkısı ıcınde gecerlı olur bu ıslem webde bılgılerı ıkı sefer kopyalamamızı engellemekte ıse yarar.ıkı sefer kaydetmemızı
# engeller

b[0]='grape'

print(a,b)



import ssl
import smtplib

kullanici='arslanahmetsamil@gmail.com'
sifre='+Aa143380'

alici=kullanici

baslik='python gonderisi'
baslik.upper

mesaj='deneme mesaji'

context=ssl.create_default_context  ()

port=456
host='smpt@gmail.com'

epost_sunucusu=smtplib.SMTP_SSL(host=host,port=port,context=context)
epost_sunucusu.login(kullanici,sifre)
epost_sunucusu.sendmail(kullanici,alici,mesaj)

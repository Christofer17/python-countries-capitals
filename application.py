"""This code is for list of countries and capitals"""
import os
import sys

ALL = {}
COUNTRY = []
CAPITAL = []


def question():
    """ask the user if you want to enter another country"""
    var3 = raw_input("Do you want to enter another COUNTRY? y/n: ")
    var3 = var3.lower()
    if var3 == "y":
        insert_country()
    elif var3 == "n":
        menu()
    else:
        print "This is not vALLid"
        limpiar()
        question()

def insert_country():
    """Asks the user to enter a country"""
    limpiar()
    var1 = raw_input("Enter the COUNTRY: ")
    COUNTRY.append(var1)
    var2 = raw_input("Enter the CAPITAL: ")
    CAPITAL.append(var2)
    ALL[var1] = var2
    question()
    menu()


def country_list():
    """Displays the list of countries"""
    limpiar()
    for i in COUNTRY:
        print i
    raw_input("Press enter")
    limpiar()
    menu()

def capital_list():
    """Display the list of capitals"""
    for i in CAPITAL:
        print i
    raw_input("Press enter")
    limpiar()
    menu()

def view_all():
    """Shows all"""
    for i in ALL:
        print i, ALL[i]
    raw_input("presione enter ")

def limpiar():
    """clear"""
    os.system("reset")

def salir():
    """exit the program"""
    sys.exit()

def menu():
    """Print menu"""
    limpiar()
    print "\t\t\t****Countries and CAPITALs****\n"
    print "*~~~What do you want to do?~~~*"
    print "1. Insert your COUNTRY"
    print "2. Countrie List"
    print "3. CAPITAL List"
    print "4. view ALLl"
    print "5. Exit/Quit\n"
    menu1 = raw_input("Insert your option: ")

    if menu1 == "1":
        insert_country()
    elif menu1 == "2":
        country_list()
    elif menu1 == "3":
        capital_list()

    elif menu1 == "5":
        salir()
    elif menu1 == "4":
        view_all()
    else:
        print "You have not entered anything"
menu()


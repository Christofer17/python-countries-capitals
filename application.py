import os
import sys

al = {}
Country = []
Capital = []


def question():
    var3=raw_input("Do you want to enter another country? y/n: " )
    var3=var3.lower()
    if var3 == "y":
        Insert_Country()
    elif var3== "n":
        menu()
    else:
        print "This is not valid"
        limpiar()
        question()

def Insert_Country():
    limpiar()
    var1 =raw_input("Enter the Country: ")
    Country.append(var1)
    var2 =raw_input("Enter the Capital: ")
    Capital.append(var2)
    
    al[var1]=var2
    question()    
    menu()


def Country_List():
    limpiar()
    for i in Country:
        print i 
    raw_input("Press enter")
    limpiar()
    menu()

def Capital_List():
    for i in Capital:
        print i 
    raw_input("Press enter")
    limpiar()
    menu()

def view_all():
    for i in al:
        print i, al[i]
    raw_input("presione enter ")


def limpiar():
    os.system("reset")


def salir():
    sys.exit()
    

def menu():
    limpiar()
    print "\t\t\t****Countries and Capitals****\n"
    print "*~~~What do you want to do?~~~*"
    print "1. Insert your Country"
    print "2. Countrie List"
    print "3. Capital List"
    print "4. view All"
    print "5. Exit/Quit\n"
    menu = raw_input("Insert your option: ")

    if menu == "1":
        Insert_Country()
    elif menu == "2":
        Country_List()
    elif menu == "3":
        Capital_List()
    
    elif menu == "5":
        salir()
    elif menu=="4":
        view_all()
    else:
        print "You have not entered anything"
menu()
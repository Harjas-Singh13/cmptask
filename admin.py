from stdiomask import getpass
import hashlib
import os
from menu import  * 
from user import *
from user import User, UserManager
from weather import *
clear = lambda: os.system('cls')

def main():
    clear()
    print("MAIN MENU")
    print("---------")
    print()
    print("1 - Admin Login")
    print()
    while True:
        print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        admin()
    else:
        print("You have to be Admin to access this")
    pass

def admin():
    database={'admin': 'admin@123'}
    name = input('Enter Admin ID : ')
    ask = getpass('Enter Admin Password: ')
    if ask in database[name]:
        opt = """
        ***************WELCOME Admin***************
        OPTION 1 : User Management 
        OPTION 2 : Weather Forecast
        *******************************************
        """
        print(opt)
        while True :
            choice = input("Enter Admin Option : ")
            if choice == '1':
                user_menu(UserManager)
                
                
            elif choice == '2':     
                pass
            
    else:
        print ('Wrong Credentials')
        
main()
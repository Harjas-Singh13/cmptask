from stdiomask import getpass
import hashlib
import os
clear = lambda: os.system('cls')

def main():
    clear()
    print("MAIN MENU")
    print("---------")
    print()
    print("1 - Admin Login")
    # print("2 - User Login")
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
                print("User Management System: ")
            elif choice == '2':
                print("Weather Forecast System")
            break
    else:
        print ('Wrong Credentials')
        
main()
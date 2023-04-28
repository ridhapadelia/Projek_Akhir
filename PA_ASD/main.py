from Model.Model_User import connect, create_account, user_login
from Model.Model_Admin import connect, admin_login 
import os
os.system('cls')

mydb = connect()
while True :
        print("=====================================================================")
        print("|        Selamat Datang Di Aplikasi Sederhana Bs-Startion            |")
        print("=====================================================================")
        print("| 1. Registrasi                                                     |")
        print("| 2. Login User                                                     |")
        print("| 3. Login Admin                                                    |")
        print("| 4. Baca Ketentuan Aplikasi                                        |")
        print("| 5. Exit                                                           |")
        print("=====================================================================")
        print("")
        tampilan = input("Silakan Ingin Melakukan Apa.... : ")
        if tampilan == "1" :
            create_account()
            print("")
        elif tampilan == "2" :
            user_login()
            print("")
        elif tampilan == "3":
            admin_login()
            print("")
        elif tampilan == "4":
            print("")
        elif tampilan == "5" :
            exit()





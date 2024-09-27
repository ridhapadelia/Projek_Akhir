from Model.Model_User import connect, create_account, user_login
from Model.Model_Admin import connect, admin_login 
import os
os.system('cls')

mydb = connect()

while True :
        print("=====================================================================")
        print("|        Selamat Datang Di Aplikasi Sederhana Bs-Startion           |")
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
            os.system('cls')
            create_account()
            print("")
        elif tampilan == "2" :
            os.system('cls')
            user_login()
            print("")
        elif tampilan == "3":
            os.system('cls')
            admin_login()
            print("")
        elif tampilan == "4":
            os.system('cls')
            print("")
            print("""                            Selamat Datang di Aplikasi sederhana Bs-station


1. Lakukan Registrasi terlebih dahulu jika anda adalah User, tetapi tidak memiliki akun terdaftar
2. Jika telah berhasil melakukan Registrasi maka user akan langsung di arahkan ke menu user
3. Pada menu User, ketika user ingin memutar anime, maka harus memasukan daftar anime yang tersedia ke playlist
4. Ketika user melakukan penambahan anime ke playlist maka akan di berikan pilihan berapa ingin menambahkan episode ke playlist nya
5. Dalam menu user, pemutaran playlist ini hanya dapat memutar anime serta episode yang telah di tambahkan sebelumnya
6. Pada menu pemutaran, user juga dapat mencari anime yang akan di putarnya
7. tetapi user tidak dapat memilih episode apa yang akan dia putar, jadi setiap pemutaran akan diputar dari episode satu
8. tersedia tombol next episode untuk melangkahi episode nya, dengan cara menekan tombol (x)
9. tersedia juga tombol stop untuk keluar dari pemutaran, dengan cara menekan tombol (z)
10. Dan jika user telah selesai menonton anime yang tersedia di playlist, maka user dapat menghapusnya. 
11. DImohon untuk memperhatikan pengetikan, dikarenakan ini aplikasi sederhana jika mengetikan diluar dari ketentuan maka program akan terhenti!
            """)

        elif tampilan == "5" :
            exit()





from View.View_User import tampilan12
import mysql.connector 
import pwinput
import os


# Koneksi ke database
def connect():
    mydb = None
    try:
        mydb = mysql.connector.connect(
        host="db4free.net",
        user="selaputri2109",
        password="sela1234567890",
        database="kelompok2_asd"
        )
        print("database connection berhasil")
    except mysql.connector.Error as e:
        print(f"error: {e}")
    return mydb

# Fungsi login user
def user_login():
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")
    query = "SELECT * FROM user WHERE username = %s AND password = %s"
    values = (username, password)
    cursor = mydb.cursor()
    cursor.execute(query, values)
    user = cursor.fetchone()
    if user:
        os.system('cls')
        print("Login berhasil. Selamat datang, {}!".format(user[0]))
        tampilan12()
    else:
        os.system('cls')
        print("Login gagal. Silakan coba lagi.")
        k = input("Apa Apakah Ingin Mengulang? Y/N : ")
        if k == "Y":
            user_login()
        elif k == "N":
            exit()

def create_account():
        cursor = mydb.cursor()
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        insert_query = "INSERT INTO user (username, password) VALUES (%s, %s)"
        account_data = (username,password)
        cursor.execute(insert_query, account_data)
        mydb.commit()
        print(f"Akun {username} berhasil dibuat!")
        cursor.close()
        user_login()

mydb = connect()

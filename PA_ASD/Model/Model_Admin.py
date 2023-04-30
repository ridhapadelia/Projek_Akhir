from View.View_Admin import tampiladmin
import mysql.connector
import pwinput
import os
os.system('cls')

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

def admin_login():
    username = input("Masukkan username admin: ")
    password = pwinput.pwinput("Masukkan password admin: ")
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    values = (username, password)
    cursor = mydb.cursor()
    cursor.execute(query, values)
    admin = cursor.fetchone()
    if admin:
        os.system('cls')
        print("Login berhasil. Selamat datang, {}!".format(admin[0]))
        tampiladmin()
    else:
        os.system('cls')
        k = input("Login gagal Apa Apakah Ingin Mengulang? Y/N : ")
        if k == "Y":
            os.system('cls')
            admin_login()
        elif k == "N":
            exit()
mydb = connect()


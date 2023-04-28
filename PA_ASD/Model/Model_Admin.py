from View.View_Admin import tampilanAdmin
import mysql.connector
import pwinput

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
        print("Login berhasil. Selamat datang, {}!".format(admin[0]))
        tampilanAdmin()
    else:
        print("Login gagal. Silakan coba lagi.")
        k = input("Apa Apakah Ingin Mengulang? Y/N : ")
        if k == "Y":
            admin_login()
        elif k == "N":
            exit()

mydb = connect()


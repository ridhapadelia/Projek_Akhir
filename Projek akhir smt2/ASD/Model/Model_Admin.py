import mysql.connector 
import pwinput

# Koneksi ke database
def connect():
    mydb = None
    try:
        mydb = mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12609736",
        password="kfnkS8CUJk",
        database="sql12609736"
        )
        print("database connection berhasil")
    except mysql.connector.Error as e:
        print(f"error: {e}")
    return mydb

def admin_login():
    username = input("Masukkan username admin: ")
    password = pwinput.pwinput("Masukkan password admin: ")

    # Query untuk memeriksa keberadaan username dan password di tabel admin
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    values = (username, password)

    cursor = mydb.cursor()
    cursor.execute(query, values)

    admin = cursor.fetchone()

    # Jika ditemukan admin dengan username dan password yang sesuai
    if admin:
        print("Login berhasil. Selamat datang, {}!".format(admin[0]))
    else:
        print("Login gagal. Silakan coba lagi.")

mydb = connect()

while True:
    print("Selamat datang di program login.")
    print("Pilih opsi:")
    print("1. Login user")
    print("2. Login admin")
    print("3. Registrasi")
    print("4. Keluar")

    choice = input("Masukkan pilihan: ")

    if choice == "1":
        # user_login()
        print("")
    elif choice == "2":
        admin_login()
    elif choice == "3":
        print("")
        # create_account(mydb)
    elif choice == "4":
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
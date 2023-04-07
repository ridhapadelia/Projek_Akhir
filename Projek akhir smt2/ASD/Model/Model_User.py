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

# Fungsi login user
def user_login():
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")

    # Query untuk memeriksa keberadaan username dan password di tabel user
    query = "SELECT * FROM user WHERE username = %s AND password = %s"
    values = (username, password)

    cursor = mydb.cursor()
    cursor.execute(query, values)

    user = cursor.fetchone()

    # Jika ditemukan user dengan username dan password yang sesuai
    if user:
        print("Login berhasil. Selamat datang, {}!".format(user[0]))
    else:
        print("Login gagal. Silakan coba lagi.")

def create_account(mydb):
        cursor = mydb.cursor()
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        insert_query = "INSERT INTO user (username, password) VALUES (%s, %s)"
        account_data = (username,password)
        cursor.execute(insert_query, account_data)
        mydb.commit()
        print(f"Akun {username} berhasil dibuat!")
        cursor.close()

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
        user_login()
    elif choice == "2":
        # admin_login()
        print("")
    elif choice == "3":
        create_account(mydb)
    elif choice == "4":
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
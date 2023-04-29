# PROJECT AKHIR ALGORITMA DAN STRUKTUR DATA
# Program BStation
## Deskripsi program 
Program BStation yang kami buat ini merupakan sebuah program yang pastinya sangat digemari oleh para pecinta anime, karena program ini menyediakan berbagai tontonan anime berkualitas dan terbaik, program ini juga sangat mudah digunakan. Pada program ini juga kami rancang agar bisa update anime terbaru yang pastinya dinantikan oleh para penggemar dan akan ditambahkan ke dalam daftar anime yang tersedia.
## Struktur Program
Pada program ini komponen awal pada struktur programnya adalah menu login yang diberfungsi untuk langkah awal sebelum masuk ke dalam inti program. Setelah itu, salah satu komponen utama dalam program ini adalah menu admin dan menu user pada komponen inilah operasi-operasi akan dipilih untuk dijalankan. Lalu komponen utama selanjutnya adalah penggunaan struktur data Linked List yang digunakan untuk menyimpan data video dan audio dari program. Ada juga komponen pembantu yang berfungsi membantu jalannya beberapa operasi yang ada di program seperti penggunaan algoritma Jump Search dan Shell Sort.
## Fitur dan fungsionalitas
### Tampilan Awal Program
Pada tampilan awal program terdapat 5 pilihan yaitu:
1. Registrasi: Apabila belum memiliki username dan password, dapat melakukan registrasi terlebih dahulu.
2. Login user: Digunakan oleh user yang sudah registrasi terlebih dahulu (memiliki username dan password yang tersimpan di database). 
3. Login admin: Digunakan oleh admin (memiliki username dan password yang tersimpan di database).
4. Baca Ketentuan Aplikasi: menampilkan ketentuan/peraturan yang ada pada program yang kami buat.
5. Exit: Keluar dari program.
### Menu User
Pada menu user memiliki 4 fitur yang tersedia dan dapat digunakan yaitu:
1. Tambahkan Anime baru ke Playlist: User dapat menambahkan anime baru yang di sukai ke dalam playlistnya.
2. Hapus Anime yang ada di Playlist: User dapat menghapus anime yang ada pada playlistnya. 
3. Putar Playlist: User dapat menonton/memutar video dari anime yang telah dipilih untuk diputar dan program akan menampilkan video anime tersebut.
4. Keluar: Jika user ingin mengakhiri menggunakan program, user dapat memilih keluar, untuk keluar dari program.
### Menu Admin
Pada menu admin memiliki 5 fitur yang dapat digunakan yaitu:
1. Tambahkan Anime baru: Jika ada anime baru yang dirilis, maka admin dapat menambahkan anime tersebut ke dalam daftar anime yang tersedia pada program. 
2. Hapus Anime yang ada: Admin dapat menghapus anime yang ada dalam daftar anime yang tersedia pada program.
3. Tambahkan Episode: Admin dapat menambahkan episode baru yang tersedia pada daftar anime.
4. Melihat anime dan episode yang ada: Admin dapat mengecek anime dan episode apa saja yang sudah tersedia dalam daftar, sehingga dapat memudahkan ketika nantinya admin akan mengupdate anime baru dan episode baru ke dalam daftar anime yang tersedia pada program.
5. Masuk ke menu USER: Admin memiliki akses untuk masuk ke menu user.
6. Keluar: Jika admin sudah menyelesaikan semua pekerjaannya dan ingin mengakhiri menggunakan program, admin dapat memilih opsi 6 untuk keluar dari program.
### Cara penggunaan 
Ketika memulai program, maka akan menampilkan tampilan awal program yaitu:
1. Registrasi
2. Login User
3. Login Admin
4. Baca Ketentuan Aplikasi
5. Exit

Bagi user, untuk dapat login pastikan telah memiliki username dan password yang tersimpan di database (telah melakukan registrasi) namun apabila belum memiliki  username dan password dapat memilih opsi 1 yaitu “Registrasi” karena jika belum melakukan registrasi, maka program tidak dapat dijalankan. Ketika melakukan registrasi, maka akan diminta untuk membuat username dan password baru, masukkan username dan password yang dapat mudah diingat. Setelah selesai melakukan registrasi, akan langsung mengarah ke login user. User akan diminta untuk memasukkan username dan password yang telah dibuat tadi, pastikan username dan password yang dimasukkan sudah sesuai. Jika username dan password benar (login berhasil), maka otomatis program dapat dijalankan dan jika salah (login gagal) maka tidak bisa melanjutkan program dan akan ada pilihan "Apakah Anda Ingin Mengulang? Y/N jika anda mengetik Y maka akan diminta kembali untuk memasukkan username dan password yang sesuai dan jika mengetik N maka program akan selesai.

Sedangkan bagi admin, username dan password yang dimasukkan untuk login telah ditentukan yaitu:
Username = kelompok2 
Password = kelompok2_asd
Jika admin memasukkan username dan password selain ini, maka otomatis akan gagal login.
### Login User
Apabila memilih opsi 2 yaitu login user, akan diminta untuk memasukkan username dan password yang telah terdaftar (sudah registrasi).
Jika login sebagai user, maka akan menampilkan 4 pilihan yang hanya dapat digunakan oleh user yaitu:
1.	Tambahkan Anime baru ke Playlist: Apabila user memilih opsi 1, User dapat menambahkan anime baru yang di sukai ke dalam playlistnya dengan memasukkan judul anime tersebut (pastikan judul yang dimasukkan adalah yang terdapat pada daftar anime yang tersedia).
2.	Hapus Anime yang ada di Playlist: Apabila user memilih opsi 2, User dapat menghapus anime yang ada pada playlistnya. Dengan cara memasukkan judul anime yang ada dalam playlist (pastikan penulisan huruf kapital dan huruf kecil sudah sesuai).
3.	Putar Playlist: Pada bagian ini terdapat 2 opsi lagi yaitu:
- Cari Anime yang ingin diputar: user akan diminta untuk memasukkan judul anime yang akan diputar. Setelah memasukkan judul yang sesuai dari playlistnya, maka akan langsung memutar video anime yang dipilih tersebut.
- Kembali: kembali ke menu user.
4.	Keluar: Opsi  4 ini digunakan jika user ingin mengakhiri program.
### Login Admin
Apabila memilih opsi 3 yaitu login admin, akan diminta untuk memasukkan username dan password admin yang telah ditentukan. jika tidak sesuai maka login akan gagal.
Jika login sebagai admin, maka akan menampilkan 6 pilihan yang hanya dapat digunakan oleh admin yaitu:
1. Tambahkan Anime baru: Apabila admin memilih opsi 1, Admin dapat menambahkan anime baru yang ke dalam daftar anime yang tersedia dengan cara memasukkan judul anime baru yang akan ditambahkan, serta 5 file episode yang telah di siapkan terlebih dahulu.
2. Hapus Anime yang ada: Apabila admin memilih opsi 2, admin dapat menghapus anime dari daftar anime yang tersedia, caranya yaitu dengan memasukkan judul anime yang akan dihapus, pastikan judul yang dimasukkan sesuai dengan yang ada pada daftar anime yang tersedia, perhatikan juga penggunaan huruf kapitalnya.
3. Tambahkan Episode: Apabila admin memilih opsi 3, dapat digunakan admin untuk menambahkan episode baru ke dalam daftar anime yang tersedia.
4. Melihat Anime dan episode yang ada: Apabila admin memilih opsi 4, pada bagian ini dapat digunakan admin untuk mengecek daftar anime dan episode yang tersedia pada program. Agar lebih mudah dan cepat disini admin dapat melihat daftar anime berdasarkan urutan abjad dari judul anime yang ada.
5. Masuk ke menu USER : Apabila admin memilih opsi 5 maka admin akan langsung di arahkan ke menu user.
6. Keluar: Opsi 6 ini digunakan jika admin ingin mengakhiri menggunakan program.

Jika memilih opsi 4 pada bagian tampilan awal yaitu baca ketentuan aplikasi akan menampilkan beberapa ketentuan/peraturan yang kami buat pada program ini dan jika memilih opsi 5 yaitu exit dapat digunakan untuk keluar dari program/menyudahi menggunakan program.  

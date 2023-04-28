# PROJECT AKHIR ALGORITMA DAN STRUKTUR DATA
# Program BStation
## Deskripsi program 
Program BStation yang kami buat ini merupakan sebuah program yang pastinya sangat digemari oleh para pecinta anime, karena program ini menyediakan berbagai tontonan anime berkualitas dan terbaik dengan kualitas video HD, program ini juga sangat mudah digunakan. Pada program ini juga kami rancang agar bisa update episode terbaru dan anime terbaru yang pastinya dinantikan oleh para penggemar dan akan ditambahkan ke dalam daftar anime yang tersedia.
## Struktur Program
Pada program ini komponen awal pada struktur programnya adalah menu login yang diberfungsi untuk langkah awal sebelum masuk ke dalam inti program. Setelah itu, salah satu komponen utama dalam program ini adalah menu admin dan menu user pada komponen inilah operasi-operasi akan dipilih untuk dijalankan. Lalu komponen utama selanjutnya adalah penggunaan struktur data Linked List yang digunakan untuk menyimpan data video dan audio dari program. Ada juga komponen pembantu yang berfungsi membantu jalannya beberapa operasi yang ada di program seperti penggunaan algoritma Jump Search dan Shell Sort.
## Fitur dan fungsionalitas
### Menu Login
Sebelum menggunakan program, tersedia menu login yaitu:
1. Login user: Digunakan oleh user yang sudah registrasi terlebih dahulu (memiliki username dan password yang tersimpan di database) 
2. Login admin: Digunakan oleh admin (memiliki username dan password yang tersimpan di database)
3. Registrasi: Apabila belum memiliki username dan password, dapat melakukan registrasi terlebih dahulu.
4. Keluar: Keluar dari program.
### Menu User
Pada menu user memiliki 5 fitur yang tersedia dan dapat digunakan yaitu:
1. Menambah anime baru ke playlist: User dapat menambahkan anime baru yang di sukai ke dalam playlistnya.
2. Menghapus anime di playlist: User dapat menghapus anime yang ada pada playlistnya. 
3. Memutar playlist: User dapat menonton video dari anime yang telah dipilih untuk diputar dan akan menampilkan video anime dari episode pertama, tetapi jika user ingin langsung menonton episode lain juga dapat dilakukan. 
Pada bagian ini juga user dapat melihat playlist sesuai dengan abjad (huruf depan judul anime dari playlist) disini kami menggunakan algoritma shell sort untuk mengurutkannya.
4. Melihat history: User dapat melihat history anime apa saja dan episode berapa saja yang telah ia tonton. Hal ini sangat bermanfaat bagi user, apabila ia sudah lama tidak menonton anime dan lupa sudah menonton anime apa saja dan episode berapa , maka ia tinggal mengecek history saja.
5. Keluar: Jika user ingin menyudahi menggunakan program, user dapat memilih keluar, untuk keluar dari program.
### Menu Admin
Pada menu admin memiliki 5 fitur yang dapat digunakan yaitu:
1. Menambah anime baru: Jika ada anime baru yang dirilis, maka admin dapat menambahkan anime tersebut ke dalam daftar anime yang tersedia. 
2. Menghapus anime yang ada: Admin dapat menghapus anime yang ada pada daftar anime yang tersedia.
3. Menambah episode baru: Jika episode baru dari anime yang tersedia dalam daftar telah keluar, admin dapat update atau menambahkan episode baru tersebut ke dalam daftar anime yang tersedia.
4. Melihat anime dan episode yang tersedia: Admin dapat mengecek anime dan episode apa saja yang tersedia dalam daftar, sehingga dapat memudahkan ketika nantinya admin akan mengupdate anime baru dan episode baru ke dalam playlist. 
5. Keluar: Jika admin sudah menyelesaikan semua pekerjaannya dan ingin menyudahi menggunakan program, admin dapat memilih keluar, untuk keluar dari program.
### Cara penggunaan 
Ketika memulai program, maka akan menampilkan menu login. Terdapat 2 login yang tersedia yaitu:
1. Login admin
2. Login user 
Untuk dapat login, pastikan telah memiliki username dan password yang tersimpan di database (telah melakukan registrasi) namun apabila belum memiliki  username dan password dapat memilih opsi 3 yaitu “registrasi” karena jika belum melakukan registrasi, maka program tidak dapat dijalankan. Ketika melakukan registrasi, maka akan diminta untuk membuat username dan password baru, masukkan username dan password yang dapat mudah diingat. Setelah selesai melakukan registrasi, pilihlah opsi login kemudian masukkan username dan password yang telah dibuat tadi, pastikan username dan password yang dimasukkan sudah sesuai. Jika username dan password benar, maka otomatis program dapat dijalankan dan jika salah maka tidak bisa masuk ke program.

Jika login sebagai admin, maka akan menampilkan 5 pilihan menu yang hanya dapat digunakan oleh admin (hak admin). Yaitu:
1.	Menambah anime baru: Apabila admin memilih opsi 1, Admin dapat menambahkan anime baru yang ke dalam daftar anime yang tersedia dengan cara memasukkan judul anime baru yang akan ditambahkan
2.	Menghapus anime: Apabila admin memilih opsi 2, admin dapat menghapus anime dari daftar anime yang tersedia, caranya yaitu dengan memasukkan judul anime yang akan dihapus, pastikan judul yang dimasukkan sesuai dengan yang ada pada daftar anime yang tersedia, perhatikan juga penggunaan huruf kapitalnya.
3.	Menambah episode baru: Apabila admin memilih opsi 3, Admin dapat menambahkan episode baru ke dalam daftar anime yang tersedia, caranya yaitu dengan memasukkan judul anime yang akan ditambahkan episodenya. Pastikan episode yang ditambahkan adalah episode yang belum ada pada daftar tersebut.
4.	Melihat anime dan episode yang tersedia: Apabila admin memilih opsi 4, Pada bagian ini dapat digunakan admin untuk mengecek daftar anime dan episode yang tersedia pada program.  Agar lebih mudah dan cepat disini admin dapat melihat daftar anime berdasarkan abjad huruf depan judul anime yang ada pada daftar.
5.	Opsi 5 digunakan jika admin ingin menyudahi menggunakan program.

Jika login sebagai user, maka akan menampilkan 5 pilihan menu yang hanya dapat digunakan oleh user (hak user). Yaitu:
1.	Menambah anime baru ke playlist: User dapat menambahkan anime baru yang di sukai ke dalam playlistnya dengan memasukkan judul anime tersebut (pastikan judul yang dimasukkan adalah yang terdapat pada daftar anime yang tersedia)
2.	Menghapus anime di playlist: User dapat menghapus anime yang ada pada playlistnya. Dengan cara memasukkan judul anime yang ada dalam playlist (pastikan penulisan huruf kapital dan huruf kecil sudah sesuai)
3.	Memutar playlist: Pada bagian ini terdapat 2 opsi yaitu:
- Mengurutkan anime sesuai abjad: Tampilan playlist user yang telah diurutkan sesuai abjad (huruf depan judul anime yang ada pada plalist user.
- Putar playlist: Pada bagian ini terdapat 2 opsi yaitu memutar anime dari awal (langsung ke video anime) dan mencari anime yang akan diputar, caranya yaitu user memasukkan judul anime yang akan diputar.
4.	Melihat history: Dengan memilih opsi 4 ini maka akan menampilkan semua history anime apa saja dan episode berapa saja yang telah ditonton user.
5.	Keluar: Opsi ini digunakan jika user ingin menyudahi program.

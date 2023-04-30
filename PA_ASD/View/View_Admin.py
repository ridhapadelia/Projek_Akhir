from Control.Control_Admin import tampilanAdmin2
# from Model.Pemutaran import Pemutaran
# from View.View_User import tampilanUser
# from Model.File_tambah import admin
# from Model.File_tambah import mutar



def tampiladmin():
        print("=======================================================")
        print("|             Selamat datang di Menu Admin            |")
        print("=======================================================")
        print("| 1. Tambahkan Anime baru                             |")
        print("| 2. Hapus Anime yang ada                             |")
        print("| 3. Melihat Anime dan episode yang ada               |")
        print("| 4. Masuk ke menu USER                               |")
        print("| 5. Keluar                                           |")
        print("=======================================================")
        tampilanAdmin2()
# mutar = Pemutaran()
# admin = Anime()

# def tampilanAdmin():
#     while True:
#         print("=======================================================")
#         print("|             Selamat datang di Menu Admin            |")
#         print("=======================================================")
#         print("| 1. Tambahkan Anime baru                             |")
#         print("| 2. Hapus Anime yang ada                             |")
#         print("| 3. Tambahkan Episode                                |")
#         print("| 4. Melihat Anime dan episode yang ada               |")
#         print("| 5. Masuk ke menu USER                               |")
#         print("| 6. Keluar                                           |")
#         print("=======================================================")
#         pilih = input("masukan pilihan anda :")
#         if pilih == "1":
#             anime   = input("masukan nama anime    : ")
#             episode = input("masukan episode : ")
#             admin.tambah_Anime(anime,episode)
#             g = 5 
#             while g > 0 :
#                 mutar.tambah_animep()
#                 g -= 1
#             # mutar.
#             print("admin anime  berhasil ditambahkan!")
#         elif pilih == "2":
#             admin.tampilan_anime()
#             anime = input("masukan nama anime yang inin dihapus : ")
#             Admin = admin.cari_anime(anime)
#             if Admin:
#                 admin.hapus_anime(anime)
#             else :
#                 print(f"nama anime {anime} tidak di temukan")
#         elif pilih == "3":
#             admin.tampilan_anime()
#             inputcari = int(input("masukan nomor anime yang ingin diupdate:"))
#             aa = admin.getindex(inputcari -1)
#             if anime :
#                 episodebaru = input("masukan episode baru :")
#                 admin.update_episode(aa,episodebaru)
#             else:
#                 print("episode berhasil ditambahkan.")

#         elif pilih == "4":
#             admin.tampilan_anime()
#             print("")
#             print("=========================================")
#             print("| 1. Urutkan anime sesuai abjad         |")
#             print("| 2. Keluar                             |")
#             print("=========================================")
#             print("")
#             urut = input("ingin melakukan apa??")
#             if urut == "1":
#                 admin.shell_sort()
#                 admin.tampilan_anime()
#             if urut == "2":
#                 tampilanAdmin()

#         elif pilih == "5":
#             tampilanUser()
#         elif pilih == "6":
#             exit()

# # tampilanAdmin()
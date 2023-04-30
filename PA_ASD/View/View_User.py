from Control.Control_User import tampilanUser
# from Control.Control_User import Playlist
# from Control.Control_User import Putar
# from Model.File_tambah import mutar

# a = mutar
# B = Putar
# C = Playlist

def tampilan12():
    print("======================================================")
    print("|             Selamat datang di BSstartion           |")
    print("======================================================")
    print("| 1. Tambahkan Anime baru ke Playlist                |")
    print("| 2. Hapus Anime yang ada di Playlist                |")
    print("| 3. Putar Playlist                                  |")
    print("| 4. Keluar                                          |")
    print("======================================================")
    tampilanUser()


# def episode(aa):
#     episode = aa
#     return episode
# def cari (ww):
#     input1 = ww
#     return input1

# def tampilanUser():
#     mutar.shell_sort()
#     admin.shell_sort()
#     while True:
#         print("======================================================")
#         print("|             Selamat datang di BSstartion           |")
#         print("======================================================")
#         print("| 1. Tambahkan Anime baru ke Playlist                |")
#         print("| 2. Hapus Anime yang ada di Playlist                |")
#         print("| 3. Putar Playlist                                  |")
#         print("| 4. Keluar                                          |")
#         print("======================================================")
#         pilih = input("masukan pilihan anda :")
#         if pilih == "1":
#             global episode1
#             admin.tampilan_anime()
#             anime   = input("masukan nama anime    : ")
#             episode1 = int(input("masukan episode : "))
#             qq = episode(episode1)
#             node = Anime()
#             # print(admin.manggil())
#             while admin.manggil(anime) is not None:
#                 if admin.manggil(anime) == anime:
#                     user.append(anime,qq)
#                     sw = admin.fibonacci_search(anime)
#                     print(sw)
#                     mutar1.update(sw,anime)
#                     mutar1.print()
#                     print("Anime berhasil ditambahkan ke playlist")
#                     tampilanUser()
#                 else :
#                     node.head != anime
#                     node.head = node.head.next
#                     print("Anime tidak ada !!")
#                     break
#             # user.tambah_playlist(anime,episode)
#         if pilih == "2":
#             user.tampilan_playlist()
#             anime = input("Masukan Judul anime yang ingin di hapus : ")
#             User = user.cari_playlist(anime)
#             if User :
#                 user.hapus_playlist(anime)
#             else :
#                 print("ANIME TIDAK ADA")
#         elif pilih == "3":
#                 if user.tampilan_playlist() is not None :
#                     print("Playlist kosong")
#                 else :
#                     while True:
#                         print("====================================")
#                         print("| 1. Cari Anime yang ingin diputar |")
#                         print("| 2. kembali                       |")
#                         print("====================================")
#                         urutu = input("Ingin memilih yang mana : ")
#                         if  urutu == "1":
#                                 user.shell_sort()
#                                 user.tampilan_playlist()
#                                 inputcari = input("masukan nama anime yang ingin diputar :")
#                                 hasil = mutar1.jumpSearch(mutar1.anime,inputcari,len(mutar1.anime))
#                                 if hasil ==-1:
#                                     print(f"anime {inputcari} tidak ditemukan")
#                                 else:
#                                     print(f"anime {inputcari} ditemukan pada index {hasil} ")
#                                     mutar.play_video2(hasil,episode1)
#                         elif urutu == "2":
#                                 break
#         elif pilih == "4":
#             exit()

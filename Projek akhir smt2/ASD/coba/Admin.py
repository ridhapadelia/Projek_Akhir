from Model.pemutaran import Pemutaran
import pemutaran as pemutaran
from prettytable import PrettyTable
import os

class Admin:
    def __init__(self, anime, episode):
        self.anime = anime
        self.episode = episode
        self.next = None

class Anime:
    def __init__(self):
        self.head = None
    def tambah_Anime(self, anime, episode):
        new_Anime = Admin(anime,episode)
        if not self.head:
            self.head = new_Anime  
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_Anime
    def tampilan_anime(self):
        if not self.head:
            print("Tidak ada Anime yang tersedia")
        else:
            current = self.head 
            table = PrettyTable(["NO", "JUDUL ANIME","EPISODE"])
            a = 1
            while current is not None:
                table.add_row([a , current.anime,current.episode])
                a += 1
                current = current.next
            print(table)

    def update_episode(self, anime, episode):
        Admin = self.cari_anime(anime)
        if Admin:
            Admin.episode = episode
            print("Episode anime berhasil diupdate!")
        else:
            print("episode anime tidak ditemukan")

    def cari_anime(self, anime):
        current = self.head
        while current is not None:
            if current.anime == anime:
                return current
            current = current.next
        return None

    def hapus_anime(self, anime):
        current = self.head
        if current and current.anime  == anime:
            self.head = current.next
            current = None
            print("Anime berhasil dihapus")
            return
        prev = None
        while current and current.anime != anime:
            prev = current
            current = current.next
        if current is None:
            print("Judul Anime tidak ditemukan")
            return
        prev.next = current.next
        current = None
        print("Anime berhasil dihapus!")

    def shell_sort(self):
            n = self.get_length()
            gap = n // 2
            while gap > 0:
                for i in range(gap, n):
                    temp_node = self.get_node_at_index(i)
                    anime = temp_node.anime
                    temp_episode = temp_node.episode
                    j = i
                    while j >= gap and self.get_node_at_index(j - gap).anime > anime:
                        node_j_gap = self.get_node_at_index(j - gap)
                        self.get_node_at_index(j).anime = node_j_gap.anime
                        self.get_node_at_index(j).episode = node_j_gap.episode
                        j -= gap
                    self.get_node_at_index(j).anime = anime
                    self.get_node_at_index(j).episode = temp_episode
                gap //= 2

    def get_length(self):
            current_node = self.head
            count = 0
            while current_node:
                count += 1
                current_node = current_node.next
            return count

    def get_node_at_index(self, index):
            current_node = self.head
            count = 0
            while current_node:
                if count == index:
                    return current_node
                count += 1
                current_node = current_node.next
            return None
data = Anime()
data.tambah_Anime("One Piece","5")
data.tambah_Anime("Black Clover","5")
data.tambah_Anime("Haikyu","5")
data.tambah_Anime("Fate Series","5")
data.tambah_Anime("Naruto","5")
data.tambah_Anime("hsdfirdif","7")


p = Pemutaran()
# p.mutar.tambah_animep()


def tampilanAdmin():
    while True:
        print("=======================================================")
        print("|             Selamat datang di Menu Admin            |")
        print("=======================================================")
        print("| 1. Tambahkan Anime baru                             |")
        print("| 2. Hapus Anime yang ada                             |")
        print("| 3. Tambahkan Episode                                |")
        print("| 4. Melihat Anime dan episode yang ada               |")
        print("| 5. Keluar                                           |")
        print("=======================================================")
        pilih = input("masukan pilihan anda :")
        if pilih == "1":
            anime   = input("masukan nama anime    : ")
            episode = input("masukan episode : ")
            data.tambah_Anime(anime,episode)
            print("data anime  berhasil ditambahkan!")
            p.tambah_animep()
        elif pilih == "2":
            data.tampilan_anime()
            anime = input("masukan nama anime yang inin dihapus : ")
            Admin = data.cari_anime(anime)
            if Admin:
                data.hapus_anime(anime)
            else :
                print(f"nama anime {anime} tidak di temukan")
        elif pilih == "3":
            data.tampilan_anime()
            anime = input("Masukan nama anime yang ingin ditambahkan episodenya : ")
            if anime == data.cari_anime :
                data.update_episode()
            else :
                print("Tidak ditemukan") 
        elif pilih == "4":
            data.tampilan_anime()
            print("")
            print("=========================================")
            print("| 1. Urutkan anime sesuai abjad         |")
            print("| 2. Keluar                             |")
            print("=========================================")
            print("")
            urut = input("ingin melakukan apa??")
            if urut == "1":
                data.shell_sort()
                data.tampilan_anime()
            if urut == "2":
                tampilanAdmin()

tampilanAdmin()

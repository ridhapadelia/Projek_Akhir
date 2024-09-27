from Model.File_tambah import mutar
from prettytable import PrettyTable
from Control.Penghubung import menuuser
import os

os.system('cls')

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
            
    def manggil(self,anime):
        current = self.head
        while current :
            if current.anime == anime:
                return current.anime
            current = current.next
        return None
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

    def getindex(self, index):
        current_node =self.head
        current_index = 0 

        while current_node is not None:
            if current_index == index:
                return current_node
            
            current_node = current_node.next
            current_index += 1
    
    def fibonacci_search(self, key):
        fib_nums = [0, 1]
        while fib_nums[-1] < self.get_length():
            fib_nums.append(fib_nums[-1] + fib_nums[-2])
        offset = -1
        fib_idx = len(fib_nums) - 1
        while fib_idx > 1:
            idx = min(offset + fib_nums[fib_idx - 2], self.get_length() - 1)
            if self.get_node_at_index(idx).anime < key:
                fib_idx -= 1
                offset = idx
            elif self.get_node_at_index(idx).anime > key:
                fib_idx -= 2
            else:
                return idx
        if fib_nums[fib_idx - 2] and self.get_node_at_index(offset + 1).anime == key:
            return offset + 1
        return -1
    

admin = Anime()
admin.tambah_Anime("Black Clover","5")
admin.tambah_Anime("Fate Series","5")
admin.tambah_Anime("Haikyu","5")
admin.tambah_Anime("Naruto","5")
admin.tambah_Anime("One Piece","5")



def tampilanadmin1():
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

def tampilanAdmin2():
    while True:
        pilih = input("masukan pilihan anda :")
        if pilih == "1":
            anime   = input("masukan nama anime    : ")
            episode = input("masukan episode : ")
            admin.tambah_Anime(anime,episode)
            g = 5 
            while g > 0 :
                mutar.tambah_animep()
                g -= 1
            os.system('cls')
            tampilanadmin1()
            print("admin anime  berhasil ditambahkan!")
            
        elif pilih == "2":
            admin.tampilan_anime()
            anime = input("masukan nama anime yang inin dihapus : ")
            Admin = admin.cari_anime(anime)
            if Admin:
                os.system('cls')
                admin.hapus_anime(anime)
                tampilanadmin1()
            else :
                os.system('cls')
                print(f"nama anime {anime} tidak di temukan")
                tampilanadmin1()
        elif pilih == "3":
            admin.tampilan_anime()
            print("")
            print("=========================================")
            print("| 1. Urutkan anime sesuai abjad         |")
            print("| 2. Keluar                             |")
            print("=========================================")
            print("")
            urut = input("ingin melakukan apa??")
            if urut == "1":
                os.system('cls')
                admin.shell_sort()
                admin.tampilan_anime()
                tampilanadmin1()
            if urut == "2":
                os.system('cls')
                tampilanadmin1()
        elif pilih == "4":
            menuuser()
            print()
        elif pilih == "5":
            exit()


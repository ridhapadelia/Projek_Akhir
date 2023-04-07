from Controller.Control_Admin import Anime
from Model.pemutaran import Pemutaran
from prettytable import PrettyTable

class User:
    def __init__(self, anime,episode):
        self.anime = anime
        self.episode = episode
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def tambah_playlist(self, anime,episode):
        new_playlist = User(anime,episode)
        if not self.head:
            self.head = new_playlist
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_playlist

    def tampilan_playlist(self):
        if not self.head:
            print("Playlist Kosong")
        else:
            current = self.head 
            table = PrettyTable(["NO", "JUDUL ANIME","EPISODE"])
            a = 1
            while current is not None:
                table.add_row([a , current.anime,current.episode])
                a += 1
                current = current.next
            print(table)

    def cari_playlist(self, anime):
        search = input("masukan anime yang ingin dicari")
        result = data1.fibonacci_search(anime)
        if result == -1:
            print(f"anime {search} tidak ditemukan")
        else:
            print(f"anime {search} ditemukan {result} ")


    def hapus_playlist(self, anime):
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
        current_node = self.head
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

u = Anime()
u.tambah_Anime("One Piece","5")
u.tambah_Anime("Black Clover","5")
u.tambah_Anime("Haikyu","5")
u.tambah_Anime("Fate Series","5")
u.tambah_Anime("Naruto","5")


g = Pemutaran()
g.append_onepiece('pict/one_piece/onepiece_1.mp4', 'pict/one_piece/onepiece_1.mp3')
g.append_onepiece('pict/one_piece/onepiece_2.mp4', 'pict/one_piece/onepiece_2.mp3')
g.append_onepiece('pict/one_piece/onepiece_3.mp4', 'pict/one_piece/onepiece_3.mp3')
g.append_onepiece('pict/one_piece/onepiece_4.mp4', 'pict/one_piece/onepiece_4.mp3')
g.append_onepiece('pict/one_piece/onepiece_5.mp4', 'pict/one_piece/onepiece_5.mp3')
g.append_blackclover('pict/black_clover/blackclover_1.mp4', 'pict/black_clover/blackclover_1_.mp3')
# g.append_blackclover('pict/black_clover/blackclover_2.mp4', 'pict/black_clover/blackclover_2_.mp3')
# g.append_blackclover('pict/black_clover/blackclover_3.mp4', 'pict/black_clover/blackclover_3_.mp3')
# g.append_blackclover('pict/black_clover/blackclover_4.mp4', 'pict/black_clover/blackclover_4_.mp3')
# g.append_blackclover('pict/black_clover/blackclover_5.mp4', 'pict/black_clover/blackclover_5_.mp3')


data1 = Playlist()
def tampilanUser ():
    while True:
        print("======================================================")
        print("|             Selamat datang di BSstation            |")
        print("======================================================")
        print("| 1. Tambahkan Anime baru ke Playlist                |")
        print("| 2. Hapus Anime yang ada di Playlist                |")
        print("| 3. Putar Playlist                                  |")
        print("| 4. Melihat  Histori Playlist                       |")
        print("| 5. Keluar                                          |")
        print("======================================================")
        pilih = input("masukan pilihan anda :")
        if pilih == "1":
            u.tampilan_anime()

            anime   = input("masukan nama anime    : ")
            episode = input("masukan episode : ")
            # node = u.Anime()
            # while node.head is not None:
            #     print(node.head.data)
            #     if node.head == anime:
            #         data1.tambah_playlist(anime,episode)
            #         print("Anime berhasil ditambahkan ke playlist")
            #         tampilanUser()
            #     else :
            #         node.head != anime

            #         node.head = node.head.next
            #         print("Anime tidak ada !!")
            data1.tambah_playlist(anime,episode)
        if pilih == "2":
            data1.tampilan_playlist()
            anime = input("Masukan Judul anime yang ingin di hapus : ")
            User = data1.cari_playlist(anime)
            if User :
                data1.hapus_playlist(anime)
            else :
                print("ANIME TIDAK ADA")
        if pilih == "3":
            data1.tampilan_playlist()
            print("====================================")
            print("| 1. urutkan playlist sesuai abjad |")
            print("| 2. Putar Anime                   |")
            print("====================================")
            urutu = input("Ingin memilih yang mana : ")
            if urutu == "1":
                data1.shell_sort()
                data1.tampilan_playlist()
            if urutu == "2":
                print("====================================")
                print("| 1. Putar Anime dari awal         |")
                print("| 2. Cari Anime yang ingin diputar |")
                print("====================================")
                inp = input("ingin melakukan yang mana : ")
                if inp == "1":
                    g.play_video()
                    print("")
                elif inp == "2":
                    data1.tampilan_playlist()
                    inputcari = input("masukan nama yang ingin cari :")
                    hasil = data1.fibonacci_search(inputcari)
                    if inputcari ==-1:
                        print(f"anime {inputcari} tidak ditemukan")
                    else:
                        print(f"anime {inputcari} ditemukan pada index {hasil} ")
                    print("=========================================")
                    print

tampilanUser()


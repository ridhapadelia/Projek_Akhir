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
        result = user.fibonacci_search(anime)
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
    
user = Playlist()
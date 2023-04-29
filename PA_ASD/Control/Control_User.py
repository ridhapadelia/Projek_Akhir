from prettytable import PrettyTable
from Control.Control_Admin import Anime
from Control.Control_Admin import admin
from Model.File_tambah import mutar

import os
import math
os.system('cls')

class User:
    def __init__(self, anime,episode):
        self.anime = anime
        self.episode = episode
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.judul = []
        self.episode = []

    def append(self,judul,episode):
        self.judul.append(judul)
        self.episode.append(episode)

    def tambah_playlist(self, anime,episode):
        new_playlist = User(anime,episode)
        if not self.head:
            self.head = new_playlist
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_playlist
            
    def manggil(self,anime):
        current = self.head
        while current :
            if current.anime == anime:
                return current.anime
            current = current.next
        return None

    def tampilan_playlist(self):
        if len(self.judul) == 0:
            os.system('cls')
            print("Playlist Kosong")
            tampilan1()
        else:
            table = PrettyTable(["NO", "JUDUL ANIME","EPISODE"])
            a = 1
            for i in range(len(self.judul)):
                table.add_row([a , self.judul[i],self.episode[i]])
                a += 1
            print(table)

    def cari_playlist(self, anime):
        search = input("masukan anime yang ingin dicari")
        result = user.jumpSearch(anime)
        if result == search:
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
    def jumpSearch(self, arr , x , n ):
        step = math.sqrt(n)
        prev = 0
        while arr[int(min(step, n)-1)] < x:
                    prev = step
                    step += math.sqrt(n)
                    if prev >= n:
                        return -1
        while arr[int(prev)] < x:        
                    prev += 1
                    if prev == min(step, n):
                        return -1
        if arr[int(prev)] == x:
                return int(prev)
        return -1

    
class Putar:
    def __init__(self):
        self.anime = ["","","","",""]
    def jumpSearch(self, arr , x , n ):
        step = math.sqrt(n)
        prev = 0
        while arr[int(min(step, n)-1)] < x:
                    prev = step
                    step += math.sqrt(n)
                    if prev >= n:
                        return -1
        while arr[int(prev)] < x:        
                    prev += 1
                    if prev == min(step, n):
                        return -1
        if arr[int(prev)] == x:
                return int(prev)
                
        return -1
    def update(self,r,q):
        self.anime.pop(r)
        self.anime.insert(r,q)
    def print(self):
        print(self.anime)
    def delete(self, r):
        self.anime.pop(r)

user = Playlist()
mutar1 = Putar()


def episode(aa):
    episode = aa
    return episode
def cari (ww):
    input1 = ww
    return input1

def tampilan1():
    print("======================================================")
    print("|             Selamat datang di BSstartion           |")
    print("======================================================")
    print("| 1. Tambahkan Anime baru ke Playlist                |")
    print("| 2. Hapus Anime yang ada di Playlist                |")
    print("| 3. Putar Playlist                                  |")
    print("| 4. Keluar                                          |")
    print("======================================================")
    tampilanUser()

def tampilanUser():
    mutar.shell_sort()
    admin.shell_sort()
    while True:
        pilih = input("masukan pilihan anda :")
        if pilih == "1":
            global episode1
            admin.tampilan_anime()
            anime   = input("masukan nama anime    : ")
            episode1 = int(input("masukan episode : "))
            qq = episode(episode1)
            node = Anime()
            while admin.manggil(anime) is not None:
                if admin.manggil(anime) == anime:
                    user.append(anime,qq)
                    sw = admin.fibonacci_search(anime)
                    print(sw)
                    mutar1.update(sw,anime)
                    mutar1.print()
                    os.system('cls')
                    print("Anime berhasil ditambahkan ke playlist")
                    tampilan1()
                elif admin.manggil(anime) != anime :
                    node.head != anime
                    node.head = node.head.next
                    print("Anime tidak ada !!")
                    tampilan1()
                else : 
                    os.system('cls')
                    print("erorr!!! silahkan kembali")
                    tampilan1()
            # user.tambah_playlist(anime,episode)
        if pilih == "2":
            if user.tampilan_playlist() is not None :
                    os.system('cls')
                    print("Playlist kosong")
                    tampilan1()
            # user.tampilan_playlist()
            else :
                anime = input("Masukan Judul anime yang ingin di hapus : ")
                User = user.jumpSearch(anime)
                if User :
                    user.hapus_playlist(anime)
                    user.tampilan_playlist()
                    print("Berhasil Menghapus! ")
                else :
                    print("Gagal Menghapus!!!")
                    ky = input("Apakah Ingin Kembali? Y/N : ")
                    if ky == "Y":
                        tampilan1()
                    else :
                        exit()
        elif pilih == "3":
                if user.tampilan_playlist() is not None :
                    os.system('cls')
                    print("Playlist kosong")
                    tampilan1()
                else :
                    while True:
                        print("====================================")
                        print("| 1. Cari Anime yang ingin diputar |")
                        print("| 2. kembali                       |")
                        print("====================================")
                        urutu = input("Ingin memilih yang mana : ")
                        if  urutu == "1":
                                user.shell_sort()
                                user.tampilan_playlist()
                                inputcari = input("masukan nama anime yang ingin diputar :")
                                hasil = mutar1.jumpSearch(mutar1.anime,inputcari,len(mutar1.anime))
                                if hasil ==-1:
                                    os.system('cls')
                                    print(f"anime {inputcari} tidak ditemukan")
                                    tampilan1()
                                else:
                                    os.system('cls')
                                    print(f"anime {inputcari} ditemukan pada index {hasil} ")
                                    mutar.play_video2(hasil,episode1)
                                    tampilan1()
                        elif urutu == "2":
                                break
                        os.system('cls')
                        tampilan1()
        elif pilih == "4":
            exit()

import time
class Node:
    def __init__(self, video):
        
        self.prev = None
        self.next = None
        self.video = video

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.next = None
        
class UserList:
    def __init__(self):
        self.head = None
        
    def register(self, username, password):
        new_user = User(username, password)
        if self.head is None:
            self.head = new_user
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_user
        print("Registration successful!")
        
    def login(self, username, password):
        current = self.head
        while current is not None:
            if current.username == username and current.password == password:
                print("Login successful!")
                return
            current = current.next
        print("Invalid username or password")
        

# class Tampilan:
#     def __init__(self):
#         self.head = None

#     def add_node(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node

#     def display_list(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next

#     playlist = ["One Piece", "Black Clover", "Kimetsu No Yaiba",
#         "Boku No Hero", "Hunter X Hunter", "Haikyuu!", "Fate Series"]

# linked_list = Tampilan()
# linked_list.add_node( playlist = ["One Piece", "Black Clover", "Kimetsu No Yaiba",
#         "Boku No Hero", "Hunter X Hunter", "Haikyuu!", "Fate Series"])


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.history = []
        self.played_videos = []

    def add_video(self, video):
        if self.head is None :
            self.head  = Node(video)
        else :
            nodebaru = Node(video)
            nodebaru.next = self.head
            self.head = nodebaru

    def remove_video(self, video):
        curr = self.head
        while curr is not None:
            if curr.video == video:
                if curr.prev is not None:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                self.size -= 1
                self.history.append(('remove', video))
                return
            curr = curr.next
    def cari(self,video):
        curr = self.head
        while curr is not None:
            if curr.video == video:
                return curr
            curr = curr.next
        return None
    def display(self):
        curr = self.head
        p = 1
        print("======================================")
        print("|           Anime Yang Tersedia      |")
        print("======================================")
        while curr is not None:
            
            print(f'{p}. {curr.video}')
            p+=1
            curr = curr.next

    def display_history(self):
        print("History:")
        for action, video in self.history:
            print(f"{action} {video}")

user_list = UserList()
panggil = Playlist()



history = []
playlist_history = []


episode = 0
def waktu():
    time.sleep(0.5)
def berikut(input3,episode):
    print("Sedang Menonton Anime ",input3)
    waktu()
    episode += 1
    print(f'Episode {episode} telah selesai')
    if episode == 12:
        print("Episode Telah Habis")
        episode-=12
        tampilan()
    l = input (f"Apakah ingin melanjutkan? : ")
    if l == "y":
        berikut(input3, episode)
    else:
        episode -= episode
        tampilan()

def tampilan ():
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
        choice = input("Silahkan pilih yang mana : ")
        if choice == "1":
            print("======================================")
            print("|           Anime Yang Tersedia      |")
            print("======================================")
            # linked_list
            print("")
            video1 = int(input("Silahkan Masukkan Anime Yang Ingin Ditambahkan Ke Dalam Playlist:"))
            # panggil.add_video(linked_list[video1-1])
            print(f"Anime {video1} telah ditambahkan ke playlist")

        elif choice == "2":
            panggil.display()
            video = (input(
                "ketikan nama anime yang ingin dihapus, nama anime harus ada diplaylist : "))
            panggil.remove_video(video)
            print("Berhasil menghapus anime ")

        elif choice == "3":
            while True:
                print("============================================")
                print("|             Daftar Playlist               |")
                print("============================================")
                panggil.display()
                print("")
                print("===========================================")
                print("|             1.Putar playlist             |")
                print("|             2. Kembali                   |")
                print("===========================================")
                print("")
                index = input("ingin melakukan apa? ")
                if index == "1":
                        input3 = input("Masukan Nama Anime Yang Ingin Ditonton: ")
                        anime1 = panggil.cari(input3)
                        if anime1 :
                            history.append(input3)
                            berikut(input3,episode)
                        else:
                            print('Anime Tidak ada dalam playlist')
                            break
                elif index == "2":
                    break

        elif choice == "4":
            if not history:
                print("Belum ada histori yang tersimpan")
            else:
                print("Histori Playlsit.")
                for i, video in enumerate(history):
                    print(f"| {i+1}. {video:<24} |12 Eps|")

        elif choice == "5":
            break
        else:
            print("Pilihan tidak ada")




while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_list.register(username, password)
        
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_list.login(username, password)
        tampilan()
        
    elif choice == "3":
        break
        
    else:
        print("Invalid choice")








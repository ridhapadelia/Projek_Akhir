from Control.Penghubung import menuuser
from prettytable import PrettyTable
import pygame
import cv2

class Node:
    def __init__(self, video_file, audio_file):
        self.video_file = video_file
        self.audio_file = audio_file
        self.next = None

class Pemutaran:
    def __init__(self):
        self.head = None
        self.playing = False 
        

    def append(self, video_file, audio_file):
        new_node = Node(video_file, audio_file)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def manggil(self,anime):
        current = self.head
        while current :
            if current.anime == anime:
                return current.anime
            current = current.next
        return None

    def append_onepiece(self, video_file, audio_file):
        new_node = Node(video_file, audio_file)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def append_blackclover(self, video_file, audio_file):
        new_node = Node(video_file, audio_file)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def append_naruto(self, video_file, audio_file):
        new_node = Node(video_file, audio_file)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def append_haikyu(self, video_file, audio_file):
        new_node = Node(video_file, audio_file)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def append_fateseries(self, video_file, audio_file):
        new_node = Node(video_file, audio_file)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def handle_events(self):  
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  
                    self.playing = False
                if event.key == pygame.K_ESCAPE:  
                    self.playing = False
                    pygame.quit()
                    cv2.destroyAllWindows()

    def play_video2(self,index,mm):
        pygame.mixer.pre_init(4410, -16, 2, 2048) 
        pygame.init()
        clock = pygame.time.Clock()
        ff = 0
        ff += index
        if ff > 0:
            hh  = 0
            hh += ff
            while hh > 0:
                ff += 4
                hh -= 1
        io = 0
        io += mm
        ss = self.getindex(ff)
        # sr = self.cari(ss)
        while io > 0:
            ss = self.getindex(ff)
            video_file = ss.video_file
            audio_file = ss.audio_file

            cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
            cv2.namedWindow('Audio', cv2.WINDOW_NORMAL)
            cap = cv2.VideoCapture(video_file)

            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            aspect_ratio = width / height

            display_width = 640
            display_height = int(display_width / aspect_ratio)
            video_fps = cap.get(cv2.CAP_PROP_FPS)
            
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            self.playing = True  
            while cap.isOpened() and self.playing:
                ret, frame = cap.read()
                if ret:
                    resized_frame = cv2.resize(frame, (display_width, display_height))
                    cv2.imshow('Video', resized_frame)
                    clock.tick(video_fps)
                    self.handle_events() 
                    if cv2.waitKey(25) & 0xFF == ord('x'):
                        ff += 1
                        break  
                    elif cv2.waitKey(25) & 0xFF == ord('z'):
                        print("Keluar dari tontonan !")
                        print("")
                        hg = input("Kembali Ke Menu User?: ")
                        if hg == "y":
                            menuuser()
                            print("")
                        else:
                            exit()
                    
                        exit()
                else:
                    break
            cap.release()
            pygame.mixer.music.stop() 
            cv2.destroyAllWindows()
            io -= 1

    def getindex(self, index):
        current_node =self.head
        current_index = 0 
        while current_node is not None:
            if current_index == index:
                return current_node
            
            current_node = current_node.next
            current_index += 1
    def cari(self,data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None
    def add_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(index-1):
                if current is None:
                    raise Exception("Index out of bounds")
                current = current.next
            new_node.next = current.next
            current.next = new_node

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
    
    def shell_sort(self):
            n = self.get_length()
            gap = n // 2
            while gap > 0:
                for i in range(gap, n):
                    temp_node = self.get_node_at_index(i)
                    anime = temp_node.video_file
                    temp_episode = temp_node.audio_file
                    j = i
                    while j >= gap and self.get_node_at_index(j - gap).video_file > anime:
                        node_j_gap = self.get_node_at_index(j - gap)
                        self.get_node_at_index(j).video_file = node_j_gap.video_file
                        self.get_node_at_index(j).audio_file = node_j_gap.audio_file
                        j -= gap
                    self.get_node_at_index(j).video_file = anime
                    self.get_node_at_index(j).audio_file = temp_episode
                gap //= 2


mutar = Pemutaran()

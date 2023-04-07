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


    def handle_events(self):  
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  
                    self.playing = False
                if event.key == pygame.K_ESCAPE:  
                    self.playing = False
                    pygame.quit()
                    cv2.destroyAllWindows()

    def play_video(self):
        pygame.mixer.pre_init(4410, -16, 2, 2048) 
        pygame.init()
        clock = pygame.time.Clock()
        current_node = self.head
        while current_node is not None:
            video_file = current_node.video_file
            audio_file = current_node.audio_file

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
                        break
                    elif cv2.waitKey(25) & 0xFF == ord('z'):
                        exit()
                else:
                    break
            cap.release()
            pygame.mixer.music.stop() 
            cv2.destroyAllWindows()
            current_node = current_node.next
    
    def tambah_animep(self):
        anime   = input("masukan nama file video yang ingin di tambah: ")
        suara =input("masukan nama file suara yang ingin di tambah: ")
        g.append(anime,suara)
        # mutar.append(anime,suara)
        print("berhasil di tambahkan ")
        g.play_video()
        # mutar.play_video()

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

# mutar = Pemutaran()

# anime   = input("masukan nama file video yang ingin di tambah: ")
# suara =input("masukan nama file suara yang ingin di tambah: ")
# mutar.append(anime,suara)
# print("berhasil di tambahkan ")
# mutar.play_video()

# pemutaran.play_video()

g = Pemutaran()
g.append_onepiece('pict/one_piece/onepiece_1.mp4', 'pict/one_piece/onepiece_1.mp3')
g.append_onepiece('pict/one_piece/onepiece_2.mp4', 'pict/one_piece/onepiece_2.mp3')
g.append_onepiece('pict/one_piece/onepiece_3.mp4', 'pict/one_piece/onepiece_3.mp3')
g.append_onepiece('pict/one_piece/onepiece_4.mp4', 'pict/one_piece/onepiece_4.mp3')
g.append_onepiece('pict/one_piece/onepiece_5.mp4', 'pict/one_piece/onepiece_5.mp3')
g.append_blackclover('pict/black_clover/blackclover_1.mp4', 'pict/black_clover/blackclover_1_.mp3')

print(g.head.video_file)
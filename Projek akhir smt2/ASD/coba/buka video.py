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

    def append(self, video_file, audio_file):
        new_node = Node(video_file, audio_file)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def play_video(self):
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

            frequency = 10000
            size = -16
            channels = 1
            buffer = 324233

            
            pygame.mixer.pre_init(frequency, size, channels, buffer)

            pygame.init()
            audio = pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

            clock = pygame.time.Clock()
            while cap.isOpened():
                # Baca frame video
                ret, frame = cap.read()
                if ret:
                    resized_frame = cv2.resize(frame, (display_width, display_height))
                    cv2.imshow('Video', resized_frame)
                    clock.tick(video_fps)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            audio.release()
            cv2.destroyAllWindows()
            current_node = current_node.next

pemutaran = Pemutaran()

pemutaran.append('onepiece_1.mp4', 'ops.mp3')

pemutaran.play_video()

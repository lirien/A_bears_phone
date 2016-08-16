import wave
import pygame
import Queue

class SoundManager:

    def __init__(self):
        pygame.mixer.init(16000)
        self.sounds = Queue.Queue()

    def play(self, sound):
        self.sounds.queue.clear()
        pygame.mixer.music.load("content/sounds/{0}.wav".format(sound))
        pygame.mixer.music.play()

    def enqueue(self, sound):
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.load("content/sounds/{0}.wav".format(sound))
            pygame.mixer.music.play()
        else:
            self.sounds.put("content/sounds/{0}.wav".format(sound))

    def update(self):
        while pygame.mixer.music.get_busy():
            continue
        if self.sounds.empty() == False:
            pygame.mixer.music.load(self.sounds.get())
            pygame.mixer.music.play()

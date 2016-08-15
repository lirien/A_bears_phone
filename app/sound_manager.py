import wave
import pygame

class SoundManager:
    sounds = dict()

    def __init__(self):
        pygame.mixer.init(16000)

    def play(self, sounds):
        for sound in sounds:
            pygame.mixer.music.load("content/sounds/{0}.wav".format(sound))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue

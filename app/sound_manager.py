import pyaudio
import wave

class SoundManager:
    sounds = dict()

    def __init__(self):
        self.chunk_size = 32768
        self.audio = pyaudio.PyAudio()

    def play(self, sound):
        if not sound in self.sounds:
            self.sounds[sound] = wave.open("content/sounds/{0}.wav".format(sound), 'rb')

        self.__play_sound__(self.sounds[sound])

    def __play_sound__(self, source):
        source.rewind()
        channels = source.getnchannels()
        frame_rate = source.getframerate()
        sample_width = source.getsampwidth()

        stream = self.audio.open(format=self.audio.get_format_from_width(sample_width),
                                 channels=channels,
                                 rate=frame_rate,
                                 output=True)
        chunk = source.readframes(self.chunk_size)

        while chunk != '':
            stream.write(chunk)
            chunk = source.readframes(self.chunk_size)

        stream.stop_stream()
        stream.close()

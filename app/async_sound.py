from subprocess import Popen

class AsyncSound:
    process = None

    def play(self, sounds):
        if AsyncSound.process != None:
            try:
                AsyncSound.process.terminate()
            except:
                print "Failed to terminate child."

        AsyncSound.process = Popen(['python', 'play_sound.py'] + sounds)

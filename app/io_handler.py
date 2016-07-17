from subprocess import call
from matrix_keypad import RPi_GPIO

class IOHandler:
    def __init__(self):
        self.kp = RPi_GPIO.keypad()

    def read(self):
        digitPressed = None
        while digitPressed == None:
            digitPressed = self.kp.getKey()
        return digitPressed

    def write(self, text):
        try:
            call(['flite', '-voice', 'awb', '-t', format(text)])
        except OSError:
            try:
                call(['say', text])
            except OSError:
                print text

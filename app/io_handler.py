from subprocess import call
from matrix_keypad import RPi_GPIO
from RPi import GPIO

class IOHandler:
    TOGGLE_PIN = 11

    def __init__(self):
        self.kp = RPi_GPIO.keypad()
        self.GPIO.setup(TOGGLE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @property
    def active(self):
        if GPIO.input(TOGGLE_PIN):
            return False
        else:
            return True

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

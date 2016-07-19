from subprocess import Popen
from matrix_keypad import RPi_GPIO
from RPi import GPIO

class IOHandler:
    TOGGLE_PIN = 11

    def __init__(self):
        self.kp = RPi_GPIO.keypad()
        GPIO.setup(IOHandler.TOGGLE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.was_active = False
        self.process = None

    @property
    def active(self):
        if GPIO.input(IOHandler.TOGGLE_PIN):
            return False
        else:
            return True

    def read(self):
        digitPressed = None
        while digitPressed == None:
            digitPressed = self.kp.getKey()
            if not self.active:
                return None
        return digitPressed

    def write(self, text):
        if self.process != None:
            self.process.terminate()
            self.process = None
        try:
            self.process = Popen(['flite', '-voice', 'awb', '-t', text])
        except OSError:
            try:
                self.process = Popen(['say', text])
            except OSError:
                print text

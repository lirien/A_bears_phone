#from matrix_keypad import RPi_GPIO
from dialog_tree import DialogTree
from pprint import pprint

def main():
    dialog_tree = DialogTree()
    dialog_tree.load('content/dialog.json')

    print dialog_tree.active_text

    #kp = RPi_GPIO.keypad()

def digit():
    # Loop while waiting for a keypress
    digitPressed = None
    while digitPressed == None:
        digitPressed = kp.getKey()
    return digitPressed

main()

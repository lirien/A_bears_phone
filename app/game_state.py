from dialog_tree import DialogTree
from io_handler import IOHandler

class GameState:
    def __init__(self):
        self.dialog_tree = DialogTree()
        self.dialog_tree.load('content/dialog.json')
        self.io = IOHandler()

    def update(self):
        self.io.write(self.dialog_tree.active_text)

        option = self.io.read()
        if option == 0:
            self.io.write('All operators are unavailable at this time.')
            return
        elif option == 9:
            return

        try:
            self.dialog_tree.select_option(option)
        except:
            self.io.write('That was not a valid option.')

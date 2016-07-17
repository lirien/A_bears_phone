from subprocess import call

class IOHandler:
    def read(self):
        return raw_input('Select an option: ')

    def write(self, text):
        call(['say', text])

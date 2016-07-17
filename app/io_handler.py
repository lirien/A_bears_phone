from subprocess import call

class IOHandler:
    def read(self):
        return raw_input('Select an option: ')

    def write(self, text):
        try:
            call(['flite', '-voice', 'awb', '-t', format(text)])
        except OSError:
            try:
                call(['say', text])
            except OSError:
                print text

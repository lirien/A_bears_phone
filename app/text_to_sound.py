from subprocess import call

class TextToSound:
    def write_file(self, filename, text):
        call(['flite', '-voice', 'awb', '-t', text, '-o', 'content/sounds/tweets/{0}.wav'.format(filename)])

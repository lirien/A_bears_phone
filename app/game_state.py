from twitter_feed import TwitterFeed
from io_handler import IOHandler

class GameState:
    def __init__(self):
        self.twitter_feed = TwitterFeed()
        self.io = IOHandler()

    def update(self):
        if !self.io.active
            print "Phone is on hook."
            return

        option = self.io.read()

        if option == '*':
            self.io.write('I am a bear. My stories come from the twitter feed of ' +
                          'a underscore single underscore bear.')
            return
        elif option == '#':
            self.display_help()
            return
        else:
            self.io.write(self.twitter_feed.get_tweet(int(option)))

    def display_help(self):
        self.io.write('Hello! I am a bear.')
        self.io.write('If you want to hear a story, press a number.')
        self.io.write('If you want to learn more about me, press star.')
        self.io.write('If you want to hear this message again, press pound.')

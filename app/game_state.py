from twitter_feed import TwitterFeed
from io_handler import IOHandler

class GameState:
    def __init__(self):
        self.twitter_feed = TwitterFeed()
        self.io = IOHandler()

    def update(self):
        if not self.io.active:
            self.twitter_feed.reset()
            return

        if self.io.active_changed:
            self.display_help()

        option = self.io.read()
        if option == '*':
            self.io.write('Hooray. I will get more stories from twitter.')
            self.twitter_feed.load_more()
            return
        elif option == '#':
            self.display_help()
            return
        elif option != None:
            self.io.write(self.twitter_feed.get_tweet(int(option)))

    def display_help(self):
        self.io.write('Hello! I am a bear. I tell stories from twitter user ' +
                      'A underscore single underscore bear. ' +
                      'If you want to hear a story, press a number. ' +
                      'If you want more stories, press star. ' +
                      'If you want to hear this message again, press pound.')

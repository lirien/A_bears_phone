from twitter_feed import TwitterFeed
from io_handler import IOHandler

class GameState:
    def __init__(self):
        self.twitter_feed = TwitterFeed()
        self.io = IOHandler()

    def update(self):
        self.twitter_feed.test()
        option = self.io.read()

        if option == 0:
            self.io.write('All operators are unavailable at this time.')
            return
        elif option == 9:
            return

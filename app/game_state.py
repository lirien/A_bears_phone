from twitter_feed import TwitterFeed
from io_handler import IOHandler
from async_sound import AsyncSound

class GameState:
    def __init__(self):
        self.twitter_feed = TwitterFeed()
        self.io = IOHandler()
        self.sound_manager = AsyncSound()

    def update(self):
        if not self.io.active:
            self.io.was_active = False
            self.twitter_feed.reset()
            return

        if not self.io.was_active:
            self.io.was_active = True
            self.display_help()

        option = self.io.read()
        if option != None:
            print option
            self.sound_manager.play("{0}".format(option))
        if option == '*':
            self.sound_manager.play('load_more')
            self.twitter_feed.load_more()
            return
        elif option == '#':
            self.display_help()
            return
        elif option != None:
            self.io.write(self.twitter_feed.get_tweet(int(option)))

    def display_help(self):
        self.sound_manager.play('intro')

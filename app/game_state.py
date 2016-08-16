from twitter_feed import TwitterFeed
from io_handler import IOHandler
from sound_manager import SoundManager

class GameState:
    def __init__(self):
        self.twitter_feed = TwitterFeed()
        self.io = IOHandler()
        self.sound_manager = SoundManager()

    def update(self):
        if not self.io.active:
            self.io.was_active = False
            self.twitter_feed.reset()
            return

        if not self.io.was_active:
            self.io.was_active = True
            self.display_help()

        option = self.io.read()
        if option == '*':
            self.sound_manager.play('*')
            self.sound_manager.enqueue('load_more')
            self.twitter_feed.load_more()
            self.sound_manager.update()
            return
        elif option == '#':
            self.display_help()
            return
        elif option != None:
            self.sound_manager.play(str(option))
            self.sound_manager.enqueue('tweets/{0}'.format(self.twitter_feed.get_tweet(int(option))))

        self.sound_manager.update()

    def display_help(self):
        self.sound_manager.play('intro')

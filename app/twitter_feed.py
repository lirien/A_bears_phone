import twitter
import json

class TwitterFeed:
    def __init__(self):
        with open('config.json') as data_source:
            self.config = json.load(data_source)

        self.api = twitter.Api(consumer_key=self.config['consumer_key'],
                               consumer_secret=self.config['consumer_secret'],
                               access_token_key=self.config['access_token_key'],
                               access_token_secret=self.config['access_token_secret'])

    def test(self):
        statuses = self.api.GetUserTimeline(screen_name='A_single_bear')
        print([s.text for s in statuses])

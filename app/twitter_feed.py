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
        self.__get_timeline__()

    def __get_timeline__(self):
        self.timeline = dict()

        try:
            statuses = self.api.GetUserTimeline(screen_name='A_single_bear',
                                                exclude_replies=True,
                                                count=200)
            self.timeline['tweets'] = [s.text.replace('#', 'hash tag') for s in statuses]
            with open('content/tweets.json', 'w') as outfile:
                json.dump(self.timeline, outfile)
        except:
            """If we have an API failure, load cached tweets"""
            with open('content/tweets.json') as infile:
                self.timeline = json.load(infile)

    def get_tweet(self, index):
        self.current_tweet = self.timeline['tweets'][index]
        return self.current_tweet

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

    def get_timeline(self):
        timeline = dict()
        
        try:
            statuses = self.api.GetUserTimeline(screen_name='A_single_bear',
                                                exclude_replies=True,
                                                count=50)
            timeline['tweets'] = [s.text for s in statuses]
            with open('content/tweets.json', 'w') as outfile:
                json.dump(timeline, outfile)
        except:
            """If we have an API failure, load cached tweets"""
            with open('content/tweets.json') as infile:
                timeline = json.load(infile)

        return timeline['tweets']

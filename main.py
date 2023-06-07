import tweepy
from textblob import TextBlob

class TwitterAnalyzer:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        
    def get_tweets(self, username, count=10):
        return tweepy.Cursor(self.api.user_timeline, id=username, tweet_mode='extended').items(count)
        
    def analyze_sentiment(self, tweet):
        analysis = TextBlob(tweet.full_text)
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'

    def analyze_user_tweets(self, username, count=10):
        tweets = self.get_tweets(username, count)
        sentiment_counts = {'Positive': 0, 'Neutral': 0, 'Negative': 0}

        for tweet in tweets:
            sentiment = self.analyze_sentiment(tweet)
            sentiment_counts[sentiment] += 1

        return sentiment_counts


import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


# client = tweepy.Client(bearer_token)

class Authentication:
    
    def authorization(self):
        client = tweepy.Client(
            consumer_key=consumer_key, consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )

        # print(client.get_me())
        return client
        # self.create_tweet(client=client)
        

    
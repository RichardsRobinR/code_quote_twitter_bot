import schedule
import time
from pytz import timezone
import authentication
import generate_new_quote

class TweetScheduler:
   
    def __init__(self):
        self.authentication = authentication.Authentication()
        self.client = self.authentication.authorization()
        self.generateNewQuote = generate_new_quote.GenerateNewQuote()
        self.tweet_dict = self.generateNewQuote.generateNew()  
        self.run_scheduler()
    
    def print_good_morning(self,):
        print("Good morning   !")

    def create_tweet(self):
        self.text = "{} - {}".format(self.tweet_dict['quote'],self.tweet_dict['author'])
        response = self.client.create_tweet(text=self.text)
        print(f"https://twitter.com/user/status/{response.data['id']}")

    def run_scheduler(self):
        # Schedule the task to run every day at 6:00 AM
        schedule.every().day.at("06:00",timezone("Asia/Calcutta")).do(self.create_tweet)

        while True:
            schedule.run_pending()
            time.sleep(1)


scheduler = TweetScheduler()

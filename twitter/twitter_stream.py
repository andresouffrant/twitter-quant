import tweepy
from tweepy.streaming import StreamListener
from configobj import ConfigObj

# define variables
twitter_conf_filename = "../config/twitter.conf"

def readConfig(filename):
    ''' reads the config file into a dictionary object '''
    return ConfigObj(filename)

class StdOutListener(StreamListener):
    ''' sets up a listener that prints data and errors '''
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    # read config
    config = readConfig(twitter_conf_filename)
    
    # authenticates and sets up stream
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_token"], config["access_token_secret"])
    stream = tweepy.Stream(auth, listener)

    # filter the stream
    stream.filter(track=["AAPL"])

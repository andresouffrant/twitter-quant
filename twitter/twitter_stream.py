import tweepy
from configobj import ConfigObj
import os

# define variables
twitter_conf_filename = "../config/twitter.conf"

def readConfig(filename):
    return ConfigObj(filename)

if __name__ == "__main__":
    config = readConfig(twitter_conf_filename)
    print(config["consumer_key"])


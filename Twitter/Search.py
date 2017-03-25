#!/usr/bin/env pyh
import tweepy
from tweepy import OAuthHandler

import twitterstream


class Search:

    def __init__(self):
        auth = OAuthHandler(twitterstream.consumer_key, twitterstream.consumer_secret)
        auth.set_access_token(twitterstream.access_token, twitterstream.access_secret)
        self.api = tweepy.API(auth)


    def print_status (self):
        for status in tweepy.Cursor(self.api.home_timeline).items(10):
            print(status.text)


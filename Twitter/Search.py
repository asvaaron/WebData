#!/usr/bin/env pyh
import tweepy
from tweepy import OAuthHandler

import twitterstream


class Search:

    def __init__(self):
        auth = OAuthHandler(twitterstream.consumer_key, twitterstream.consumer_secret)
        auth.set_access_token(twitterstream.access_token, twitterstream.access_secret)
        self.api = tweepy.API(auth)
        # entry point for most of the Twitter operations .


    def print_status (self):
        for status in tweepy.Cursor(self.api.home_timeline).items(100):
            print(status.text)


    def search_query (self, query, count =None, lang="en"):
        if count is None or (count >1000):
            count = 1000
            # max tweets
        return self.api.search(q=query,count=count, lang=lang, show_user=True)


    def seach_results(self, search_results):
        for search_result in search_results:
            print search_result.text.encode('utf8')
            print search_result.created_at
            print search_result.author._json['screen_name']


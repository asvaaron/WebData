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
        if (not self.api):
            print ("Can't Authenticate")



    def print_status (self):
        for status in tweepy.Cursor(self.api.home_timeline).items(100):
            print(status.text)


    def search_query (self, query, count =None, lang="en OR es"):
        if count is None or (count >1000):
            count = 1000
            # max tweets
        search_results= self.api.search(q=query, count=count, lang=lang, show_user=True)
        for search_result in search_results:
            print search_result.text.encode('utf8')
            print search_result.created_at
            print search_result.author._json['screen_name']
            print search_result.lang
            #print search_results.favorited
            print search_result.entities.get('urls')
            print search_result.entities.get('hashtags')
            print search_result.entities.get('country')
            print search_result.favorite_count
            # Indicates approximately how many times this Tweet has been liked by Twitter users.

    def seach_results(self, search_results):
        for search_result in search_results:
            print search_result.text.encode('utf8')
            print search_result.created_at
            print search_result.author._json['screen_name']
            print search_result.lang
            #print search_result.place._json['country']





import datetime

"""Model Class used in MVC design"""
class model():
    reddit_api = None
    twitter_api = None

    reddit_username = None
    twitter_username = None

    reddit_user = None

    reddit_post_list = None

    def __init__(self, reddit_api):
        self.reddit_api = reddit_api

    def set_username(self, username):
        self.reddit_username = username

    def set_reddit_user(self, reddit_user):
        self.reddit_user = reddit_user

    def get_posts(self):
        return self.reddit_post_list










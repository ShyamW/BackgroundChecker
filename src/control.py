import praw
import pprint
from model import model
from view import view
from datetime import datetime

"""Control Class used in MVC Gui"""
class control():
    model1 = None
    view1 = None

    """
    Constructor for control object.
    @param reddit_api
        authenticated praw object
    """
    def __init__(self, reddit_api):
        self.model1 = model(reddit_api)
        self.view1 = view()
        self.view1.run()
        self.model1.set_username(self.view1.user_name)
        if len(self.model1.reddit_username) == 0:
            print "Application Terminated"
            exit(1)

    """
    Fetches reddit posts by self.model1.reddit_username and stores the list into {@code self.model1.reddit_post_list}.
    """
    def fetch_posts(self, username):
        self.model1.set_username(username)
        reddit_user = self.model1.reddit_api.redditor(username)
        self.model1.set_reddit_user(reddit_user)

        # grab all posts from user and store into reddit_post_list
        self.model1.reddit_post_list = reddit_user.comments.new(limit=None)

    """
    Print Posts out
    """
    def print_posts(self):
        with open('../data/index.html', 'w') as f:
            for post in self.model1.reddit_post_list:
                date = str(datetime.fromtimestamp(post.created_utc))
                post_url = post.link_url + post.id
                post_karma = str(post.score)
                f.write('<h3 style="color: #5e9ca0; display: inline;">' + 'username:&nbsp;&nbsp' +
                        self.model1.reddit_username + '&emsp;&emsp;</h3>\n')
                f.write('<h3 style="color: #5e9ca0; display: inline;">' + 'date:&nbsp&nbsp' + date + '&emsp;&emsp;' +
                        'karma:&nbsp&nbsp' + post_karma + '&emsp;</h3>\n')
                f.write('<p style="color: #5e9ca0; display: inline;"><a href="' + post_url + '"><img\n')
                f.write('src="https://cdn4.iconfinder.com/data/icons/web-links/512/41-512.png" alt="" '
                        'width="14" height="14" /></a></p>')
                f.write('<div class="md">\n')
                f.write(post.body_html.encode('utf-8') + '\n')
                f.write('</div>\n<hr />\n')

    """
    Investigates User by scraping reddit post data and writing information to file
    """
    def investigate_user(self):
        self.fetch_posts(self.model1.reddit_username)
        self.print_posts()

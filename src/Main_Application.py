from model import model
from control import control
import ConfigParser
import praw

"""
Ensures CLIENT_ID is unique, and not default value in config_template
@param CLIENT_ID
    String representing CLIENT_ID api key
@ensures CLIENT_ID is unique
"""
def ensure_valid_config(CLIENT_ID):
    """If No Api key info in config file: warn user"""
    if len(CLIENT_ID) == 0:
        print "You need to insert your own values in data/config.ini"
        exit()

"""
Reads API login information from config.ini (gitignored for security purposes. See data/config_template for template)
    and logs into reddit
@return reddit_api
    authenticated praw object
"""
def read_login_info():
    """ Read all login information from ../data/config.ini """
    config = ConfigParser.ConfigParser()
    config.read('../data/config.ini')
    client_id = config.get('API_INFO', 'id')
    client_secret = config.get('API_INFO', 'secret')
    password = config.get('API_INFO', 'password')
    user_agent = config.get('API_INFO', 'user_agent')
    username = config.get('API_INFO', 'username')

    """ If No Api key info in config file: warn user """
    ensure_valid_config(client_id)

    reddit_api = praw.Reddit(client_id=client_id, client_secret=client_secret,
                             password=password, user_agent=user_agent,
                             username=username)
    return reddit_api

"""Main Method"""
def main():
    reddit_api = read_login_info()
    control1 = control(reddit_api)
    control1.investigate_user()

if __name__ == '__main__':
    main()

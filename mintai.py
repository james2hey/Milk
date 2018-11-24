import praw
import random
from config import Config


def get_mintai():
    r = praw.Reddit(user_agent='Milk',
                    client_id=Config().r_id,
                    client_secret=Config().r_secret)

    sub = r.subreddit('FortNiteBR')
    posts = [post for post in sub.hot(limit=20)]
    random_post_number = random.randint(0, 20)
    random_post = posts[random_post_number]
    return random_post


import urllib2
import cookielib
import pickle
from urllib import urlencode

PASSWORD = "********"

def get_feed(url, cookie_pickle):
    cookie_jar = cookielib.CookieJar()
    for cookie in pickle.loads(cookie_pickle):
        cookie_jar.set_cookie(cookie)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
    feed = opener.open(url)
    feed_string = feed.read()
    feed.close()
    return feed_string

def get_cookies(url, formdata):
    cookie_jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
    feed = opener.open(url, formdata)
    feed.close()
    return pickle.dumps([c for c in cookie_jar])


pop_data = urlencode({'edit[name]': 'admin',
            'edit[pass]': PASSWORD,
            'op': 'Log in'
            })

login_url = 'http://www.southbend.peopleofpraise.org/user/login'
feed_url = 'http://www.southbend.peopleofpraise.org/node/feed'

# Get cookies
cookies = get_cookies(login_url, pop_data)
# Get feed
feed = get_feed(feed_url, cookies)

# For each feed, need: 
#  * login_url
#  * feed_url
#  * where to put un and pwd in form data

# Need to assemble cookie. Find login form. Then submit post with un/pwd.

# User types in page to login
# server grabs that page, alters form action (action = "/capture/?action=%s" % action)
# User types in info and submit.
# Server captures, then submits, either saving info or just saving cookie
# Server could also remember how to submit so we don't have to go through this process again.

#!/usr/bin/env python

import json
import twitter
# from tweetsql.database import Base, db_session, engine
# from tweetsql.model import Hashtag, Tweet, User, Word
# from sqlalchemy.exc import OperationalError
# from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

credentials = json.load(open('credentials.json'))

CONSUMER_KEY = credentials["api_key"]
CONSUMER_SECRET = credentials["api_secret"]

OAUTH_TOKEN = credentials["access_token"]
OAUTH_TOKEN_SECRET = credentials["token_secret"]

TRACK = 'lonely valentine'

twitter_auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twit_user = twitter.Twitter(auth=twitter_auth)

twitter_stream = twitter.TwitterStream(auth=twitter_auth)

statuses = twitter_stream.statuses.filter(track=TRACK)

for t in statuses:
    # print(t['text'])
    # print(t['id'])
    if (phrase != last_phrase)
        phrase = '@' + str(t['user']['screen_name']) + ' Lonely on Valentine\'s day? So are these folks: ' 
        print phrase
        last_phrase = phrase
        # twit_user.statuses.update(status=phrase)

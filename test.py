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
        phrase = '@' + str(t['user']['screen_name']) + 'Lonely on Valentine\'s day? So are these folks: ' 
        print phrase
        last_phrase = phrase
        # twit_user.statuses.update(status=phrase)

    # try:
    #     u = db_session.query(User).filter_by(uid=str(t['user']['id'])).one()
    # except NoResultFound:
    #     u = User(screen_name=t['user']['screen_name'], uid=t['user']['id'])
    #     db_session.add(u)
    #     db_session.commit()

    # tw = Tweet(tweet=t['text'], tid=t['id'], user_id=u.id, created_at=t['created_at'], data=json.dumps(t))

    # try:
    #     words = tw.tweet.split()
    #     for w in words:
    #         try:
    #             w_obj = db_session.query(Word).filter(Word.word == w).one()
    #         except MultipleResultsFound:
    #             pass
    #         except NoResultFound:
    #             w_obj = Word(word=w)
    #             db_session.add(w_obj)
    #             db_session.commit()
    #             tw.words.append(w_obj)
    #     db_session.add(tw)
    #     db_session.commit()
    # except OperationalError:
    #     db_session.rollback()

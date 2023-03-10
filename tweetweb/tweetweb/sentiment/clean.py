# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:01:33 2020

@author: aarus
"""


import re

def cleanTweet(tweet):

    # Remove Links, Special Characters etc from tweet
    tweet=re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)

    tweet=re.sub('RT','',tweet)
    tweet=' '.join(re.sub("@[\w]*"," ",tweet).split())
        
    tweet=' '.join(re.sub("([^a-zA-Z0-9#])"," ",tweet).split())
                             
    return tweet
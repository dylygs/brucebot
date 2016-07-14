#!/usr/bin/python
import tweepy, sys, time, random, os

KEYFILE = "keys.txt"
SONGS_PATH = "songs"

# open file with oauth keys & store them
def authenticate():
    keyfile = open(KEYFILE, "r")

    CONSUMER_KEY = str.strip(keyfile.readline())
    CONSUMER_SECRET = str.strip(keyfile.readline())
    ACCESS_TOKEN = str.strip(keyfile.readline())
    ACCESS_TOKEN_SECRET = str.strip(keyfile.readline())

    keyfile.close()

# authenticate tweepy & setip api
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

# take the song files & pick a random one
def getRandomFile():
    files = os.listdir(SONGS_PATH)
    randomFileInt = random.randint(0, len(files) - 1)
    return files[randomFileInt]

# get random line from file
def getRandomLine():
    randomLine = ""
    songFileStr = SONGS_PATH + "/" + getRandomFile()
    songFile = open(songFileStr, "r")
    randomLineInt = random.randint(0, amountOfLines(songFileStr) - 1)

    for i, line in enumerate(songFile):
        if i == randomLineInt:
            randomLine = line
            break

    return str.strip(randomLine)

# get amount of lines in file
def amountOfLines(songFile):
    length = 1
    with open(songFile) as f:
        length = sum(1 for _ in f)
    return length
        

# get my account and do stuff with it for testing
def doStuff(api):
#    me = api.me()
#    print(str(me.id) + " " + me.screen_name)
    print(getRandomLine())

api = authenticate()
doStuff(api)

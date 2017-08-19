import praw
import config
import time
import random
import os
import requests
import re
import wikipedia

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "HyperBotS v1.0")
	print "Logging in as %s..." % (config.username)
	
	print "Logged in!"
	
	return r


def run_bot(r, replcomm):

	print "Obtaining 20 comments..."

	#Hypercharged
	for comment in r.subreddit('AskReddit').comments(limit=20):
		
		if "Who is" in comment.body and comment.id not in replcomm and comment.author != r.user.me():
			with open ("replcomm2.txt", "a") as f:
				f.write(comment.id + "\n")
			stringV = comment.body
			returnV = re.sub(r'.*Who', 'Who', stringV)
			
			returnV = returnV.replace("Who is ","",1)
			returnV = returnV.replace("?","",1)
			wikipedia.set_lang("en")
			TLDR = wikipedia.summary(returnV, sentences=1)
			returnS = "https://en.wikipedia.org/wiki/%s" % (returnV)
			comment.reply("**%s:**\n>[%s's Wikipedia Page](%s)\n>**TL;DR: **%s" % (returnV, returnV, returnS, TLDR))
			
			print "Replied to comment " + comment.id
			replcomm.append(comment.id)
		
			
	
	print "Sleeping for 10 seconds..."
	#Sleep for 10 seconds...
	time.sleep(10)

def get_saved_comments():
	if not os.path.isfile("replcomm2.txt"):
		replcomm = []
	else:
		with open("replcomm2.txt", "r") as f:
			replcomm = f.read()
			replcomm = replcomm.split("\n")
			replcomm = filter(None, replcomm)

	return replcomm

r = bot_login()
replcomm = get_saved_comments()
while True:
	run_bot(r, replcomm)
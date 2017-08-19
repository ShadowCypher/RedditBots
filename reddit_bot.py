import praw
import config
import time
import random
import os
import requests


def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "HyperBotS v1.0")
	print "Logging in as %s..." % (config.username)
	
	print "Logged in!"
	
	return r


def runb(r, replcomm):

	print "Obtaining 30 comments..."

	#Hypercharged
	for comment in r.subreddit('Hypercharged').comments(limit=30):
		if "Hypercharged" in comment.body and comment.id not in replcomm and comment.author != r.user.me():
			with open ("replcomm.txt", "a") as f:
				f.write(comment.id + "\n")
			print "String with \"Hypercharged\" found in comment " + comment.id
			comment.reply("**Hypercharged** is a great channel with more than 100 subscribers! \n Their instagram page can be found here: \n > [Instagram](https://www.instagram.com/hyperchargedvideos/)")
			print "Replied to comment " + comment.id
			replcomm.append(comment.id)

		if "Who is" in comment.body and comment.id not in replcomm and comment.author != r.user.me():
			with open ("replcomm.txt", "a") as f:
				f.write(comment.id + "\n")
			stringV = comment.body.replace("Who is ","",1)
			stringV = "https://en.wikipedia.org/wiki/%s" % (stringV)
		
	else:
		print "Duplicate found!"	
	#Funny
	rand = random.randint(1,6)

	for comment in r.subreddit('Funny').comments(limit=2):

		if "Haha" or "lmao" or "that's funny" or "hehe" or "lololol" in comment.body and comment.id not in replcomm and comment.author != r.user.me():
			with open ("replcomm.txt", "a") as f:
				f.write(comment.id + "\n")
			if rand == 1:
				comment.reply("Haha! If I didn't add to the laughing mood, \nI'm sorry.")
			if rand == 2:
				comment.reply("LOL! If I didn't add to the laughing mood, \nI'm sorry.")
			if rand == 3:
				comment.reply("LMAO! If I didn't add to the laughing mood, \nI'm sorry.")
			if rand == 4:
				comment.reply("Hahahahahah! If I didn't add to the laughing mood, \nI'm sorry.")
			else:
				comment.reply("LOLOLOLOL! If I didn't add to the laughing mood, \nI'm sorry.")
	
			print "Replied to comment " + comment.id
			replcomm.append(comment.id)
	else:
		print "Duplicate found!"

	print "Sleeping for 10 seconds..."
	#Sleep for 10 seconds...
	time.sleep(10)

def get_saved_comments():
	if not os.path.isfile("replcomm.txt"):
		replcomm = []
	else:
		with open("replcomm.txt", "r") as f:
			replcomm = f.read()
			replcomm = replcomm.split("\n")
			replcomm = filter(None, replcomm)

	return replcomm

r = bot_login()
replcomm = get_saved_comments()
while True:
	runb(r, replcomm)

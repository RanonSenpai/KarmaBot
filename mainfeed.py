import praw

# reddit = praw.Reddit(client_id="tpOt927_JHB-PA",
# 					 client_secret="d4VA65AlqNtVev3TxIGhKuqhrIg",
# 					 username="RanonS",
# 					 password="1234qazw0987",
# 					 user_agent="KarmaBot by /u/RanonS")

reddit = praw.Reddit(client_id="cIPXWVlMAx5W3g",
					 client_secret="DGvA0oHtrx_vmna3ZcHwv69QVHU",
					 username="MikuYagami",
					 password="1234qazw0987",
					 user_agent="KarmaBot by /u/RanonS")

subreddit = reddit.subreddit("ZumBIDO")

def check_string_list(string, list_array):
	for filter in list_array:
		if filter in string:
			return True

def clear_inbox():
	message_subject = ""
	message_body = ""

	for item in reddit.inbox.unread():
		unread_message = item
		message_body = unread_message.body

		print("[*] Inbox : " + message_body)

		if(message_body != ""):
			unread_message.upvote()
			unread_message.reply("Upvoted again ^ _ ^ !")
			unread_message.mark_read()
			print("[+] Replied to the inbox")

last_submission_id = 0;

comments_filters = ["upvote",
					"upvotes",
					"please",
					"comment", 
					"karma",
					"plz",
					"pls",
					"help",
                    "upvoting"]

start = False
filters = False

print("[+] Bot Started")

while True:
	try :
		reddit_posts = subreddit.new(limit=1)
		account_posts = list(reddit.redditor('MikuYagami').submissions.new(limit=1))[0]

		for submissions in reddit_posts:
			if not submissions.stickied:
				if start == False:
					last_submission_id = submissions
					start = True

				if last_submission_id != submissions:
					last_submission_id = submissions
					
					print("[*] New Post : " + submissions.title)

					if filters == True:
						if check_string_list(submissions.title.lower(), comments_filters):
							if(account_posts != submissions):
								submissions.upvote()
								submissions.reply("Done, buddy ! upvote my comment too ^ _ ^")
								submissions.reply("Can you upvote my post too ? please . . . " + reddit.config.reddit_url + account_posts.permalink)
								print("[+] Replied : Done")
							else:
								print("[*] Sent by this account")
					else:
						if(account_posts != submissions):
							submissions.reply("Done, buddy ! upvote my comment too ^ _ ^")
							submissions.reply("Can you upvote my post too ? please . . . " + reddit.config.reddit_url + account_posts.permalink)
							submissions.upvote()
							print("[+] Replied : Done")
						else:
							print("[*] Sent by this account")

	except:
		continue

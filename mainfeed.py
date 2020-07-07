import praw

reddit = praw.Reddit(client_id="tpOt927_JHB-PA",
					 client_secret="d4VA65AlqNtVev3TxIGhKuqhrIg",
					 username="RanonS",
					 password="1234qazw0987",
					 user_agent="KarmaBot by /u/RanonS")

subreddit = reddit.subreddit("FreeKarma4U")

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
while True:
	try :
		reddit_posts = subreddit.new(limit=1)

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
							submissions.upvote()
							submissions.reply("Done, buddy ! upvote my comment too ^ _ ^")
							print("[+] Replied : Done")
					else:
						submissions.reply("Done, buddy ! upvote my comment too ^ _ ^")
						submissions.upvote()
						print("[+] Replied : Done")

	except:
		continue

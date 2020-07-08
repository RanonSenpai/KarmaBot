import praw

reddit = praw.Reddit(client_id="tpOt927_JHB-PA",
					 client_secret="d4VA65AlqNtVev3TxIGhKuqhrIg",
					 username="RanonS",
					 password="1234qazw0987",
					 user_agent="KarmaBot by /u/RanonS")

account_posts = reddit.redditor('RanonS').submissions.new(limit=1)

for submission in account_posts:
    submission.delete()
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

while True:
	account_posts = reddit.redditor('RanonS').comments.new(limit=1)

	for submission in account_posts:
		print("[+] Deleted Comment : " + submission.body)
		submission.delete()
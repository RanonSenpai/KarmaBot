import praw

account_username = "MikuYagami"
account_password = "1234qazw0987"
account_client_id = "cIPXWVlMAx5W3g"
account_client_secret = "DGvA0oHtrx_vmna3ZcHwv69QVHU"

# reddit = praw.Reddit(client_id="tpOt927_JHB-PA",
# 					 client_secret="d4VA65AlqNtVev3TxIGhKuqhrIg",
# 					 username="RanonS",
# 					 password="1234qazw0987",
# 					 user_agent="KarmaBot by /u/RanonS")

reddit = praw.Reddit(client_id=account_client_id,
					 client_secret=account_client_secret,
					 username=account_username,
					 password=account_password,
					 user_agent="KarmaBot by /u/RanonS")

while True:
	account_posts = reddit.redditor(account_username).comments.new(limit=1)

	for submission in account_posts:
		print("[+] Deleted Comment : " + submission.body)
		submission.delete()
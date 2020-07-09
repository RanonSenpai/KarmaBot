import praw
import time

account_username = "MikuYagami"
account_password = "1234qazw0987"
account_client_id = "cIPXWVlMAx5W3g"
account_client_secret = "DGvA0oHtrx_vmna3ZcHwv69QVHU"

sub_reddit = "ZumBIDO"

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

reddit.validate_on_submit = True

while True:
	print("[+] Posting a Post, It's 1 hour from last one.")
	try:
		reddit.subreddit(sub_reddit).submit(title="Upvote this Post and first 5 Comments ! I'll upvote all your posts ! ", url="https://i.kym-cdn.com/photos/images/newsfeed/001/531/312/328.png")
		time.sleep(3600)
	except:
		print("[-] 10 minute wait timer")
		time.sleep(600)
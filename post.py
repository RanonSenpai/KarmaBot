import praw

reddit = praw.Reddit(client_id="tpOt927_JHB-PA",
					 client_secret="d4VA65AlqNtVev3TxIGhKuqhrIg",
					 username="RanonS",
					 password="1234qazw0987",
					 user_agent="KarmaBot by /u/RanonS")

reddit.validate_on_submit = True

reddit.subreddit("ZumBIDO").submit(title="bot_test", url="https://i.kym-cdn.com/photos/images/newsfeed/001/531/312/328.png")
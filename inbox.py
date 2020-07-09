import praw
from praw.models import Message

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

while True:
	try:
		clear_inbox()
	except:
		continue

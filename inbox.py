import praw
from praw.models import Message

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
		print("[-] Error : Try in 10min")
		continue

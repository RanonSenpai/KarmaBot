import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import praw

account_username = "RanonS"
account_password = "1234qazw0987"
account_client_id = "cIPXWVlMAx5W3g"
account_client_secret = "DGvA0oHtrx_vmna3ZcHwv69QVHU"

reddit = praw.Reddit(client_id="tpOt927_JHB-PA",
					 client_secret="d4VA65AlqNtVev3TxIGhKuqhrIg",
					 username="RanonS",
					 password="1234qazw0987",
					 user_agent="KarmaBot by /u/RanonS")

# # reddit = praw.Reddit(client_id=account_client_id,
# # 					 client_secret=account_client_secret,
# # 					 username=account_username,
# # 					 password=account_password,
# # 					 user_agent="KarmaBot by /u/RanonS")

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)

# xs1 = []
# ys1 = []

# ax2 = fig.add_subplot(1,1,1)

# xs2 = []
# ys2 = []

# def animate(i):
#     xs1.append(i)
#     ys1.append(reddit.redditor(account_username).comment_karma)
#     ax1.clear()
#     ax1.plot(xs1, ys1)
#     xs2.append(i)
#     ys2.append(reddit.redditor(account_username).link_karma)
#     ax2.clear()
#     ax2.plot(xs2, ys2)

# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')

comment_karma_x = []
comment_karma_y = []

link_karma_x = []
link_karma_y = []

def animate(i):
    comment_karma_x.append(i)
    comment_karma_y.append(reddit.redditor(account_username).comment_karma)

    link_karma_x.append(i)
    link_karma_y.append(reddit.redditor(account_username).link_karma)

    axs[0].plot(comment_karma_x, comment_karma_y)

ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()
# pip install praw

import praw

reddit = praw.Reddit(
    client_id="RFV4JD4o7WaMmg",
    client_secret="ONq60_EDhK-FFUY80taWKxnzdBNcZQ",
    password="5Yfu>g86VVMK]ma?mb&X",
    user_agent="wsb_bot",
    username="unisg_wsb_bot",
)

print(reddit.user.me())

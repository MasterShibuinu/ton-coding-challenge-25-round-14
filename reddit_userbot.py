import praw
import time

reddit = praw.Reddit(
    client_id="id",
    client_secret="secret",
    user_agent="userbot",
    username="username",
    password="password"
)

subreddit = reddit.subreddit("test")

for comment in subreddit.stream.comments(skip_existing=True):
    if "ping" in comment.body.lower():
        comment.reply("pong")
        print("Ответил pong!")

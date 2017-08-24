import praw
import time
import config

r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "singsing bot - v1")
def bot():
    subreddit = r.subreddit("DotA2")
    for submission in subreddit.new(limit=25):
        n = "0"
        if "SingSing" in submission.title or "singsing" in submission.title:
            for comment in submission.comments:
                if comment.author == "singsong-fan-bot":
                    n = "500"
            if(n != '500'):
                submission.reply("Did you know singsing was the highest mmr on the leaderboard when mmr was not announced ? Tobi said when he went to valve HQ he got a glimpse of the mmr leaderboard and singsing was at the top")
    
    time.sleep(60)
    bot()

    
bot()

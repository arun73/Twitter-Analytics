import sqlite3


def get_tweets():
    conn = sqlite3.connect("tweets.db")
    c = conn.cursor()
    conn.text_factory = str
    c.execute("SELECT tweet FROM ces_tweets")
    _tweets = [r[0] for r in c.fetchall()]
    conn.close()
    return _tweets

tweets = get_tweets()
print tweets[0]

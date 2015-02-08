import sqlite3

conn = sqlite3.connect('tweets.db')
conn.text_factory = str
c = conn.cursor()

ces_tweets_file = 'ces.txt'


# Create SQLite DB to store CES Tweets
c.execute('CREATE TABLE ces_tweets (tweet TEXT)')
conn.commit()

# Add all CES tweets to sqlite DB
with open('ces.txt', 'r') as f:
	for line in f:
		if ((line == '\n') or (len(line) <= 30)):
			continue
		else:
			tweet = line
			# words = [word for word in line.split() if not (str.startswith(word, '@'))]
			# tweet = ' '.join(words)
			# print('')
			# print(tweet)
			# print('')
			c.execute("INSERT INTO ces_tweets VALUES(?)", [tweet])		
	conn.commit()

conn.close()
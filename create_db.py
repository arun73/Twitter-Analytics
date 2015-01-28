import csv
import sqlite3
import time


conn = sqlite3.connect('tweets.db')
neg_tweets_csv_file = 'Neg-tweets.csv'
pos_tweets_csv_file = 'Pos-tweets.csv'
conn.text_factory = str
c = conn.cursor()


def createTweetsTable():
	c.execute('CREATE TABLE training_data (tweet TEXT, sentiment TEXT)')
	conn.commit()


def addNegTweets():
	with open(neg_tweets_csv_file, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			c.execute("INSERT INTO training_data VALUES(?, ?)", [row[5], 'N'])
	conn.commit()


def addPosTweets():
	with open(pos_tweets_csv_file, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			c.execute("INSERT INTO training_data VALUES(?, ?)", [row[0], 'P'])
	conn.commit()

def main():
	createTweetsTable()
	addNegTweets()
	addPosTweets()

main()
conn.close()
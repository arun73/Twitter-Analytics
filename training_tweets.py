import re
import sqlite3
import time
import nltk
import pprint

conn = sqlite3.connect('tweets-analytics.db')
conn.text_factory = str
c = conn.cursor()
pp = pprint.PrettyPrinter(indent=4)

# tag set needs to updated 
tag_set = set(['JJ', 'RB', 'RBR', 'RBS'])

test_tweets = [
    (['feel', 'happy', 'this', 'morning'], 'P'),
    (['larry', 'friend'], 'P'),
    (['not', 'like', 'that', 'man'], 'N'),
    (['house', 'not', 'great'], 'N'),
    (['your', 'song', 'annoying'], 'N')]

def getAllTweets():
	tweets = []
	for row in c.execute('SELECT * FROM training_data LIMIT 1000'):
		tweets.append(row)
		#time.sleep(10)
	return tweets


def getWordsInTweets(tweets):
	wordList = []
	for (words, sentiment) in tweets:
		wordList = wordList + words
	# pp.pprint(wordList)
	return wordList


def getWordFeatures(wordList):
	wordList = nltk.FreqDist(wordList)
	word_features = wordList.keys()
	pp.pprint(wordList)
	return word_features


def main():
	tweets_data = getAllTweets()
	tweets = []

	# Laurent Luce
	# for (words, sentiment) in tweets_data:
	# 	words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
	# 	tweets.append((words_filtered, sentiment))

	for (tweet, sentiment) in tweets_data:
		tokenized = nltk.word_tokenize(tweet)
		tagged = nltk.pos_tag(tokenized)
		word_list = [word for (word, tag) in tagged if tag in tag_set]

		print 'Tweet:\n', tweet, '\n'
		print 'Tagged:\n', str(tagged), '\n'
		print word_list
		print '\n\n'

		time.sleep(5)

	word_features = getWordFeatures(getWordsInTweets(tweets))


main()
conn.close()
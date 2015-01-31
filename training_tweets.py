import re
import sqlite3
import time
import nltk
import pprint

conn = sqlite3.connect('tweets.db')
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
	for row in c.execute('SELECT * FROM training_data LIMIT 1600000'):
		tweets.append(row)
		#time.sleep(10)
	return tweets


def getWordsInTweets(tweets):
	wordList = []
	for (words, sentiment) in tweets:
		wordList.extend(words);
	# pp.pprint(wordList)
	return wordList


def getWordFeatures(wordList):
	wordList = nltk.FreqDist(wordList)
	word_features = wordList.keys()
	print wordList.most_common(1000)
	#pp.pprint(wordList)
	return word_features


#def main():
tweets_data = getAllTweets()
tweets = []
conn.close()
# Laurent Luce
for (words, sentiment) in tweets_data:
 	words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
 	tweets.append((words_filtered, sentiment))

	#for (tweet, sentiment) in tweets_data:
	#	tokenized = nltk.word_tokenize(tweet.decode('utf-8'))
	#	tagged = nltk.pos_tag(tokenized)
	#	word_list = [word for (word, tag) in tagged if tag in tag_set]
	#	tweets.append((word_list, sentiment))
		# print 'Tweet:\n', tweet, '\n'
		# print 'Tagged:\n', str(tagged), '\n'
		# print word_list
		# print '\n\n'

		# time.sleep(5)

print len(tweets);

word_features = getWordFeatures(getWordsInTweets(tweets))







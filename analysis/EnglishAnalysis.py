#!/usr/bin/env python3

def matchesTrigram(text, trigram):
	if len(text) != 3 or len(trigram) != 3:
		return False

	trigram = trigram.lower()
	text = text.lower()

	remainingSpaces = 0
	index = 0
	for c in text:
		if c == ' ' and remainingSpaces > 0:
			remainingSpaces -= 1;
		elif c != trigram[index]:
			return False
		index += 1
	return True

def matchTrigramsInText(text):
	trigrams = [
	'the', 'and', 'tha', 'ent',
	'ing', 'ion', 'tio', 'for',
	'nde', 'has', 'nce', 'edt',
	'tis', 'oft', 'sth', 'men'
	]

	trigramCount = 1

	for i in range(0, len(text) - 2):
		threeCharText = text[i:i+3]
		for trigram in trigrams:
			if matchesTrigram(threeCharText, trigram):
				trigramCount += 1
	return trigramCount

def matchesBigram(text, bigram):
	if len(text) != 2 or len(bigram) != 2:
		return False

	bigram = bigram.lower()
	text = text.lower()
	return bigram == text


def matchBigramsInText(text):
	bigrams = [
	'th','he','in','er','an',
	're','nd','on','en','at',
	'ou','ed','ha','to','or',
	'it','is','hi','es','ng'
	]

	bigramCount = 0

	for i in range(0, len(text) - 1):
		twoCharText = text[i:i+2]
		for bigram in bigrams:
			if matchesBigram(twoCharText, bigram):
				bigramCount += 1
	return bigramCount

def englishRank(text):
	return float((matchBigramsInText(text) + matchTrigramsInText(text))) / float(len(text))

def sortByEnglishRank(array):
	import analysis
	def keyFunc(line):
		return -analysis.englishRank(line)
	return sorted(array, key=keyFunc)
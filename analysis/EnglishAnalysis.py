#!/usr/bin/env python3

import math
from scipy import stats

def getLetterFreqDict():
	# Percentage of letters in the english language
	letter_freq = {
		'a': 0.08167,
		'b': 0.01492,
		'c': 0.02782,
		'd': 0.04253,
		'e': 0.12702,
		'f': 0.02228,
		'g': 0.02015,
		'h': 0.06094,
		'i': 0.06966,
		'j': 0.00153,
		'k': 0.00772,
		'l': 0.04025,
		'm': 0.02406,
		'n': 0.06749,
		'o': 0.07507,
		'p': 0.01929,
		'q': 0.00095,
		'r': 0.05987,
		's': 0.06327,
		't': 0.09056,
		'u': 0.02758,
		'v': 0.00978,
		'w': 0.02361,
		'x': 0.00150,
		'y': 0.01974,
		'z': 0.00074
	}

	return letter_freq

def getEmptyLetterDict():
	empty = {
			'a': 0,
			'b': 0,
			'c': 0,
			'd': 0,
			'e': 0,
			'f': 0,
			'g': 0,
			'h': 0,
			'i': 0,
			'j': 0,
			'k': 0,
			'l': 0,
			'm': 0,
			'n': 0,
			'o': 0,
			'p': 0,
			'q': 0,
			'r': 0,
			's': 0,
			't': 0,
			'u': 0,
			'v': 0,
			'w': 0,
			'x': 0,
			'y': 0,
			'z': 0
		}

	return empty


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


# Will preserve capitilization
def stripNonAlphaChars(text):
	out = ''
	for char in text:
		charNum = ord(char)
		if (charNum >= ord('a') and charNum <= ord('z')) or (charNum >= ord('A') and charNum <= ord('Z')):
			out += char
	return out

def getLetterFreq(text):
	assert isinstance(text, str)
	text = text.lower()
	text = stripNonAlphaChars(text)

	observed_letter_count = getEmptyLetterDict()

	for char in text:
		if ord(char) >= ord('a') and ord(char) <= ord('z'):
			observed_letter_count[char] += float(1)

	return observed_letter_count

def getExpectedLetterFreq(textlength):
	assert isinstance(textlength, int) and textlength >= 0

	expected_letter_count = getEmptyLetterDict()
	letter_freq = getLetterFreqDict()

	for key in expected_letter_count:
		expected_letter_count[key] = float(textlength) * letter_freq[key]

	return expected_letter_count

def letterDictToArrayCounts(letter_dict):
	dict_arr = list(letter_dict.items())

	def sortFunc(item):
		return item[0]

	sorted_dict_arr = sorted(dict_arr, key=sortFunc)

	result_arr = []
	for i in range(0, len(sorted_dict_arr)):
		result_arr.append(sorted_dict_arr[i][1])
	return result_arr

def letterDictToArrayLetters(letter_dict):
	dict_arr = list(letter_dict.items())

	def sortFunc(item):
		return item[1]

	sorted_dict_arr = sorted(dict_arr, key=sortFunc, reverse=True)

	result_arr = []
	for i in range(0, len(sorted_dict_arr)):
		result_arr.append(sorted_dict_arr[i][0])
	return result_arr

# A greater p-value means stronger likleyhood that the freqency matches english
def chiSquaredTestPVal(text):
	assert isinstance(text, str)
	assert len(text) > 0


	actualFreq = getLetterFreq(text)
	expectedFreq = getExpectedLetterFreq(len(text))


	actualFreqListArr = letterDictToArrayCounts(actualFreq)
	expectedFreqListArr = letterDictToArrayCounts(expectedFreq)

	return stats.chisquare(actualFreqListArr, f_exp=expectedFreqListArr).pvalue

def simpleEnglishFrequencyScore(text, selection_length=6):
	assert isinstance(text, str)
	assert isinstance(selection_length, int)
	assert selection_length > 0 and selection_length < 13

	text = text.lower()
	text = stripNonAlphaChars(text)

	# The english letters ordered by frequency
	ordered_chars = [
		'e', 't', 'a', 'o', 'i', 'n', 's',
		'h', 'r', 'd', 'l', 'u', 'c', 'm',
		'f', 'w', 'g', 'y', 'p', 'b', 'v',
		'k', 'x', 'j', 'q', 'z'
	]

	first_chars = ordered_chars[0:selection_length]
	last_chars = ordered_chars[-selection_length:]
	freq_dict = getLetterFreq(text)
	actual_freq = letterDictToArrayLetters(freq_dict)

	actual_first_chars = actual_freq[0:selection_length]
	actual_last_chars = actual_freq[-selection_length:]

	score = 0

	for char in actual_first_chars:
		if char in first_chars:
			score += 1

	for char in actual_last_chars:
		if char in last_chars:
			score += 1

	return score


# Score will be 100 if non alphabetic characters are detected
# Score will always be positive and a score closer to 0 is better
def englishLetterFreqAnalysisByPercent(text):
	assert isinstance(text, str)

	text = text.lower()
	text = stripNonAlphaChars(text)

	# Percentage of letters in the english language
	letter_freq = getLetterFreq()

	observed_letter_count = getEmptyLetterDict()

	observed_letter_percent = getEmptyLetterDict()

	for char in text:
		if ord(char) >= ord('a') and ord(char) <= ord('z'):
			observed_letter_count[char] += 1
		else:
			return 100

	for key,value in observed_letter_count.items():
		observed_letter_percent[key] = float(value) / float(len(text))

	error = 0
	for key, value in observed_letter_percent.items():
		error += math.fabs(value - letter_freq[key])

	return error
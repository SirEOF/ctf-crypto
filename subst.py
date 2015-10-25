#!/usr/bin/python

import base64

def getLetterWithOffset(offset, letter):
	letterNum = ord(letter)
	if letterNum <= ord('z') and letterNum >= ord('a'):
		letterNum += offset
		while letterNum > ord('z'):
			letterNum -= 26
		return chr(letterNum)
	elif letterNum <= ord('Z') and letterNum >= ord('A'):
		letterNum += offset
		while letterNum > ord('Z'):
			letterNum -= 26
		return chr(letterNum)
	else:
		return letter



def wordWithOffset(offset, word):
	out = ''
	for char in input:
		out += getLetterWithOffset(offset, char)
	return out

def reverseWordWithOffset(offset, word):
	return wordWithOffset(offset, word)[::-1]
	return wordWithOffset(offset, word)[::-1]

def calcRotations():
	out = []
	for offset in range(0,26):
		out.append(wordWithOffset(offset, input))
	return out;

def b64DecodeRotations():
	rotations = calcRotations()
	decoded = []
	for rotation in rotations:
		decoded.append(normalCharsOnly(base64.b64decode(rotation), ' '))

	return decoded

# Any unusal characters are turned into the unknownChar provided
def normalCharsOnly(text, unknownChar='*'):
	output = ''
	for c in text:
		char_num = ord(c)
		if char_num >= 32 and char_num <= 126:
			output += c
		else:
			output += unknownChar
	return output

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

def printRotations():
	rotations = calcRotations()
	offset = 0
	for rotation in rotations:
		print(str(offset) + ': ' + rotation)
		offset += 1

def printDecodedRotations():
	decoded = b64DecodeRotations()
	offset = 0
	for line in decoded:
		print(str(englishRank(line)) + ' - ' + str(offset) + ': ' + str(line))
		offset += 1

def sortByEnglishRank(array):
	def keyFunc(line):
		return -englishRank(line)
	return sorted(array, key=keyFunc)

def printArray(array):
	for line in array:
		print(line)
# Substitutes char in a string of text, based on entries defined in a python dicionary
def substitute(text, dictionary, unknownChar='*'):
	out = ''
	for char in text:
		charPrinted = False
		if(char == ' '):
			out += ' '
			continue
		for key, value in dictionary.items():
			if char == key:
				out += value
				charPrinted = True
				break
		if not(charPrinted):
			out += unknownChar
	return out

# If the pivot is encountered in the text it is replaced with a *
def flipAsciiOverPivot(text, pivot, offset, pivotChar='*'):
	out = ''
	for char in text:
		charNum = ord(char)
		if char == ' ':
			out += ' '
			continue
		elif charNum < pivot:
			out += chr(charNum + offset)
			continue
		elif charNum > pivot:
			out += chr(charNum - offset)
			continue
		else:
			out += pivotChar
	return out

# Uses a completley reversed alphabet to perform a substitution
def reverseAlphabetSubstitution(text):
	out = ''
	for char in text:
		charNum = ord(char)
		if char == ' ':
			out += ' '
			continue
		elif charNum >= ord('a') and charNum <= ord('z'):
			out += chr(ord('a') + (ord('z') - charNum))
		elif charNum >= ord('A') and charNum <= ord('Z'):
			out += chr(ord('A') + (ord('Z') - charNum))
	return out;
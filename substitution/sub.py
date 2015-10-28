#!/usr/bin/env python3

import base64
import util
from util import CipherInput
from util import CipherOutput
from util import CipherType
import operator

###########
# PRIVATE #
###########

def getLetterWithOffset(offset, letter):
	letterNum = ord(letter)
	if letterNum <= ord('z') and letterNum >= ord('a'):
		letterNum += offset
		while letterNum > ord('z'):
			letterNum -= 26
		while letterNum < ord('a'):
			letterNum += 26
		return chr(letterNum)
	elif letterNum <= ord('Z') and letterNum >= ord('A'):
		letterNum += offset
		while letterNum > ord('Z'):
			letterNum -= 26
		while letterNum < ord('A'):
			letterNum += 26
		return chr(letterNum)
	else:
		return letter



def wordWithOffset(offset, word):
	out = ''
	for char in word:
		out += getLetterWithOffset(offset, char)
	return out

def reverseWordWithOffset(offset, word):
	return wordWithOffset(offset, word)[::-1]

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

def vigenereDecryptWithKey(text, key):
	key = key.lower()
	keylen = len(key)

	keypos = 0


	out = ''
	for char in text:
		if char == ' ':
			out += ' '
			continue

		offset = (ord(key[keypos]) - ord('a'))
		out += getLetterWithOffset(-offset, char)

		#increment the key pos
		keypos += 1
		keypos %= keylen
	return out

# The second number in the touple is the number of instances of that offset found, the first is the offset
def findRepeatedSequenceOffsetsAndCounts(text):
	# Remove all spaces
	text = text.replace(' ', '')
	allSeq = []

	for i in range(0, len(text) - 3):
		allSeq.append([i, text[i:i+3]])
		allSeq.append([i, text[i:i+4]])

	lastStart = len(text) - 3
	allSeq.append([lastStart, text[lastStart:]])

	# Now all possible sequences of 3 and 4 chars are stored in allSeq

	def keyFunc(item):
		return item[1]

	# Sort it based on text contents, so that those that match are back to back
	sortedSeq = sorted(allSeq, key=keyFunc)

	matchDiffs = {}

	lastItem = None
	for item in sortedSeq:
		if lastItem is None:
			lastItem = item
			continue

		if lastItem[1] == item[1]:
			diff = item[0] - lastItem[0]
			if diff in matchDiffs:
				matchDiffs[diff] += 1
			else:
				matchDiffs[diff] = 1

		lastItem = item
	# END FOR

	matchDiffsAndFactors = dict(matchDiffs)
	for key, value in matchDiffs.items():
		# print(str(key) + ':'+ str(value))
		factors = util.factor(key)
		for factor in factors:
			if factor in matchDiffsAndFactors:
				matchDiffsAndFactors[factor] += value
			else:
				matchDiffsAndFactors[factor] = value

	return sorted(matchDiffsAndFactors.items(), key=operator.itemgetter(1), reverse=True)

def findRepeatedSequenceOffsets(text, threshold=None):
	assert threshold is None or threshold >= 1

	arr = findRepeatedSequenceOffsetsAndCounts(text)

	def getFirstElement(pair):
		return pair[0]

	rawList = list(map(getFirstElement, arr))
	if threshold is not None:
		def filterFunc(item):
			return item <= threshold
		return list(filter(filterFunc, rawList))
	else:
		return rawList


##########
# PUBLIC #
##########

def decryptRotation(cipher):
	assert isinstance(cipher, CipherInput)
	assert cipher.getCipherType().name == CipherType.cesar.name
	if cipher.getKey() is not None:
		assert cipher.getKey().isdigit()
		return [CipherOutput(cipher, wordWithOffset(int(cipher.getKey()), cipher.getInput()))]
	else:
		resultCiphers = []
		for offset in range(0,26):
			resultCiphers.append(CipherOutput(cipher, wordWithOffset(offset, cipher.getInput()), offset))
		return resultCiphers

def decryptB64(cipher):
	from base64 import b64decode
	assert isinstance(cipher, CipherInput)
	assert cipher.getCipherType().name == CipherType.base64.name
	return [CipherOutput(cipher, util.normalCharsOnly(base64.b64decode(cipher.getInput()), '.'))]


def decryptReverseAlphabet(cipher):
	assert isinstance(cipher, CipherInput)
	return [CipherOutput(cipher, reverseAlphabetSubstitution(cipher.getInput()))]

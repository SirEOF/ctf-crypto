#!/usr/bin/python

import base64

# input = "uozdovhhob zigrxfozgrmt slmvbyzwtvi"
input = "JedmRUT0sYMyReNlQOpdAYFqwPT0t2vqQPTgRPAyv2znAZvnueldRUTzvUTKsPRdueBztekyLYXat3BzvY9qsONrDaTPsYX0AYzzuqTrsYMyQeNdtaTcvOBaROIyQPE/"

# Range of 97 - 122
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

def normalCharsOnly(text, unknownChar):
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
	# dictionary = {}
	# ranks = []
	# for line in array:
	# 	rank = englishRank(line)
	# 	dictionary[line] = rank
	# 	ranks.append(rank)

def printArray(array):
	for line in array:
		print(line)

def substitute(text, dictionary):
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
			out += '*'
	return out

# If the pivot is encountered in the text it is replaced with a *
def flipAsciiOverPivot(text, pivot, offset):
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
			out += '*'
	return out




lines = [
	'x46>2? A@DE65 @? 9:D A286] a w@FCD p8@',
	's2:=J &A52E6i %96 DE@4< 6I492?86 92D 366? E2<6? 5@H? 2?5 H6 2C6 :? E96 AC@46DD @7 EC2?D76C:?8 2== 4C656?E:2=D E@ @FC D6CG6CD] x?7:=EC2E:@? @7 !~$x) 32?< :D 4@?E:?F:?8 2D A=2??65]',

	'$925@H $ECJ<6 A@DE65 2 ?6H 6IA=@:E c w@FCD p8@',
	'#@@E 4@?EC@= G:2 >@5048: 2?5 32D9] }@E6i ~C:8:?2= 7:I 7@C GF=?6C23:=:EJ 5@6D ?@E C6D@=G6 E96 AC@3=6>] tIA=@:E DE:== 24E:G6]',
	'`b s@H?=@25D',

	'_Istpsqttu  4@??64E65 H:E9 q=24<(`5@H  ] d w@FCD p8@',

	'$A6I  FA=@2565 2 ?6H 4@56D?:AA6E] d w@FCD p8@',
	'g \':6HD',
	]


dictionary= {
	'p': 'a',
	'8': 'g',
	'@': 'o',
	'w': 'h',
	'F': 'u',
	'C': 'r',
	'D': 's',
	's': 'D',
	'2': 'a',
	':': 'i',
	'=': 'l',
	'J': 'y',
	'%': 'T',
	'9': 'h',
	'6': 'e',
	'&': 'U',
	'A': 'p',
	'5': 'd',
	'2': 'a',
	'E': 't',
	'6': 'e',
	'i': ':',
	'4': 'c',
	'<': 'k',
	'3': 'b',
	'?': 'n',
	']': '.',
	'I': 'x',
	'x': 'I',
	'7': 'f',
	'H': 'w',
	'G': 'v',
	'}': 'N',
	'>': 'm',
	't': 'E',
	'#': 'R',
	'0': '_',
	'~': 'O',
	'$': 'S',
	'`': '1',
	'a': '2',
	'b': '3',
	'c': '4',
	'd': '5',
	'e': '6',
	'f': '7',
	'g': '8',
	'h': '9',
	'\'': 'V'
}

# print(substitute(text1, dictionary))
# print(flipAsciiOverPivot(conversation, 91, 47))
for line in lines:
	print(flipAsciiOverPivot(line, 91, 47))
	# print(substitute(line, dictionary))

# print(wordCrack(text5, 47, 47))

# print(ord('') - ord('2'))

# print(ord('p') - ord('a'))
# print(ord('8') - ord('g'))
# print(ord('@') - ord('o'))

# print(ord('w') - ord('h'))
# print(ord('@') - ord('o'))
# print(ord('F') - ord('u'))
# print(ord('C') - ord('r'))
# print(ord('D') - ord('s'))


# printArray(sortByEnglishRank(b64DecodeRotations()))
# printArray(sortByEnglishRank([
# 	'flawlessly articulating honeybadger',
# 	'flawlessly articulating doneypazger',
# 	'flawlessly articulating doneymaqger',
# 	'flawlessly articulating moneypazger',
# 	'flawlessly articulating doneymazger',
# 	'flawlessly articulating doneymavger',
# 	'flawlessly articulating honeypazger',
# 	'flawlessly articulating moneybadger',
# 	'flawlessly articulating doneymahger',
# 	'flawlessly articulating honeymaqger',
# 	'flawlessly articulating doneypaxger'
# 	]))

# print(matchesBigram('te', 'tee'))
# printDecodedRotations()


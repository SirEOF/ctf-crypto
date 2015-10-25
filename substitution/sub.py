
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

	# dictionary = {}
	# ranks = []
	# for line in array:
	# 	rank = englishRank(line)
	# 	dictionary[line] = rank
	# 	ranks.append(rank)


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


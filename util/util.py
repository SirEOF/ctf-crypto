#!/usr/bin/env python3

from enum import Enum
from math import sqrt

# Any unusal characters are turned into the unknownChar provided
def normalCharsOnly(text, unknownChar='*'):
	assert isinstance(unknownChar, str)
	assert isinstance(text, str) or isinstance(text, bytes)
	output = ''
	if isinstance(text, bytes):
		text = text.decode('utf-8', 'ignore')

	for c in text:
		char_num = ord(c)
		if char_num >= 32 and char_num <= 126:
			output += c
		else:
			output += unknownChar
	return output

# NOTE: This method will NOT return 1 and num as factors
def factor(num):
	assert isinstance(num, int)
	assert num >= 0

	lowerFactors = []
	for i in range(2, int(sqrt(num) + 1)):
		if num % i == 0:
			lowerFactors.append(i)
	allFactors = list(lowerFactors)
	for factor in lowerFactors:
		allFactors.append(int(num / factor))

	return sorted(set(allFactors))

class CipherType(Enum):
	cesar = 1
	reverse_alphabet = 2
	base64 = 3
	substitution = 4

class CipherInput:

	# cipherType should be of the enum type type CipherType
	def __init__(self, cipherType, inputText, key=None):
		assert isinstance(cipherType, CipherType)
		assert isinstance(inputText, str)
		assert key is None or isinstance(key, int) or isinstance(key, string)

		self.cipherType = cipherType
		self.input = str(inputText)
		self.key = str(key) if key is not None else None

	def getCipherType(self):
		return self.cipherType

	def getKey(self):
		return self.key

	def getInput(self):
		return self.input

	# Leave no key for a cesar cipher to try all possibilities or specify a number for a single rotation
	def decrypt(self):
		from substitution import decryptRotation
		from substitution import decryptB64
		from substitution import decryptReverseAlphabet

		# All methods should accept only a CipherInput as their only parameter
		# and return a list of CipherOutputs.
		#
		# The string name that corresponds to the method must match the enum type
		methods = {
			'cesar': decryptRotation,
			'base64': decryptB64,
			'reverse_alphabet': decryptReverseAlphabet
		}

		return methods[self.getCipherType().name](self)

	# toString method
	def __str__(self):
		out = 'Cipher: ' + self.getCipherType().name + '\n'
		out += 'Key: ' + str(self.getKey()) + '\n'
		out += 'Input: ' + self.getInput() + '\n'
		return out

class CipherOutput:
	def __init__(self, cipherInput, result, key=None):
		assert isinstance(cipherInput, CipherInput)
		assert isinstance(result, str)
		assert key is None or isinstance(key, int) or isinstance(key, string)

		self.cipherType = cipherInput.getCipherType()
		self.input = cipherInput.getInput()
		self.result = str(result)
		self.key = str(key) if key is not None else cipherInput.getKey()

	def generateCipherInput(self, newCipherType, newKey=None):
		assert isinstance(newCipherType, CipherType)
		assert newKey is None or isinstance(key, int) or isinstance(key, string)

		return CipherInput(newCipherType, self.result, str(newKey) if newKey is not None else None)

	def getCipherType(self):
		return self.cipherType

	def getKey(self):
		return self.key

	def getInput(self):
		return self.input

	def getResult(self):
		return self.result

	def __str__(self):
		out = ''
		out += 'Cipher: ' + self.getCipherType().name + '\n'
		out += 'Key: ' + str(self.getKey()) + '\n'
		out += 'Input: ' + self.getInput() + '\n'
		out += 'Result: ' + self.getResult() + '\n'
		return out


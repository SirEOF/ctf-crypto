def printArray(array):
	for line in array:
		print(line)

def sortByEnglishRank(array):
	import analysis
	def keyFunc(line):
		return -analysis.englishRank(line)
	return sorted(array, key=keyFunc)

if __name__ == '__main__':
	import substitution
	printArray(sortByEnglishRank(substitution.b64DecodeRotations()))
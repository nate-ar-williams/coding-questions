#!/usr/bin/python3

totalCounts = 0

def getMatches(n, A, start, end):
	matches = 0
	for i in range(start, end + 1):
		if A[i] == n:
			matches += 1
	global totalCounts
	totalCounts += end - start + 1
	return matches

def majorityElement(A, me, count, start, end):
	if start == end:
		global totalCounts
		totalCounts += 1
		return A[end], 1

	endOfFirst = (start + end) // 2
	startOfSecond = endOfFirst + 1

	firstCandidate, firstCount = majorityElement(A, me, count, start, endOfFirst)
	secondCandidate, secondCount = majorityElement(A, me, count, startOfSecond, end)

	if firstCandidate == secondCandidate:
		return firstCandidate, firstCount + secondCount

	if firstCandidate != -1:
		# check second array for number of matches
		numMatches = getMatches(firstCandidate, A, startOfSecond, end) + firstCount
		if numMatches > (end + 1 - start) // 2:
			return firstCandidate, numMatches

	if secondCandidate != -1:
		numMatches = getMatches(secondCandidate, A, start, endOfFirst) + secondCount
		if numMatches > (end + 1 - start) // 2:
			return secondCandidate, numMatches
	
	# otherwise no majorityElement
	return -1, 0

def getMajorityElement(A):
	global totalCounts
	totalCounts = 0
	return majorityElement(A, -1, 0, 0, len(A) - 1)

def getMostTouchingestElement(A):
	maxHomogenousElement, maxHomogenousLength = 0, 0
	currentHomogenousElement, currentHomogenousLength = A[0], 1


	for i in range(1, len(A)):
		if A[i] == currentHomogenousElement:
			currentHomogenousLength += 1
			if currentHomogenousLength > maxHomogenousLength:
				maxHomogenousLength = currentHomogenousLength
				maxHomogenousElement = currentHomogenousElement

		else:
			currentHomogenousElement = A[i]
			currentHomogenousLength = 1

	print('max ele=' + str(maxHomogenousElement))
	print('max len=' + str(maxHomogenousLength))

def getME(A):
	lastME = -1
	currentME = -1
	currentMECount = 0
	currentMEStart = 0
	currentMELen = 0

	i = 0
	length = len(A)
	while True:

		# no current majority element
		if currentME == -1:
			currentME = A[i]
			currentMELen = 1
			currentMECount = 1
			currentMEStart = i

		# matches current majority element
		elif A[i] == currentME:
			currentMECount += 1
			currentMELen += 1

		# does not match current majority element
		else:
			# no longer a majority element
			if currentMELen > currentMECount * 2:
				currentME = -1

			# still a valid majority element
			else:
				currentMELen += 1

		if currentMELen * 2 > length:
			return currentME

		# wraparound
		if i == length - 1:
			i = 0
		else:
			i += 1


		# break if we've looped around to start
		if i == currentMEStart:
			if lastME == -1:
				if currentME == -1:
					return -1
				lastME = currentME
				currentME = -1
			else:
				return -1


def main():
	pass

if __name__ == '__main__':
	main()

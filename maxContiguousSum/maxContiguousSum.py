#!/usr/bin/python3

import sys

# let a be an array of ints
def maxContiguousSum(a):
	# set maxSum to be lil value
	maxSum = -sys.maxsize

	startOfSequence = endOfSequence = 0

	length = len(a)
	currentSum = a[startOfSequence]

	while endOfSequence < length:
		if currentSum > maxSum:
			maxSum = currentSum

		currentValue = a[endOfSequence]
		if startOfSequence == endOfSequence:
			currentSum = currentValue
			endOfSequence += 1
			#print('new cursum: ' + str(currentSum))
			if currentSum < 0:
				startOfSequence = endOfSequence

		elif currentSum + currentValue > 0:
			currentSum += currentValue
			#print('increased cursum: ' + str(currentSum))
			endOfSequence += 1

		else:
			#print('done with cursum: ' + str(currentSum))
			startOfSequence = endOfSequence
			currentSum = -sys.maxsize

	if currentSum > maxSum:
		maxSum = currentSum

	return maxSum


def main():
	testCase1 = [2, -1, 2]
	expectedResult = 3
	result = maxContiguousSum(testCase1)
	if result != expectedResult:
		print('testCase1 failed. returned {}, expected {}'.format(result, expectedResult))
	else:
		print('testCase1 passed')

	testCase2 = [0, -1, -2]
	expectedResult = 0
	result = maxContiguousSum(testCase2)
	if result != expectedResult:
		print('testCase2 failed. returned {}, expected {}'.format(result, expectedResult))
	else:
		print('testCase2 passed')

	testCase3 = [-2, -1, 0]
	expectedResult = 0
	result = maxContiguousSum(testCase3)
	if result != expectedResult:
		print('testCase3 failed. returned {}, expected {}'.format(result, expectedResult))
	else:
		print('testCase3 passed')

	testCase4 = [1, 2, 3]
	expectedResult = 6
	result = maxContiguousSum(testCase4)
	if result != expectedResult:
		print('testCase4 failed. returned {}, expected {}'.format(result, expectedResult))
	else:
		print('testCase4 passed')

	testCase5 = [3, 2, 1]
	expectedResult = 6
	result = maxContiguousSum(testCase5)
	if result != expectedResult:
		print('testCase5 failed. returned {}, expected {}'.format(result, expectedResult))
	else:
		print('testCase5 passed')

	testCase6 = [1, -2, 3]
	expectedResult = 3
	result = maxContiguousSum(testCase6)
	if result != expectedResult:
		print('testCase6 failed. returned {}, expected {}'.format(result, expectedResult))
	else:
		print('testCase6 passed')

	testCase7 = [1, -2, 0]
	expectedResult = 1
	result = maxContiguousSum(testCase7)
	if result != expectedResult:
		print('testCase7 failed. returned {}, expected {}'.format(result, expectedResult))
	else:
		print('testCase7 passed')

	testCase8 = [-1, 1, -1]
	expectedResult = 1
	result = maxContiguousSum(testCase8)
	if result != expectedResult:
		print('testCase8 failed. returned {}, expected {}'.format(result, expectedResult))
	else:
		print('testCase8 passed')

if __name__ == '__main__':
	main()

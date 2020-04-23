#!/usr/bin/python3

import string

# let A be list of nums and letters
def findLongestBalancedSubarray(A):

	# cb is current balance. it always starts at 0
	cb = 0

	# define an empty list to be smallest possible length
	maxLength = 0

	# startPoint of largest balanced subarray 
	maxStartPoint = 0

	# endpoint of largest balanced subarray 
	maxEndpoint = 0

	length = len(A)

	# pbs is non-negative balances
	pbs = [0]

	# nbs is negative balances
	nbs = [0]
	
	for i in range(length):
		if A[i] in string.digits:
			cb += 1	
		else:
			cb -= 1

		balances = pbs
		absoluteBalance = abs(cb)
		if cb < 0:
			balances = nbs

		# we don't have a start point for this balance
		if len(balances) <= absoluteBalance:
				balances += [i + 1]
		else:
			subarrayLength = i - balances[absoluteBalance]
			if subarrayLength > maxLength:
				maxLength = subarrayLength
				maxEndpoint = i
				maxStartPoint = balances[absoluteBalance]

	return A[maxStartPoint : maxEndpoint + 1]

def test(name, expected, result):
	if expected == result:
		print('test {} passed'.format(name))
	else:
		print('case {} failed; expected {} got {}'.format(name, expected, result))
		

def main():
	testcase = '1'
	input = []
	expected = []
	result = findLongestBalancedSubarray(input)
	test(testcase, expected, result)

	testcase = '2'
	input = ['n', '1']
	expected = ['n', '1']
	result = findLongestBalancedSubarray(input)
	test(testcase, expected, result)

	testcase = '3'
	input = ['1', 'n']
	expected = ['1', 'n']
	result = findLongestBalancedSubarray(input)
	test(testcase, expected, result)

	testcase = '4'
	input = ['1', 'n', '1', 'n']
	expected = ['1', 'n', '1', 'n']
	result = findLongestBalancedSubarray(input)
	test(testcase, expected, result)

	testcase = '5'
	input = ['1', 'n', '1', '1', 'n']
	expected = ['n', '1', '1', 'n']
	result = findLongestBalancedSubarray(input)
	test(testcase, expected, result)

	testcase = '6'
	input = ['1', 'n', '1', '1', 'n', 'n', 'n', 'n']
	expected = ['1', 'n', '1', '1', 'n', 'n']
	result = findLongestBalancedSubarray(input)
	test(testcase, expected, result)

if __name__ == '__main__':
	main()

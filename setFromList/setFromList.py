#!/usr/bin/python3

import random

# let a be a list of size >= m
def generateSet(m, a):
	result = set()
	endIndex = len(a) - 1
	i = 0
	while i < m:
		randIndex = random.randint(0, endIndex)
		tmp = a[randIndex]
		a[randIndex] = a[endIndex]
		a[endIndex] = tmp
		endIndex -= 1

		if tmp not in result:
			result.add(tmp)
			i += 1
	return result	

def main():
	pass

if __name__ == '__main__':
	main()

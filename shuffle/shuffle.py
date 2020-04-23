#!/usr/bin/python3

import random

def shuffle(x):
	shuffled = [i for i in range(x)]
	for i in range(x):
		tmp = shuffled[i]
		randIndex = random.randint(i, x - 1)
		shuffled[i] = shuffled[randIndex]
		shuffled[randIndex] = tmp
	return shuffled

def main():
	pass

if __name__ == '__main__':
	main()

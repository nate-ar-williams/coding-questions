#!/bin/bash/python3

# basic plan: xor = XOR operands
# carry = & operands, << result

import sys

def main():
	args = sys.argv[1:]
	a = int(args[0])
	b = int(args[1])

	while True:
		xor = a ^ b
		remainder = a & b
		remainder = remainder << 1
		a = xor
		b = remainder
		if remainder == 0:
			break
	print(a)

if __name__ == '__main__':
	main()

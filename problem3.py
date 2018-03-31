#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket, hashlib, string, sys, os, time

host = "irc.csec.umiacs.umd.edu"   # IP address or URL
port =  4444     # port



def main():
	# use these to connect to the service
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	#for i in range (3):
	# receive some data
	data = s.recv(128)
	print(data)

	values = data.split("\n")
	print values
	operation = values[1]

	equation = operation.split(" ")
	print equation
	num1 = int(equation[0])
	operator = str(equation[1])
	num2 = int(equation[2])

	print num1
	print operator

	print num2

	if (operator == "+"):
		answer = num1 + num2
	elif (operator == "-"):
		answer = num1 - num2
	else:
		answer = 1337

	ans = str(answer)
	print ans
	hex_result = hashlib.sha256(ans).hexdigest()
	print hex_result
	s.send(bytes(hex_result + "\n"))

	time.sleep(1)

	#
	data = s.recv(128)
	print(data)

	values = data.split("\n")
	print values
	operation = values[1]

	equation = operation.split(" ")
	print equation
	num1 = int(equation[0])
	operator = str(equation[1])
	num2 = int(equation[2])

	print num1
	print operator

	print num2

	if (operator == "+"):
		answer = num1 + num2
	elif (operator == "-"):
		answer = num1 - num2
	else:
		answer = 1337

	ans = str(answer)
	print ans
	data = hashlib.sha256(ans).hexdigest()
	s.send(bytes(hex_result + "\n"))
	time.sleep(1)

	#

	data = s.recv(128)
	print(data)
	time.sleep(1)
	data = s.recv(128)
	print(data)
	data = s.recv(128)
	print(data)

	values = data.split("\n")
	print values
	operation = values[1]

	equation = operation.split(" ")
	print equation
	num1 = int(equation[0])
	operator = str(equation[1])
	num2 = int(equation[2])

	print num1
	print operator

	print num2

	if (operator == "+"):
		answer = num1 + num2
	elif (operator == "-"):
		answer = num1 - num2
	else:
		answer = 1337

	ans = str(answer)
	print ans
	hex_result = hashlib.sha256(ans).hexdigest()
	print hex_result
	s.send(bytes(hex_result + "\n"))

	time.sleep(1)

	# close the connection
	s.close()

'''
def remove_non_digits(str):

	 x='aaa12333bb445bb54b5b52'
	>>> import string
	>>> all=string.maketrans('','')
	>>> nodigs=all.translate(all, string.digits)
	>>> x.translate(all, nodigs)
	'1233344554552'
'''

if __name__ == "__main__":
	main()

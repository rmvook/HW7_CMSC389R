#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket, hashlib, string, sys, os, time

host = "irc.csec.umiacs.umd.edu"   # IP address or URL
port =  4444     # port


def main():
	# use these to connect to the service
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	for i in range (4):
	# receive some data
		data = s.recv(1024)
		print(data)

		values = data.split("\n")						#split on \n to isolate the line
		print values
		operation = values[1]							#second part had equation

		equation = operation.split(" ")					#break up equation
		print equation	
		num1 = int(equation[0])							#first number
		operator = str(equation[1])						#operator + or -
		num2 = int(equation[2])							#second number

		if (operator == "+"):							#seemed to only have two operations
			answer = num1 + num2
		elif (operator == "-"):
			answer = num1 - num2
		else:
			answer = 1337								#error, gets turned into LEET

		ans = str(answer)
		hex_result = hashlib.sha256(ans).hexdigest()
		s.send(bytes(hex_result + "\n"))			     #make sure to send as bytes


	
	# close the connection
	s.close()

if __name__ == "__main__":
	main()

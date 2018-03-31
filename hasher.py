import string
import sys
import hashlib
import os

salt = ''
pepper = ''

hashes=[]

def main():
	password_file = open("rockyou.txt", 'r')
	#output_file = open("out.txt", 'w')
	i = 0
	for line in password_file:
		print line.rstrip()

		hash_1 = hashlib.sha1(line.rstrip()).hexdigest()
		print hash_1
		hash_1 = hash_1.decode("hex").encode("base64")
		print hash_1

		hash_md5 = hashlib.md5(line.rstrip()).hexdigest()
		print hash_md5
		hash_md5 = hash_md5.decode("hex").encode("base64")
		print hash_md5

		hash_244 = hashlib.sha224(line.rstrip()).hexdigest()
		print hash_244
		hash_244 = hash_244.decode("hex").encode("base64")
		print hash_244

		hash_256 = hashlib.sha256(line.rstrip()).hexdigest()
		print hash_256
		hash_256 = hash_256.decode("hex").encode("base64")
		print hash_256

		hash_384 = hashlib.sha384(line.rstrip()).hexdigest()
		print hash_384
		hash_384 = hash_384.decode("hex").encode("base64")
		print hash_384

		hash_512 = hashlib.sha512(line.rstrip()).hexdigest()
		print hash_512
		hash_512 = hash_512.decode("hex").encode("base64")
		print hash_512


		i+=1
		if(10 == i):
			sys.exit("Error message")
	'''
	h = open('output.txt', 'w')
	with open("rockyou.txt", 'r') as f:		
		for line in f:
			hashes.append(line)

	with open(sys.argv[1], 'r') as g:
		for line in g:
			hash_object = hashlib.sha256(salt + line.rstrip() + pepper).hexdigest()
			hash_object = hash_object.decode("hex").encode("base64")
			hash_object = hash_object				
			if  hash_object in hashes:	
				for i in range (len(hashes)):
					if hashes[i] == hash_object:
						hashes[i] = line

			
	for i in range (len(hashes)):
		h.write(hashes[i])
	'''
	
	
if __name__ == "__main__":
	main()

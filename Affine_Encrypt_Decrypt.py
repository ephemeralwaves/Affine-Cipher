#Encrypter Function
#E(x) = eaffine = (ax + b) mod m
def eaffine(a, b):
	print "This is the encrypted Alphabet\n (plain text : cipher text)\n"
	
	#sets the mod to 26
	for i in range(26):
		#Prints the plain text alphabet and it's corresponding ciphertext alphabet values
		#Note: ascii A is 65, so we have to add/sub 65 to account for ascii value (so that A is essentialy set to 0)
		print chr(i+65) + ": " + chr(((a*i+b)%26)+65) 

	print "Now that we have the transposition table, let's encrypt a plaintext message\n"
	
	#User inputs the plain text message they want encrypted
	plaintext = raw_input("Message (in capitals):")
	# Start with and empty list for the encrypted message
	ciphertext = []
	
	#Finds the numerical value for each letter in the plain text and puts it in the list 
	for x in plaintext:
		ciphertext.append(ord(x))
		
	#Append the corresponding plain text character to encrypted one
	for i in range(len(ciphertext)):
		#encryption algorithm
		ciphertext[i] = chr(((a*(ciphertext[i]-65)+b)%26)+65)
	
	#Print the original and the encrypted message
	print plaintext + ": " + " ".join(ciphertext)
	

#Decrypter Function
#D(x) = daffine = ainverse *(x-b) mod m
def daffine(a, b):
	print "This is the decrypted Alphabet\n (cipher text : plain text)"
	
	#sets the mod to 26
	for i in range(26):
		#Finds the modular multiplicative inverse of a, which is needed in the function below for decrypting
		ainverse = a**(phi(a)-1)%26
		#Prints the cipher text alphabet and it's corresponding plain text alphabet values
		print chr(i+65) + ": " + chr((ainverse*(i- b))%26+65)
		
 	print "Now that we have the transposition table, let's decipher that message\n"
	
	#User inputs the ciphertext they want decrypted
	ciphertext =raw_input("Enter encrypted message (in capitals): ")
	# Start with and empty list to store the decrypted message
	plaintext = []
	
	#Finds the numerical value for letter in the ciphertext and puts it in the list 
	for x in ciphertext:
		plaintext.append(ord(x))
	
	#Append the corresponding ciphertext character to plain text
	for i in range(len(plaintext)):
		#decryption algorithm 
		plaintext[i] = chr((ainverse*((plaintext[i]-65)- b))%26+65)
	
		
	#Print the cipher text and the decrypted message
	print ciphertext + ": " + " ".join(plaintext) + '\n'
	
	
	
#Other Functions Needed for Decryption

#Greatest common divisor
def gcd(a,b):
	#Return the gcd of two positive integers.
	while b != 0:
		a, b = b, a%b
		print a
		print b
        return a
	
#Coprime
def coprime(a,b):
	#return True if 'a' and 'b' are coprime.
	return gcd(a,b) == 1
	
#Euler's Totient Function
def phi(m):
	if m == 1:
		return 1
	else:
		r = [n for n in range(1,int(m)) if coprime(int(m),int(n))]
		#Returns the number/length of coprime numbers that make up m
		return len(r)
		
    

print "Would you like to encrypt (enter e) or decrypt (enter d) the message? "
decision = raw_input("> ")

if decision == "e":
	print "Enter the key: "
	a = int(input("a key: "))
	b = int(input("b key: ")) 
	eaffine(a, b)
	
elif decision == "d":
	print "Now that you have a secret message let's decipher it!"
	print "Enter the key: "
	a = int(input("a key: "))
	b = int(input("b key: ")) 
	daffine(a, b)

else: 
	print "I hope you liked the program!"



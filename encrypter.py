import hashlib

#Letters to numbers dict
lettersAndNumbers = {
	'1': 1,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'0': 0,

	'a': 10,
	'b': 11,
	'c': 12,
	'd': 13,
	'e': 14,
	'f': 15,
	'g': 16,
	'h': 17,
	'i': 18,
	'j': 19,
	'k': 20,
	'l': 21,
	'm': 22,
	'n': 23,
	'o': 24,
	'p': 25,
	'q': 26,
	'r': 27,
	's': 28,
	't': 29,
	'u': 30,
	'v': 31,
	'w': 32,
	'x': 33,
	'y': 34,
	'z': 35
}

#Encrypt function
def encrypt(path, password):
	bytesArray = []

	#Generate hash password
	textHash = hashlib.sha1(password.encode('cp866')).hexdigest()
	for i in password:
		textHash += hashlib.sha1(i.encode('cp866')).hexdigest()

	#Read data from file
	with open(path, 'rb') as file:
		data = file.read()
	
	#Encrypt
	for j in range(len(data)):
		num = j - j//len(textHash)*len(textHash)
		letter = textHash[num]

		#Encode
		bytesArray.append(data[j]^lettersAndNumbers[letter])

	#Write data in file
	with open(path, 'wb') as file:
		file.write(bytes(bytesArray))
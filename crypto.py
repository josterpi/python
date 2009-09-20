
import math
import random

def alpha2num(x):
	return ord(x) - 97

def num2alpha(x):
	return chr(97 + x)

def make_key(x):
	key = ""
	for i in range(x):
		key += num2alpha(random.randrange(26))
	return key

def affine_char_enc(a, b, x):
	return num2alpha((a*alpha2num(x) + b) % 26)

def affine_char_dec(a, b, x):
	inverses = {1 : 1, 3 : 9, 5 : 21, 7 : 15, 9 : 3, 11 : 19, 15 : 7, 17 : 23, 19 : 11, 21 : 5, 23 : 17, 25 : 25}
	return num2alpha((inverses[a]*alpha2num(x) - inverses[a]*b) % 26)

def affine(a,b, plaintext):
	ciphertext = ""
	for i in plaintext:
		ciphertext += affine_char_enc(a,b,i)
	return ciphertext

def affine_dec(a,b,ciphertext):
	plaintext = ""
	for i in ciphertext:
		plaintext += affine_char_dec(a,b,i)
	return plaintext

def vig_key_resize(key, length):
	newkey = key * (length/len(key)+1)
	return newkey[:length]

def vigenere(plaintext, key):
	fullkey = vig_key_resize(key, len(plaintext))
	ciphertext = ""
	for i in range(len(plaintext)):
		ciphertext += affine_char_enc(1,alpha2num(fullkey[i]),plaintext[i])
	return ciphertext

def vigenere_dec(ciphertext, key):
	fullkey = vig_key_resize(key, len(ciphertext))
	plaintext = ""
	for i in range(len(ciphertext)):
		plaintext += affine_char_dec(1,alpha2num(fullkey[i]),ciphertext[i])
	return plaintext

def preptext(text):
	newtext = ""
	for i in text.lower():
		if 97 <= ord(i) and ord(i) <= 122: # between 'a' and 'z'
			newtext += i
	return newtext

def prepfile(filename):
	f = open(filename,"r")
	text = f.read()
	newtext = ""
	for i in text.lower():
		if 97 <= ord(i) and ord(i) <= 122: # between 'a' and 'z'
			newtext += i
	return newtext

def count_chars(text):
	stat_dict = {}
	#stat_dict["len"] = len(text)
	for i in range(26):
		stat_dict[num2alpha(i)] = text.count(num2alpha(i))
		#stat_dict[num2alpha(i) + "%"] = float(stat_dict[num2alpha(i)]) / float(stat_dict["len"])
	return stat_dict

def char_percent(count, length):
	stat_dict = {}
	for i in range(26):
		stat_dict[num2alpha(i)] = float(count[num2alpha(i)]) / float(length)
	return stat_dict


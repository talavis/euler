#!/usr/bin/env python3

'''Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.'''

import string
import sys

def decrypt(key, cipher) :
    text = ''
    for i in range(0, len(cipher)-len(key), len(key)) :
        for j in range(len(key)) :
            print
            text += chr(ord(cipher[i+j]) ^ ord(key[j]))
    diff = len(cipher) % len(key) != 0
    if diff != 0 :
        for i in range((0-diff), 0) :
            text += chr(ord(cipher[i]) ^ ord(key[i+diff]))
    return text
        
raw = open('cipher1.txt').read()

letters = raw[:-1].split(',')
for c in range(len(letters)) :
    letters[c] = chr(int(letters[c]))

key = list('aaa')

text = ''
while not 'gospel' in text.lower() :
    text = decrypt(key, letters)
#    print(key, text)
    key[0] = chr(ord(key[0])+1)
    if key[0] > 'z' :
        key[1] = chr(ord(key[1])+1)
        key[0] = 'a'
        if key[1] > 'z' :
            key[2] = chr(ord(key[2])+1)
            key[1] = 'a'
            if key[2] > 'z' :
                break

int_sum = 0
for i in range(len(text)) :
    int_sum += ord(text[i])
print(int_sum)

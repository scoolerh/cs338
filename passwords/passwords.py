#Hannah Scooler, Oct 25 2023
import hashlib
import binascii

words = [line.strip().lower() for line in open('words.txt')]
             
#Part 1

digests = []
hashCount = 0 
cracked1 = open("cracked1.txt", "w")

for word in words:
    encodedPassword = word.encode('utf-8')
    hasher = hashlib.sha256(encodedPassword)
    digest = hasher.digest()
    hexDigest = binascii.hexlify(digest)
    stringDigest = hexDigest.decode('utf-8')
    hashCount += 1
    digests.append(stringDigest)

users1 = [line.strip().lower() for line in open('pwfile1.txt')]
passwordsCracked = 0
for user in users1:
    user = user.split(":")
    username = user[0]
    encodedPassword = user[1]
    password = ""
    if (encodedPassword in digests): 
        index = digests.index(encodedPassword)
        password = words[index]
        passwordsCracked += 1
        cracked1.write(username + ":" + password + "\n")

print("Hashes Computed: " + str(hashCount))
print("Passwords Cracked: " + str(passwordsCracked))
cracked1.close() 


#Part 2
""" 
users2 = [line.strip().lower() for line in open('pwfile2.txt')]
passwords = {}
cracked2 = open("cracked2.txt", "w")

for user in users2:
    user = user.split(":")
    username = user[0]
    encodedPassword = user[1]
    passwords[encodedPassword] = username

hashCount = 0 
passwordsCracked = 0
for word1 in words:
    for word2 in words: 
        word = word1 + word2
        encodedPassword = word.encode('utf-8')
        hasher = hashlib.sha256(encodedPassword)
        digest = hasher.digest()
        hexDigest = binascii.hexlify(digest)
        stringDigest = hexDigest.decode('utf-8')
        hashCount += 1
        if (stringDigest in passwords):
            username = passwords[stringDigest]
            solved = username + ":" + word + "\n"
            cracked2.write(solved)
            print(solved)
            passwordsCracked += 1
            print("Hashes Computed: " + str(hashCount))
            print("Passwords Cracked: " + str(passwordsCracked)) 
cracked2.close()
"""

#Part 3
""" 
users3 = [line.strip().lower() for line in open('pwfile3.txt')]
cracked3 = open("cracked3.txt", "w")

hashCount = 0
passwordsCracked = 0
for user in users3:
    user = user.split(":")
    password = user[1].split("$")
    username = user[0]
    salt = password[2]
    password = password[3]
    for word in words:
        cat = str(salt) + word
        encodedPassword = cat.encode('utf-8')
        hasher = hashlib.sha256(encodedPassword)
        digest = hasher.digest()
        hexDigest = binascii.hexlify(digest)
        stringDigest = hexDigest.decode('utf-8')
        hashCount += 1
        if (stringDigest == password): 
            passwordsCracked += 1
            password = word
            solved = username + ":" + password
            cracked3.write(solved + "\n")
            print("Passwords Cracked: " + str(passwordsCracked))
print("Hashes Computed: " + str(hashCount))
cracked3.close() 
"""

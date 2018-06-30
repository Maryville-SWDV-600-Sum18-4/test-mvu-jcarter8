#File: password_generator.py
#Author: Jerry Carter
#GitHub: mvu-jcarter8

from random import randrange

#get user input for password length
pwdLength = int(input('How many characters for your password?: '))

#create list for numbers 65-90, 97-122 to assign with ordinals for ABC-xyz
ordList = list(range(65,91)) + list(range(97,123))
#print(ordRange)

#initialize variable
newPassword = ''

#create for loop with input as range
for char in range(pwdLength):

	#pull random number that will correspond to a ordinal value from the ordinal list of usable characters and store in accumulation variable
	randomOrdinal = randrange(0, len(ordList))
	newPassword = newPassword + chr(ordList[randomOrdinal])

#print out password
print(newPassword)
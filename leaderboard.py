#File: leaderboard.py
#Author: Jerry Carter
#GitHub: mvu-jcarter8

#Write a program that processes a file with video game scores and then outputs the highest score for each difficulty level. Within the file each line contains a player's name, the difficulty level, and their score

#create player class to store name, difficulty, and score
class PlayerData():
	def __init__(self, name, level, score):
		self.name = name
		self.level = level
		self.score = score

	def getName( self ):
		return self.name

	def getLevel( self ):
		return self.level

	def getScore( self ):
		return self.score
		
#open the file and read through each line
def main():
	scoresFile = open('scores.txt','r')
	scoresList = scoresFile.readlines()
	playerDataDict = {} 
	lineCount = 0

	for line in scoresList:
		lineCount = lineCount + 1
		scoreLine = line.split(',')

		#store line in player class
		dataToPlayer = PlayerData( scoreLine[0], scoreLine[1], scoreLine[2].strip())

		#store player class data in dictionary list
		playerDataDict[lineCount] = (dataToPlayer.getName(),dataToPlayer.getLevel(), dataToPlayer.getScore())

	#format output and sort results
	print('********** LEADERBOARD ***********')
	for line in playerDataDict:
		print('{} : {} with {} points'.format(dataToPlayer.getLevel(), dataToPlayer.getName(),dataToPlayer.getScore() ))

main()
#Tyler Schad
#TA Jason Zietz
#Project 1

import random
#first list
oldList = [("Kai" , "Red" , "big"), ("Mark", "Black" , "big"), ("Bob" , "Blonde" , "small"), ("Kevin" , "Grey" , "small"), ("Megan" , "Red" , "small"), ("Sam" , "Long blonde" , "small"), ("Mallory" , "Black" , "small"), ("Hannah" , "Long blonde" , "big"), ("Adam" , "Grey" , "big")]

#second list
characterList = []
#third list
mafiaList = []
for i in range(len(oldList)):
	element = random.choice(oldList)
	oldList.remove(element)
	characterList.append(element)
characterList = characterList

killerOne = characterList[0]
killerTwo = characterList[1]

mafiaList.append(killerOne)
mafiaList.append(killerTwo)
mafiaList = mafiaList

import pygame
from pygame.locals import *

surfarray = pygame.surfarray

#initialize pygame
pygame.init()
#load the image
imgsurface = pygame.image.load('MafiaCharactersSmall.png')
#convert to pixel array
imgarray = surfarray.array3d(imgsurface)

string1 = ""

def writeStringsToFile(string1):
	f = open('MafiaWinners.txt', 'a')
	string1 = raw_input("Type your name to add to the winner's list: ")
	f.write(string1 + '\n')
	f.close()
		
def surfdemo_show(array_img, name):
    "displays a surface, waits for user to continue"
    screen = pygame.display.set_mode(array_img.shape[:2], 0, 32)
    surfarray.blit_array(screen, array_img)
    pygame.display.flip()
    pygame.display.set_caption(name)

def intro():
	begin = False
	#first while loop
	while begin == False:
		#first string
		print "You live in a small town, practically isolated from the rest of society."
		print "Everyone is happy, and rarely anything exciting happens. But recently the mafia has come into town..."
		print "AND ARE DISGUISED AS REGULAR VILLAGERS!" 
		print "You must figure out who the mafia members are and defeat them before they kill everyone in the town. This is how it works..."
		print ""
		print "1. There are 2 mafia members, 7 regular townspeople, and you."
		print "2. Every night, while everyone sleeps, one innocent person will be killed."
		print "3. You will then recieve a clue, and guess every day who you think a mafia member is. The clue will be based off of footprints or hair found at the crime scene. But be careful, this clue is for only one of the two mafia members."
		print "4. Whoever you guess as the mafia will then die, so be careful to not accidentally kill an innocent!"
		print "5. The game will end when you kill the two mafia members, or if they are able to kill everyone in town."
		print "Do you think you can win?"
		startPlay = raw_input("Press space and enter to play:")
		if startPlay == " ":
			beginReal = False
			#second while loop
			while beginReal == False:
				#second string
				print ""
				print "GREAT! Let's meet the villagers..."
				print ""
				print "1. Kai: Red hair, has big feet."
				print "2. Mallory: Black hair, has small feet."
				print "3. Sam: Long blonde hair, has small feet."
				print "4. Adam: Grey hair, has big feet."
				print "5. Bob: Blonde hair, has small feet."
				print "6. Megan: Red hair, has small feet."
				print "7. Kevin: Grey hair, has small feet."
				print "8. Mark: Black hair, has big feet."
				print "9. Hannah: Long blonde hair, has big feet."
				print ""
				
				#load image
				surfdemo_show(imgarray, 'imgarray')
				
				print ""
				print ""
				print ""
				print ""
				print ""
				print ""
				print ""
				print ""
				print ""
				print ""
				startPlay = raw_input("Are you ready? To go to the first night, play space and enter:")

				if startPlay == " ":
					beginReal = True
				else:
					beginReal = False
			print ""
			begin = True
		else:
			begin = False
	
def dayLoop():
	#first numerical variable
	alive = 3
	#second numerical variable
	n = 1
	#third numerical variable
	mafiaAlive = 2
	#fourth numerical variable
	wrongGuess = 0
	
	#third while loop
	while alive > 0 and mafiaAlive > 0:
		victim = characterList[n+1][0]
		#third string
		print "__________________________________________________________"
		print ""
		print "After going to bed, you wake up the next morning."
		print "As you leave your house, something seems wrong..."
		print ""
		print "Oh no,", victim, "has died!"
		alive = alive - 1
		n = n + 1
		from random import randint
		hairOrFeet = randint(0,1)
		
		#first if/else block
		if len(mafiaList) == 2:
			#second if/else block
			if mafiaList[0] == characterList[0]:
				#third if/else block
				if hairOrFeet == 0:
					print mafiaList[0][1], "hair was found at the scene!"
				else:
					print "Some", mafiaList[0][2], "footprints were found at the scene!"
			else:
				#fourth if/else block
				if hairOrFeet == 0:
					print mafiaList[1][1], "hair was found at the scene!"
				else:
					print "Some", mafiaList[1][2], "footprints were found at the scene!"
		else:
			#fifth if/else block
			if hairOrFeet == 0:
				print mafiaList[0][1], "hair was found at the scene!"
			else:
				print "Some", mafiaList[0][2], "footprints were found at the scene!"
		hairOrFeet = randint(0,1)

#where the guessing begins...AND ALLL THE IF/ELSE BLOCKS
		guessMafia = raw_input("Who committed the crime? It's time to guess by writing the villager's name: ")
		
#if they guess correctly
		if len(mafiaList) == 2:
			if guessMafia == mafiaList[0][0]:
				print "You guessed correctly!", guessMafia, "was one of the killers!"
				print ""
				print "They are now eliminated from the game. Good job!"
				print ""
				mafiaAlive = mafiaAlive - 1
				del mafiaList[0]
				#gives you an extra turn, because 2 villagers could still kill 1 mafia
				alive = alive + 1
			elif guessMafia == mafiaList[1][0]:
				print "You guessed correctly!", guessMafia, "was one of the killers!"
				print ""
				print "They are now eliminated from the game. Good job!"
				print ""
				mafiaAlive = mafiaAlive - 1
				del mafiaList[1]
				alive = alive + 1
		elif len(mafiaList) == 1:
			if guessMafia == mafiaList[0][0]:
				print "You guessed correctly!", guessMafia, "was one of the killers!"
				print ""
				print "They are now eliminated from the game. Good job!"
				print ""
				mafiaAlive = mafiaAlive - 1
				alive = alive + 1
		else:
			print "No more mafia members!"

#if they guess incorrectly
	#if they haven't guessed incorrectly yet...
		if wrongGuess == 0:
			if guessMafia == characterList[2][0]:
				#fourth string
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				n = n + 1
				characterList.insert(2, characterList[2])
				del characterList[3]
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[3][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[3])
				del characterList[4]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[4][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[4])
				del characterList[5]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[5][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[5])
				del characterList[6]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[6][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[6])
				del characterList[7]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[7][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[7])
				del characterList[8]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[8][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[8])
				del characterList[9]
				n = n + 1
				wrongGuess = wrongGuess + 1
			else:
				print ""
	
	#if they have guessed incorrectly once before...
		elif wrongGuess == 1:
			if guessMafia == characterList[3][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[3])
				del characterList[4]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[4][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[4])
				del characterList[5]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[5][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[5])
				del characterList[6]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[6][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[6])
				del characterList[7]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[7][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[7])
				del characterList[8]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[8][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[8])
				del characterList[9]
				n = n + 1
				wrongGuess = wrongGuess + 1
			else:
				print ""	
	
	#if they've guessed incorrectly twice before...		
		elif wrongGuess == 2:
			if guessMafia == characterList[4][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[4])
				del characterList[5]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[5][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[5])
				del characterList[6]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[6][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[6])
				del characterList[7]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[7][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[7])
				del characterList[8]
				n = n + 1
				wrongGuess = wrongGuess + 1
			elif guessMafia == characterList[8][0]:
				print ""
				print "Sorry... you guessed incorrectly.", guessMafia, "is eliminated from the game."
				print ""
				characterList.insert(2, characterList[8])
				del characterList[9]
				n = n + 1
				wrongGuess = wrongGuess + 1
			else:
				print ""
		else:
			print ""
	
#if you killed all of the mafia in time				
	if mafiaAlive == 0:
		print ""
		print "All of the mafia are defeated! Congrats!"
		myFile = open("MafiaWinners.txt", "a")
		writeStringsToFile(string1)
	
#losing message
	else:
		print ""
		print "You lose, the mafia have taken over! Better luck next time."

def scoreboard():
	print "__________________________________________________________"
	seeScoreboard = raw_input("If you would like to see the list of past winners, press space and enter:")
	if seeScoreboard == " ":
		print ""
		myFile = open("MafiaWinners.txt", "r") 
		lns = myFile.readlines()
		#print "lns=", lns
		for line in lns:
			print line
			print ""
		myFile.close()
	else:
		print "Thanks for playing!"
	
def main():
	#first function
	intro()
	#second function
	dayLoop()
	#third function
	scoreboard()

#fourth function (and surfdemo_show is the fifth, writeStringsToFile is the sixth)
main()

#also use file i/o twice, and image graphics

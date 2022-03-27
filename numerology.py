#numerology
from datetime import datetime

masterNumbers = True

def addDigits(inNum):
	sum = 0
	for digit in str(inNum):
		sum += int(digit)
	if sum < 10 or (masterNumbers and sum in [11, 22]):
		return sum
	else:
		return addDigits(sum)

def letterValue(letter):
	return (ord(letter) - 65) % 9 + 1

def analyzeName(name):
	name = name.upper()
	consonantsSum = 0
	vowelsSum = 0
	for letter in name:
		if ord(letter) >=65 and ord(letter) <= 90:
			if letter in "AEIOUY":
				vowelsSum += letterValue(letter)
			else:
				consonantsSum += letterValue(letter)
	destiny = addDigits(vowelsSum + consonantsSum)
	soul = addDigits(vowelsSum)
	personality = addDigits(consonantsSum)
	return (destiny, soul, personality)

class Person:
	def __init__(self, name, birth):
		self.name = name.upper()
		self.birth = birth
		self.destiny, self.soul, self.personality = analyzeName(self.name)
		self.life = addDigits(self.birth.strftime("%m%d%Y"))
		
	def showProfile(self):
		print("***********************")
		print(f"{self.name}")
		print(f"Life Path: {self.life}")
		print(f"Destiny Number: {self.destiny}")
		print(f"Soul Number: {self.soul}")
		print(f"Personality Number: {self.personality}")
		print("***********************")

name = input("Enter a name: ")
dob = datetime.strptime(input("Enter the date & time of birth (MM/DD/YYYY HH:MM:SS): "), "%m/%d/%Y %H:%M:%S")
p = Person(name, dob)
p.showProfile()

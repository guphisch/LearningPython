#!/usr/bin/python3
import random
abbort = "n"

def addition():
	first = 0
	second = 0
	sollErgebnis = 101
	while sollErgebnis > 100:
		first = random.randint(1,100)
		second = random.randint(1,100)
		sollErgebnis = first + second
	print("Bitte rechne " + str(first) + " + " + str(second))
	print("Ergebnis: ")
	try:
		istErgebnis = int(input())
	except ValueError:
		abbort = "j"
		return
	if istErgebnis == sollErgebnis:
		print("Super, das Ergebnis ist richtig!")
	else:
		print("Schade, das Ergebnis ist leider falsch!")
		print("Das richtige Ergebnis lautet: " + str(sollErgebnis)) 

def subtraktion():
	first = random.randint(1, 100)
	second = random.randint(1,100)
	if first > second:
		print("Bitte rechne " + str(first) + " - " + str(second))
		print("Erghebnis: ")
		try:
			istErgebnis = int(input())
		except ValueError:
			abbort = "j"
			return
		sollErgebnis = first - second
		if istErgebnis == sollErgebnis:
			print("Super, das Ergebnis ist richtig!")
		else:
			print("Schade, das Ergebnis ist leider falsch!")
			print("Das richtige Ergebnis lautet: " + str(sollErgebnis))
	else:
		print("Bitte rechne " + str(second) + " - " + str(first))
		print("Ergebins: ")
		try:
			istErgebnis = int(input())
		except ValueError:
			abbort = "j"
			return
		sollErgebnis = second - first
		if istErgebnis == sollErgebnis:
			print("Super, das Ergebins ist richtig!")
		else:	 
			print("Schade, das Ergebnis ist leider falsch!")
			print("Das richtige Ergebnis lautet: " + str(sollErgebnis))

while abbort != "j":
	rechnung = random.randint(1,2)
	
	if rechnung == 1:
		addition()
	else:
		subtraktion()



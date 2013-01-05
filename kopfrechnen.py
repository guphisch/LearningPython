#!/usr/bin/python3
import random
abbort = "n"
aufgabenGesamt = 0;
aufgabenRichtig = 0;

def addition(hoechstwert):
	first = 0
	second = 0
	sollErgebnis = hoechstwert + 1
	while sollErgebnis > 100:
		first = random.randint(1,hoechstwert)
		second = random.randint(1,hoechstwert)
		sollErgebnis = first + second
	print("Bitte rechne " + str(first) + " + " + str(second))
	print("Ergebnis: ")
	try:
		istErgebnis = int(input())
	except ValueError:
		global abbort
		abbort = "j"
		return
	if istErgebnis == sollErgebnis:
		print("Super, das Ergebnis ist richtig!")
		print("")
	else:
		print("Schade, das Ergebnis ist leider falsch!")
		print("Das richtige Ergebnis lautet: " + str(sollErgebnis))
		print("")

def subtraktion(hoechstwert):
	first = random.randint(1, hoechstwert)
	second = random.randint(1,hoechstwert)
	if first > second:
		print("Bitte rechne " + str(first) + " - " + str(second))
		print("Erghebnis: ")
		try:
			istErgebnis = int(input())
		except ValueError:
			global abbort
			abbort = "j"
			return
		sollErgebnis = first - second
		if istErgebnis == sollErgebnis:
			print("Super, das Ergebnis ist richtig!")
			print("")
		else:
			print("Schade, das Ergebnis ist leider falsch!")
			print("Das richtige Ergebnis lautet: " + str(sollErgebnis))
			print("")
	else:
		print("Bitte rechne " + str(second) + " - " + str(first))
		print("Ergebins: ")
		try:
			istErgebnis = int(input())
		except ValueError:
			global abbort
			abbort = "j"
			return
		sollErgebnis = second - first
		if istErgebnis == sollErgebnis:
			print("Super, das Ergebins ist richtig!")
			print("")
		else:	 
			print("Schade, das Ergebnis ist leider falsch!")
			print("Das richtige Ergebnis lautet: " + str(sollErgebnis))
			print("")
			
print("Bitte gebe den Maximalwert ein!")
try:
	hoechstwert = int(input())
except ValueError:
	abbort = "j"

while abbort != "j":
	rechnung = random.randint(1,2)
	
	if rechnung == 1:
		addition(hoechstwert)
	else:
		subtraktion(hoechstwert)



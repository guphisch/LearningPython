#!/usr/bin/python3

abbort = "n"
eingabe = "1"

while abbort != "j":
	print("Bitte geben Sie den Wert in Sekunden ein:")
	wert = 1;
	try:
		eingabe = input()
		wert = int(eingabe)
	except ValueError:
		print("Bitte nur ganze Zahlen eingeben.")
		continue
	stunden = int(wert / 3600)
	minuten = int((wert % 3600) / 60)
	sekunden = (wert % 3600) % 60
	print(stunden,"Stunden",minuten,"Minuten",sekunden,"Sekunden")
	print("Programm verlassen? (j/n)")
	abbort = input()



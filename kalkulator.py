# Autor: Albert Mika

#import biblioteki odpowiedzialnej za regex
import re

#definicja funkcji wykorzystywanych w programie
def dodawanie(liczba1, liczba2):
	return liczba1 + liczba2
def odejmowanie(liczba1, liczba2):
	return liczba1 - liczba2
def mnozenie(liczba1, liczba2):
	return liczba1 * liczba2
def dzielenie(liczba1, liczba2):
	return liczba1 / liczba2
#funkcja sprawdzająca poprawność wprowadzanych danych
def sprawdzenieTypu(liczba):
	while not re.match('^-?[0-9]*\.?[0-9]+$',liczba):
		liczba = input("Błędna wartość, wprowadź nową wartość: ")
	if re.match('^-?[0-9]*\.?[0-9]+$',liczba): return float(liczba)

// plik po rozwiązaniu konfliktu
#wyświetlenie listy dostępnych operacji
print("Wybierz operację:")
print("+ Dodawanie")
print("- Odejmowanie")
print("* Mnożenie")
print("/ Dzielenie\n")

wybor = input("Twój wybór ? +, -, *, / : ")
while not(wybor == '+' or wybor == '-' or wybor == '*' or wybor == '/' or wybor == ":"):
	wybor = input("Błędna opcja! Wybierz na nowo: ")


liczba1 = input("Wprowadź pierwszą liczbę: ")
liczba1 = sprawdzenieTypu(liczba1)

liczba2 = input("Wprowadź drugą liczbę: ")
liczba2 = sprawdzenieTypu(liczba2)

# instrukcja wyboru operacji
if wybor == '+':
	print(liczba1,"+",liczba2,"=",dodawanie(liczba1,liczba2))
elif wybor == "-":
	print(liczba1,"-",liczba2,"=",odejmowanie(liczba1,liczba2))
elif wybor == "*":
	print(liczba1,"*",liczba2,"=",mnozenie(liczba1,liczba2))
elif wybor == "/" or wybor == ":":
	print(liczba1,"/",liczba2,"=",(liczba2 == 0) and "Nie policzę tego przykładu, \
nie dzielimy przez 0!" or dzielenie(liczba1,liczba2))

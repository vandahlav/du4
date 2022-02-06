import json
from json.decoder import JSONDecodeError

#funkce pro kontrolu načítání souboru
def otevreni_souboru(soubor):
    try:
        with open(soubor, encoding="utf-8") as soubor:
            return json.load(soubor)
    except FileNotFoundError:
        print("Vstupní soubor se nepodařilo načíst. Ujistěte se, že daný soubor existuje, případně zda je k němu zadána korektní cesta.")
        quit()
    except PermissionError:
        print("Program nemá přístup k zápisu výstupních souborů.")
        quit()
    except JSONDecodeError:
        print("Načtený vstupní soubor není platný JSON.")
        quit()

#funkce pro kontrolu přístupu k zápisu výstupního souboru
def pristup_k_souboru(soubor):
    try:
        pass
        #SEM POTOM DÁT, ŽE TO ZAPISUJU
    except PermissionError:
        print("Program nemá přístup k zápisu výstupních souborů.")

#funkce pro kontrolu maximální délky
def je_cislo(n):
    try:
        cislo = int(n)
    except ValueError:
        print("Chybně zadána maximální délka segmentu. Program končí.")
        quit()
    if cislo < 0:
        print("Bylo zadáno záporné číslo, program skončí.")
        quit()
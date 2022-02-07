import json
from json.decoder import JSONDecodeError

"""#funkce pro načtení souboru
def otevreni_souboru(soubor):
    data = {}
    try:
        with open(soubor, "r",  encoding="utf-8") as in_file:
            #data = json.load(in_file)
            #return data
            return json.load(in_file)
    except FileNotFoundError:
        print("Vstupní soubor se nepodařilo načíst. Ujistěte se, že daný soubor existuje, případně zda je k němu zadána korektní cesta.")
        quit()
    except PermissionError:
        print("Program nemá přístup k zápisu výstupních souborů.")
        quit()
    except JSONDecodeError:
        print("Načtený vstupní soubor není platný JSON.")
        quit()

#funkce zápis do výstupního souboru
def pristup_k_souboru(output_soubor):
    try: 
        with open(output_soubor, "w", encoding="utf-8") as zapis:     
            json.dump(output_soubor, zapis)
    except PermissionError:
        print("Program nemá přístup k zápisu výstupních souborů.")
        quit()"""

#ookus s definováním class pro zápis a načtení souboru
class Writer():
    def __init__(self, data):
        self.data = data
        self.data_in = {}
        self.seznam = []
    
    #načtení souboru
    def input (self):
        try:
            with open(self.data, "r",  encoding="utf-8") as in_file:
                self.data_in = json.load(in_file)
                return self.data_in
        except FileNotFoundError:
            print("Vstupní soubor se nepodařilo načíst. Ujistěte se, že daný soubor existuje, případně zda je k němu zadána korektní cesta.")
            quit()
        except PermissionError:
            print("Program nemá přístup k zápisu výstupních souborů.")
            quit()
        except JSONDecodeError:
            print("Načtený vstupní soubor není platný JSON.")
            quit()

    #zápis do souboru
    def output (self):
        try: 
            with open(self.data, "w", encoding="utf-8") as zapis: 
                zapisuju_sem = []    
                for line in self.seznam:
                    zapisuju_sem.append(line.zapis()) 
                self.data_in["features"] = zapisuju_sem              
                json.dump(self.data, zapis)
        except PermissionError:
            print("Program nemá přístup k zápisu výstupních souborů.")
            quit()

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
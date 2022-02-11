import json
from json.decoder import JSONDecodeError

#funkce pro načtení souboru
def otevreni_souboru(vstupni_soubor):
    try:
        with open(vstupni_soubor, "r",  encoding="utf-8") as in_file:
            data = json.load(in_file)
            return data
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
def vystupni_soubor(data ,output_soubor):
    try: 
        with open(output_soubor, "w", encoding="utf-8") as vystup:  
            json.dump(data, vystup)
    except PermissionError:
        print("Program nemá přístup k zápisu výstupních souborů.")
        quit()
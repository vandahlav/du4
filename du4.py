import argparse
import json
from funkce_du4 import otevreni_souboru, pristup_k_souboru, je_cislo

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--inputfile", help="Název vstupního souboru", type = otevreni_souboru)
parser.add_argument("-l", "--maxlenght", help="Maximální délka", type = je_cislo)
parser.add_argument("-o", "--outputfile", help="Název výstupního souboru", type = pristup_k_souboru)

arguments = parser.parse_args()
vstup = arguments.inputfile

for feature in vstup["features"]:
    promena = feature["geometry"]["coordinates"]
    print(promena)


import argparse
import json
#from funkce_du4 import otevreni_souboru, pristup_k_souboru, je_cislo
from funkce_du4 import je_cislo, Writer
from classes import LineString

#načtení parametrů 
parser = argparse.ArgumentParser()
"""
parser.add_argument("-f", "--inputfile", help="Zadejte název vstupního souboru", type = otevreni_souboru)
parser.add_argument("-l", "--maxlength", help="Zadejte maximální délku segmentu", type = je_cislo)
parser.add_argument("-o", "--outputfile", help="Zadejte název výstupního souboru", type = pristup_k_souboru)
arguments = parser.parse_args()"""

#pokus s class místo funkcí
parser.add_argument("-f", "--inputfile", help="Zadejte název vstupního souboru")
parser.add_argument("-l", "--maxlength", help="Zadejte maximální délku segmentu", type = je_cislo)
parser.add_argument("-o", "--outputfile", help="Zadejte název výstupního souboru")
arguments = parser.parse_args()

max_length = arguments.maxlength

#načtení suboru
"""soubor = otevreni_souboru(arguments.inputfile)
vystup = pristup_k_souboru(arguments.outputfile)"""

zpracovani = Writer(arguments.inputfile)
soubor = zpracovani.input()
linestring_seznam = []
for data in soubor:
    if data["geometry"]["type"] == "LineString":
        lomena_linie = LineString(data)
        linestring_seznam.append(lomena_linie.divide_long_segments(max_length))

zpracovani.output()
import argparse
import json
from funkce_du4 import otevreni_souboru, vystupni_soubor
from classes import LineString

#načtení parametrů 
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--inputfile", help="Zadejte název vstupního souboru", required=True)
parser.add_argument("-l", "--maxlength", help="Zadejte maximální délku segmentu", required=True, type = float)
parser.add_argument("-o", "--outputfile", help="Zadejte název výstupního souboru", required=True)
arguments = parser.parse_args()

max_length = arguments.maxlength

#načtení suboru
soubor = otevreni_souboru(arguments.inputfile)

linestring_seznam = []
for k in soubor:
    #if k["geometry"]["type"] == "LineString":
    lomena_linie = LineString(k)
    linestring_seznam.append(lomena_linie.divide_long_segments(max_length))

vystup = vystupni_soubor(arguments.outputfile)
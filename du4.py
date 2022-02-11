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
output_file = arguments.outputfile

#načtení suboru
soubor = otevreni_souboru(arguments.inputfile)

linestring_seznam = []
for linie in soubor:
    #if linie ["geometry"]["type"] == "LineString":
    linie1 = LineString(linie)
    linestring_seznam.append(linie1.divide_long_segments(max_length))

#zápis výstupního souboru
output = vystupni_soubor(linestring_seznam, output_file)
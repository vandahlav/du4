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
input_file = arguments.inputfile

#načtení suboru
soubor = otevreni_souboru(input_file)

#procházení souboru typu LineString
for line in soubor["features"]:
    if line ["geometry"]["type"] == "LineString":
        line_p = LineString(line["geometry"]["coordinates"])
        line_p.divide_long_segments(max_length)
        line["geometry"]["coordinates"] = line_p.zapis()

#zápis výstupního souboru
output = vystupni_soubor(soubor, output_file)
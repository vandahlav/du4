import argparse
import json
from funkce_du4 import otevreni_souboru, pristup_k_souboru, je_cislo, vzdalenost
from abc import ABC, abstractclassmethod
from classes import LineString, Segment, Point

#načtení souboru
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--inputfile", help="Název vstupního souboru", type = otevreni_souboru)
parser.add_argument("-l", "--maxlenght", help="Maximální délka", type = je_cislo)
parser.add_argument("-o", "--outputfile", help="Název výstupního souboru", type = pristup_k_souboru)

arguments = parser.parse_args()
vstup = arguments.inputfile
max_lenght = arguments.maxlenght
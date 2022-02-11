### Domácí úkol 4 - dělení lomených čar
## Použití (vstupní data a výstupy)
Program načítá celkem tři vstupní argumenty od uživatele pomocí knihovny "argparse". Jedná se o název vstupního souboru (-f), maximální délku segmentu dané lomené čáry (-l) a nakonec jméno výstupního souboru (-o). Tyto argumenty jsou nunté pro spuštění, tedy v případě nedefinování všech, program neproběhne. Samotné spuštění programu porté probíhá v souboru du4.py. Soubory classes.py a funkce_du4.py obsahují definování tříd a funkcí. 

Výstupem je soubor json, který obsahuje segmenty, které nejsou delší, než daná maximální vzdálenost. 

## Zpracování 
Jak již bylo zmíněno, program načte tři vstupní parametry od uživatele. Následně prochází pomocí for cyklu jednotlivé linie, u kterých zjišťuje vzdálenost. Pokud je tato vzdálenost větší, než uživatelem zadaná, dojde k rozdělení příslušné linie na dva segmenty. Vzniknou tak dva stejně dlouhé nové segmenty (k rozdělení dochází v polovině původní linie). Poté dojde opět k porovnání a v případě, že i tyto nové segmenty jsou delší než požadovaná vzdálenost, proběhne půlení znovu.
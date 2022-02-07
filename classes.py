from math import sqrt

#vytvoření třídy polyline
class LineString():
    def __init__(self, vstup): 
        self.linestring = []
        self.vstup = vstup
        
    #tvorba linestring - procházení dat? rozdělení linestring na segmenty?
    def vstupni_data (self):
        for bod in self.vstup["features"]["coordinates"]:
            point = Point(bod[0], bod[1])

    #doplnění linestring o nově rozdělené segmenty
    def nove_segmenty (self, novy_segment):
        self.linestring.append(novy_segment) 
    
    #rozělení dlouhého segmentu
    def divide_long_segments(self, max_length):
        new_linestring = LineString()
        new_linestring.vstup = self.vstup
        for line in self.linestring:
            linestring_rozdeleni = line.divide(max_length)
            self.linestring.append(new_linestring)
        return new_linestring

    #funkce pro zápis nových dat
    def zapis (self):
        zapisuju_sem = []
        for segment in self.linestring:
        #UPRAVIT - NEBUDE SE TO TAKHLE PŘEPISOVAT?
            zapisuju_sem.append([segment.bod1.x, segment.bod1.y])
            zapisuju_sem.append([segment.bod2.x, segment.bod2.y])
        self.vstup ["geometry"]["coordinates"] = zapisuju_sem
        return self.vstup 

#vytvoření třídy segmentů
class Segment():
    def __init__(self, bod1, bod2):
        self.bod1 = bod1
        self.bod2 = bod2

    #výpočet délky segmentu
    def vzdalenost (self):
        self.delka = sqrt((self.bod1.x - self.bod2.x)**2 + (self.bod1.y - self.bod2.y)**2)
        return self.delka

    #výpočet půlícího bodu v případě příliš dlouhého segmentu
    def middle_point (self):
        self.middle_point = Point(((self.bod1.x + self.bod2.x)/2), ((self.bod1.y + self.bod2.y)/2))

    #rozdělení příliš dlouhých segmentů
    def divide(self, max_length):
        linestring = LineString()
        if self.delka() >= max_length:
            self.middle_point()
            #vytváření nových segmentů
            linestring.nove_segmenty(Segment(self.bod1, self.middle_point))
            linestring.nove_segmenty(Segment(self.middle_point, self.bod2))
            return linestring.divide_long_segments(max_length)
        #vytvoření linestring z jednotlivých segmentů
        linestring.nove_segmenty(self)
        return linestring

#vytvoření třídy bodů
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y 
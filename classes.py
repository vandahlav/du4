from math import sqrt

#VYTVOŘENÍ TŘÍDY POLYLINE
class LineString():
    def __init__(self, vstup): 
        self.polyline = []
        self.vstup = vstup

    def divide_long_segments(self, max_lenght):
        new_linestring = LineString()
        pass
        #super metoda (rozdělení line)
        
    #tvorba linestring - procházení dat? rozdělení linestring na segmenty?
    def data (self):
        pass
    """for bod in vstup["features"]["coordinates"]:
        point = Point(bod[0], bod[1])"""

    #doplnění linestring o nově rozdělené segmenty
    def nove_segmenty (self, novy_segment):
        self.polyline.append(novy_segment) 
    
    def __str__ (self):
        return f"Tohle je lomená čára {self.l}"

#VYTVOŘENÍ TŘÍDY SEGMENTŮ 
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

    def divide(self, max_length):
        #odkazuju se na super metodu - takže na tvorbu linestring
        linestring = LineString()
        #zjistím, jestli to je moc dlouhý a pak to hodím do super metody
        if self.delka() >= max_lenght:
            self.middle_point()
            #tady vytvářím nový segment? 
            linestring.nove_segmenty(Segment(self.bod1, self.middle_point))
            linestring.nove_segmenty(Segment(self.middle_point, self.bod2))
            #rekurze? kdyby byl segment pořád too long
        linestring.nove_segmenty(self)
        return linestring

#VYTVOŘENÍ TŘÍDY JEDNOTLIVÝCH BODŮ
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y 
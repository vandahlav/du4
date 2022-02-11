from math import sqrt

#vytvoření třídy polyline
class LineString():
    def __init__(self, coords): 
        self.linestring = []
        
        #počet bodů v jednom LineString
        count_points = (len(coords)-1)

        #procházení dat
        for i in range(count_points):
            point1 = Point(coords[i][0], coords[i][1])
            point2 = Point(coords[i+1][0], coords[i+1][1])
            segment = Segment(point1, point2)
            self.linestring.append(segment)

    """#doplnění linestring o nově rozdělené 
    def nove_segmenty (self, novy_segment):
        self.linestring.append(novy_segment) 
        return self.linestring"""

    #rozělení dlouhého segmentu
    def divide_long_segments(self, max_length):
        new_linestring = []
        for line in self.linestring:
            new_line = line.divide(max_length)
            new_linestring.extend(new_line)
        self.linestring = new_linestring
        
    #funkce pro zápis nových dat
    def zapis (self):
        coordinates = []
        for segment in self.linestring:
            coordinates.append([segment.bod1.x, segment.bod1.y])
        last_point = ([self.linestring[-1].bod2.x, self.linestring[-1].bod2.y])
        coordinates.append(last_point)
        return (coordinates)

#vytvoření třídy segmentů
class Segment():
    def __init__(self, bod1, bod2):
        self.bod1 = bod1
        self.bod2 = bod2

    #výpočet délky segmentu
    def vzdalenost (self):
        delka = sqrt((self.bod1.x - self.bod2.x)**2 + (self.bod1.y - self.bod2.y)**2)
        return delka
    
    """#půlící bod u dlouhého segmentu
    def middle_point (self):
        self.middle = Point((self.bod1.x+self.bod2.x)/2, (self.bod1.y+self.bod2.y)/2)"""
   
    #rozdělení příliš dlouhých segmentů
    def divide(self, max_length):
        if self.vzdalenost() >= max_length:

            #výpočet půlícího bodu v případě příliš dlouhého segmentu
            middle_p = Point((self.bod1.x+self.bod2.x)/2, (self.bod1.y+self.bod2.y)/2)

            #vytváření nových segmentů
            segment1= Segment(self.bod1, middle_p)
            segment2= Segment(middle_p, self.bod2)

            #kontrola délky nových segmentů
            new_line1 = segment1.divide(max_length)
            new_line2 = segment2.divide(max_length)
            return new_line1 + new_line2
        
        return [self]

#vytvoření třídy bodů
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y 
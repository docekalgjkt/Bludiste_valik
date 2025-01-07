import tkinter as tk
from Tools.scripts.pysource import walk_python_files

import numpy as np

import csv

import xml.etree.ElementTree as ET

class BludisteApp(tk.Tk):
    def __init__(self, canvas):
        self.canvas = canvas

class Bludiste:
    def __init__(self, bludiste_data):
        self.bludiste_data = bludiste_data

    def getSirka(self):
        sirka = len(self.bludiste_data)
        return sirka

    def getVyska(self):
        vyska = len(self.bludiste_data[0])
        return vyska

class Robot:
    def __init__(self, bludiste, bludiste_data):
        self.bludiste = bludiste
        self.bludiste_data = bludiste_data

    def find_start(self, bludiste, bludiste_data):
       start = []
        for i in range(len(bludiste_data)):
            for j in range(len(bludiste_data[0])):
                if bludiste_data[i][j] == 2:
                   start = bludiste_data[i][j]
        return start

    def find_end(self, bludiste, bludiste_data):
       end = []
        for i in range(len(bludiste_data)):
            for j in range(len(bludiste_data[0])):
                if bludiste_data[i][j] == 3:
                    end = bludiste_data[i][j]
        return end

    def find_walls(self, bludiste, bludiste_data):
       walls = []
        for i in range(len(bludiste_data)):
            for j in range(len(bludiste_data[0])):
                if bludiste_data[i][j] == 1:
                    walls.append([i][j])
        return walls

    def find_paths(self, bludiste, bludiste_data):
       paths = []
       for i in range(len(bludiste_data)):
           for j in range(len(bludiste_data[0])):
               if bludiste_data[i][j] == 0:
                   paths.append([i][j])
       return paths

    def find_a_way(self, bludiste, bludiste_data):










class DAO:
    def __init__(self, bludiste_data):
        self.bludiste_data = bludiste_data

    def save_to_txt_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.bludiste_data:
                file.write(' '.join(map(str, row)) + '\n')
        print(f"Bludiste data saved to {filename}")

    def getBludisteDataTxt(self,filename):
       with open(filename, 'r') as file:
           bludiste_data = np.loadtxt(filename, dtype=int)
           print(bludiste_data)

    def save_to_csv_file(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            mazewriter = csv.writer(csvfile, delimiter=',')
            for row in self.bludiste_data:
                mazewriter.writerow(row)
        print(f"Bludiste data saved to {filename}")

    def getBludisteDataCsv(self,filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            bludiste_data = []
            for row in reader:
                bludiste_data.append([int(value) for value in row])
            print(bludiste_data)

    def save_to_xml_file(self, filename):
        root = ET.Element("bludiste_data")

        for row_data in self.bludiste_data:
            row_element = ET.SubElement(root, 'row')
            for value in row_data:
                ET.SubElement(row_element, 'value', attrib={'value': str(value)})


        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        print(f"Bludiste data saved to {filename}")

    def getBludisteDataXml(self,filename):
        tree = ET.parse(filename)
        root = tree.getroot()

        bludiste_data = []
        for row in root.findall('row'):  # Loop over each row
            row_data = []
            for value in row.findall('value'):
                row_data.append(int(value.attrib['value']))
            bludiste_data.append(row_data)
        print (bludiste_data)

class BludisteView:
    def __init__(self, canvas, bludiste_data, size):
        self.canvas = canvas
        self.bludiste_data = bludiste_data
        self.size = size

    def kresli_bludiste(self):
            radky = len(self.bludiste_data)
            sloupce = len(self.bludiste_data[0])

            for i in range(radky):
                for j in range(sloupce):
                    x1 = j * self.size
                    y1 = i * self.size
                    x2 = x1 + self.size
                    y2 = y1 + self.size
                    if self.bludiste_data[i][j] == 0:
                        color = 'white'
                    elif self.bludiste_data[i][j] == 1:
                        color = 'black'
                    elif self.bludiste_data[i][j] == 2:
                        color = 'red'
                    elif self.bludiste_data[i][j] == 3:
                        color ='cyan'

                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")


bludiste_data = ([[1, 2, 0, 3],
                [1, 0, 1, 0],
                [1, 0, 0, 0],
                [0, 1, 1, 1],
            ])


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

bludiste = BludisteView(canvas, bludiste_data, 100)
bludiste.kresli_bludiste()

dao = DAO(bludiste_data)
dao.getBludisteDataXml("bludiste_save.xml")
dao.save_to_txt_file("bludiste_save.txt")
dao.save_to_csv_file("bludiste_save.csv")
dao.save_to_xml_file("bludiste_save.xml")

bludiste_objekt = Bludiste(bludiste_data)
sirka = bludiste_objekt.getSirka()
print("sirka =", sirka)
vyska = bludiste_objekt.getVyska()
print("vyska =", vyska)


root.mainloop()

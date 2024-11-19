import tkinter as tk

import numpy as np


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

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.bludiste_data:
                file.write(' '.join(map(str, row)) + '\n')
        print(f"Bludiste data saved to {filename}")


class DesignPattern:
    def __init__(self):
        pass
    def getBludisteData(self):
        pass


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
                    color = 'black' if self.bludiste_data[i][j] == 1 else 'white'
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")


bludiste_data = ([[1, 0, 1, 0],
                [1, 0, 1, 0],
                [1, 0, 0, 0],
                [0, 1, 1, 1],
            ])


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

bludiste = BludisteView(canvas, bludiste_data, 100)
bludiste.kresli_bludiste()

bludiste_objekt = Bludiste(bludiste_data)
sirka = bludiste_objekt.getSirka()
print("sirka =", sirka)
vyska = bludiste_objekt.getVyska()
print("vyska =", vyska)

bludiste_objekt.save_to_file("bludiste_data.txt")


root.mainloop()

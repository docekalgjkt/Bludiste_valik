import tkinter as tk
from Tools.scripts.mailerdaemon import emparse_list_from


class BludisteApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)



class Bludiste:
    def __init__(self, bludiste_data):
        self.bludiste_data = bludiste_data

    def getSirka(self):
        sirka = len(self.bludiste_data)
        return sirka

    def getVyska(self):
        vyska = len(self.bludiste_data[0])
        return vyska


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

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

bludiste_data = ([[1, 0, 1, 0],
                  [1, 0, 1, 0],
                  [1, 0, 0, 0],
                  [1, 1, 1, 1],
                  ])

bludiste = BludisteView(canvas, bludiste_data, 100)
bludiste.kresli_bludiste()

bludiste_objekt = Bludiste(bludiste_data)

sirka = bludiste_objekt.getSirka()
print("sirka =", sirka)

vyska = bludiste_objekt.getVyska()
print("vyska =", vyska)

root.mainloop()

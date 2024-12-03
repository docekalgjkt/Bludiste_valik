import tkinter as tk
import numpy as np


class Bludiste:
    def __init__(self, bludiste_data):
        self.bludiste_data = bludiste_data

    def getSirka(self):
        return len(self.bludiste_data)

    def getVyska(self):
        return len(self.bludiste_data[0]) if self.bludiste_data.size > 0 else 0


class BludisteView:
    def __init__(self, canvas, size):
        self.canvas = canvas
        self.size = size
        self.bludiste_data = None

    def create_bludiste(self):
        n = self.size
        self.bludiste_data = np.random.randint(2, size=(n, n))
        print("Bludiště vytvořeno:")
        print(self.bludiste_data)

    def kresli_bludiste(self):
        if self.bludiste_data is None:
            raise ValueError("Bludiště data nebyla vytvořena. Spusťte nejdříve metodu 'create_bludiste'.")

        radky = len(self.bludiste_data)
        sloupce = len(self.bludiste_data[0])

        for i in range(radky):
            for j in range(sloupce):
                x1 = j * 20
                y1 = i * 20
                x2 = x1 + 20
                y2 = y1 + 20
                color = 'black' if self.bludiste_data[i][j] == 1 else 'white'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()


size = 5
bludiste_view = BludisteView(canvas, size)

bludiste_view.create_bludiste()
bludiste_view.kresli_bludiste()

bludiste_objekt = Bludiste(bludiste_view.bludiste_data)
sirka = bludiste_objekt.getSirka()
print("Šířka =", sirka)

vyska = bludiste_objekt.getVyska()
print("Výška =", vyska)

root.mainloop()
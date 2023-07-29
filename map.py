# conda activate map
# pyinstaller -w --icon=maps.ico map.py --hidden-import openpyxl.cell._writer

import matplotlib.pyplot as plt
import os
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from PIL import ImageTk, Image, ImageGrab
import PIL.ImageGrab
import time
import pandas as pd
import numpy as np
nan = np.nan
import geopandas as gpd
from fiona.ogrext import Iterator, ItemsIterator, KeysIterator


# texas = gpd.read_file("./Texas_County/County.shp")
texas = gpd.read_file(os.path.join('/Users/basavaprasadgola/Codes/Python/Texas_Map_coloring/Texas_County', 'County.shp'))


root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=700)
canvas.pack()
fig = plt.figure(figsize=(9, 4))
ax=fig.gca()

texas.plot(color = 'white', edgecolor = 'black', linewidth = 0.2, ax=ax)
ax.axis('off')

root.attributes("-fullscreen", True)

canvas = FigureCanvasTkAgg(fig, canvas)
canvas.draw()
canvas.get_tk_widget().pack()

def take_screenshot():
  filename = f"screenshot-{time.strftime('%Y%m%d-%H%M%S')}.png"
  image = PIL.ImageGrab.grab()
  image.save(filename)

def choose_Sheets():
  filename = tk.filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])


  if filename:
    sheet = pd.read_excel(filename, engine='openpyxl')
    # sheet = gpd.read_file(filename)  

    string1 = tk.simpledialog.askstring(title="String 1", prompt="Enter 1st column:")
    string2 = tk.simpledialog.askstring(title="String 2", prompt="Enter 2nd column:")

  colors = []

  for i in texas["CNTY_NM"]:
    index_In_xlsx = sheet[string1].tolist().index(i)


    if sheet[string2][index_In_xlsx] is nan:
      colors.append('#D3D3D3')
    if sheet[string2][index_In_xlsx] == 'WHITE':
      colors.append('#FFFFFF')
    elif sheet[string2][index_In_xlsx] == 'RED':
      colors.append('#FF0000')
    elif sheet[string2][index_In_xlsx] == 'LIGHT GREEN':
      colors.append('#90EE90')
    elif sheet[string2][index_In_xlsx] == 'DARK GREEN':
      colors.append('#006400')
    elif sheet[string2][index_In_xlsx] == 'ORANGE':
      colors.append('#FF8000')
    elif sheet[string2][index_In_xlsx] == 'LIGHT YELLOW':
      colors.append('#FFFF51')
    elif sheet[string2][index_In_xlsx] == 'DARK YELLOW':
      colors.append('#FFBF25')

  texas.plot(color = colors, edgecolor = 'black', linewidth = 0.2, ax=fig.gca())
  # Save as functionallity
  plt.savefig('/Users/basavaprasadgola/Codes/Python/Texas_Map_coloring/dist/new.jpg')

button2 = tk.Button(text="Choose Sheet", command=choose_Sheets)

button2.pack(side="left")

root.mainloop()
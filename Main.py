import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import Ai
import numpy as np

model = Ai.load_ai()

window = tk.Tk()

img = Image.new(mode="1", size=(500, 500), color=0)
tkImage = ImageTk.PhotoImage(img)
canvas = tk.Label(window, image=tkImage)
canvas.pack()

draw = ImageDraw.Draw(img)

last_point = (0,0)
prediction = tk.StringVar()

def draw_image(event):
    global last_point, tkImage, prediction
    current_point = (event.x, event.y)

    draw.line([last_point, current_point], fill=255, width=50)

    last_point = current_point
    tkImage = ImageTk.PhotoImage(img)
    canvas['image'] = tkImage
    canvas.pack()

    img_temp = img.resize((28, 28))
    img_temp = np.array(img_temp)
    img_temp = img_temp.flatten()
    output = model.predict([img_temp])
    if(output[0] == 0):
        prediction.set("Segiempat")
        print("Segiempat")
    elif(output[0] == 1):
        prediction.set("Segitiga")
        print("Segitiga")
    elif(output[0] == 2):
        prediction.set("Lingkaran")
        print("Lingkaran")
    print(output)

def start_draw(event):
    global last_point 
    last_point = (event.x, event.y)

def clear_canvas(event):
    global tkImage, img, draw
    img = Image.new(mode="1", size=(500, 500), color=0)
    draw = ImageDraw.Draw(img)
    tkImage = ImageTk.PhotoImage(img)
    canvas['image'] = tkImage
    canvas.pack()

segiempat = 0
segitiga = 0
lingkaran = 0

def save_image(event):
    global segiempat, segitiga, lingkaran
    img_temp = img.resize((28, 28))
    if (event.char == "k"):
        img_temp.save(f"segiempat/{segiempat}.png")
        segiempat += 1
    elif (event.char == "s"):
        img_temp.save(f"segitiga/{segitiga}.png")
        segitiga += 1
    elif (event.char == "l"):
        img_temp.save(f"lingkaran/{lingkaran}.png")
        lingkaran += 1

window.bind("<B1-Motion>", draw_image)
window.bind("<ButtonPress-1>", start_draw)
window.bind("<ButtonPress-3>", clear_canvas)
window.bind("<Key>", save_image)


label = tk.Label(window, textvariable=prediction)
label.pack()

window.mainloop()
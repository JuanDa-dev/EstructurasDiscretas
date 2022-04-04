from tkinter import *
import sys
import os


#from main import getData

from numpy import var


sw = 0


def btn_clicked():

    d = data.get()
    d1 = data1.get()
    d2 = data2.get()
    d3 = data3.get()
    sw = 1


def setD():

    d = data.get()
    d1 = data1.get()
    d2 = data2.get()
    d3 = data3.get()

    return d, d1, d2, d3


window = Tk()

window.geometry("285x450")
window.configure(bg="#799cf4")
canvas = Canvas(
    window,
    bg="#799cf4",
    height=450,
    width=285,
    bd=0,
    highlightthickness=0,
    relief="ridge")

background_img = PhotoImage(file="Entrega1/Assets/background.png")
'''label = Label(
    window,
    image=background_img
)
label.place(x=0, y=0)'''

data = IntVar()
data1 = IntVar()
data2 = IntVar()
data3 = IntVar()


canvas.pack(expand=True, fill=BOTH)

canvas.create_image(0, 0, image=background_img, anchor="nw")

canvas.create_text(145, 55,
                   text="Digite la cantidad de submarinos",
                   fill="#ffffff",
                   font=("IM_FELL_French_Canon_SC", int(14.0)))

entry0_img = PhotoImage(file=f"Entrega1/Assets/img_textBox0.png")
entry0_bg = canvas.create_image(
    145, 80,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0,
    textvariable=data)


entry0.place(
    x=50, y=70,
    width=195.0,
    height=23)

canvas.create_text(
    145, 110,
    text="Digite la cantidad de cruceros",
    fill="#ffffff",
    font=("IM_FELL_French_Canon_SC", int(14.0)))

entry1_bg = canvas.create_image(
    145, 135,
    image=entry0_img)

entry1 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0,
    textvariable=data1)

entry1.place(
    x=50, y=125,
    width=195.0,
    height=23)

canvas.create_text(
    145, 175,
    text="Digite la cantidad de destructores\n",
    fill="#ffffff",
    font=("IM_FELL_French_Canon_SC", int(14.0)))


entry2_bg = canvas.create_image(
    145, 200,
    image=entry0_img)

entry2 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0,
    textvariable=data2)

entry2.place(
    x=50, y=190,
    width=195.0,
    height=23)

canvas.create_text(
    145, 235,
    text="Digite la cantidad de portaaviones",
    fill="#ffffff",
    font=("IM_FELL_French_Canon_SC", int(14.0)))

entry3_img = PhotoImage(file=f"Entrega1/Assets/img_textBox3.png")
entry3_bg = canvas.create_image(
    145, 265,
    image=entry3_img)

entry3 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0,
    textvariable=data3)

entry3.place(
    x=50, y=255,
    width=195.0,
    height=23)

img0 = PhotoImage(file=f"Entrega1/Assets/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    bg="#799cf4",
    highlightthickness=0,
    command=btn_clicked,
    relief="flat",
    activebackground="#799cf4")


b0.place(
    x=94, y=300,
    width=98,
    height=28)


'''window.resizable(False, False)
window.mainloop()'''


def display_window():
    window.resizable(False, False)
    window.mainloop()

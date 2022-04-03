from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("285x303")
window.configure(bg="#799cf4")
canvas = Canvas(
    window,
    bg="#799cf4",
    height=303,
    width=285,
    bd=0,
    highlightthickness=0,
    relief="ridge")
background_img = PhotoImage(file="Entrega1/Assets/background_.png")


data = IntVar()


canvas.pack(expand=True, fill=BOTH)

canvas.create_image(0, 0, image=background_img, anchor="nw")

canvas.create_text(
    145, 55,
    text="Coordinates X,Y",
    fill="#ffffff",
    font=("IM_FELL_French_Canon_SC", int(14.0)))

canvas.create_text(
    145, 90,
    text="Write the coordinates of the shot",
    fill="#ffffff",
    font=("IM_FELL_French_Canon_SC", int(14.0)))

canvas.create_text(
    145, 120,
    text="Example :  4 5 ",  # (The coordinates need a space between then)
    fill="#ffffff",
    font=("IM_FELL_French_Canon_SC", int(16.0)))


entry0_img = PhotoImage(file=f"Entrega1/Assets/img_textBox0.png")
entry0_bg = canvas.create_image(
    145, 150,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry0.place(
    x=50, y=140,
    width=195.0,
    height=23)


img0 = PhotoImage(file=f"Entrega1/Assets/img0_.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    bg="#799cf4",
    highlightthickness=0,
    command=btn_clicked,
    relief="flat",
    activebackground="#799cf4")

b0.place(
    x=92, y=200,
    width=98,
    height=28)


'''







'''

window.resizable(False, False)
window.mainloop()

from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()

    Canvas.itemconfig(canvasbtn,text=data["quote"])

    #Write your code here.



window = Tk()
window.config(padx=20,pady=20)
Canvas = Canvas(width=300,height=414)

background = PhotoImage(file="./background.png")
Canvas.create_image(150,207, image= background)
canvasbtn = Canvas.create_text(150,207,text="",width=250, font=("Ariel",10,"bold"))
Canvas.grid(row=0,column= 0)

kanyebtn = PhotoImage(file="./Kanye.png")
Kanye_btn = Button(image=kanyebtn, command=get_quote)
Kanye_btn.grid(row= 1, column=0)
window.mainloop()
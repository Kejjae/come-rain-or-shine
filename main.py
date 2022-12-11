"""come-rain-or-shine"""
from tkinter import*
import requests
from PIL import ImageTk,Image
from tkinter import messagebox
from time import strftime
import math
from datetime import datetime

window = Tk()
window.geometry('800x400')
window.iconbitmap('ok.ico')
window.title("Weather")
window.resizable(0,0)

try:

    # Mechenism

    def weather_data(query):
        """ weather data """

        res = requests.get('http://api.openweathermap.org/data/2.5/weather?' + #อาจแก้อีก
                           query+'&appid=06c921750b9a82d8f5d1294e1586276f')
        return res.json()

    # Body UI
    Frame(window, width=800, height=50, bg='#353535').place(x=0, y=0)

    # serach bar
    img1 = ImageTk.PhotoImage(Image.open("search.png"))

    def on_enter(e):
        """on enter"""
        city1.delete(0, 'end')
    
    def on_leave(e):
        """on leave"""
        if city1.get() == '':
            city1.insert(0, 'Search City')

    city1 = Entry(window, width=21, fg='white', bg="#353535", border=0)
    city1.config(font=('Goudy Old Style', 16))
    city1.bind("<FocusIn>", on_enter)
    city1.bind("<FocusOut>", on_leave)
    city1.insert(0, 'Search City')
    city1.place(x=540, y=12)

    # date

    timer = datetime.today().strftime('%B')
    up_timer = (timer.upper())
    ddate = datetime.now().month

    now = datetime.now()

    cel = now.strftime('%B')
    month = cel[0:3]

    today = datetime.today()

    date = today.strftime("%d")

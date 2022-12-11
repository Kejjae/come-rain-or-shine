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

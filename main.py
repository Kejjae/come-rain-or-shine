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

def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        tempF = weather['main']['temp']
        tempC = round((int(tempF) - 32) * 0.5556)
        final_str = 'City: %s\nConditions: %s\nTemperature: %s °C'%(city, condition, tempC)
    except:
        final_str = 'There was a problem retrieving that information'
    return final_str

def get_weather(city):
    #weather_key = 'b86245b23ea848abe010da2d64c71464' อาจเปลี่ยนถ้าขอ api key ทัน
    #url = 'https://api.openweathermap.org/data/2.5/weather'

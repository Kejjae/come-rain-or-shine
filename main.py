from tkinter import*
import requests
from PIL import ImageTk,Image
from tkinter import messagebox
from time import strftime
import math
from datetime import datetime

root = tk.Tk()

root.title("Weather App") #Title
root.geometry("600x500") #Window size


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
#https://www.windy.com/13.791/100.585?capAlerts,13.182,100.585,8 แปะๆไว้ก่อน

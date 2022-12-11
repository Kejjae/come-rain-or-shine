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


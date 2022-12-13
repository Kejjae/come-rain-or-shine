"""come-rain-or-shine"""
from tkinter import*
import requests
from PIL import ImageTk,Image
from tkinter import messagebox
from time import strftime
import math
from datetime import datetime

window = Tk()
window.geometry('700x400')
window.iconbitmap('ok.ico')
window.title("come-rain-or-shine")
window.resizable(0,0)

try:
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
    
    def label(timer):
        """ make our label"""
        Frame(width = 500, height = 50, bg = "#353535").place(x = 0, y = 0)
        upperborder = Label(window, text = str(timer), bg = "#353535", fg = "white")  # upper border
        upperborder.config(font = ("Goudy Old Style", 20))
        upperborder.place(x = 22, y = 7)

        city = timer
        query = 'q='+city
        w_data = weather_data(query)
        result = w_data
        try:
            check = "{}".format(result['main']['temp'])
       
        except:
               messagebox.showinfo("", "    City name not found    ")

        cel = (int(float(check)))-273
        weather = ("{}".format(result['weather'][0]['main']))

        global img

        if cel > 10 and weather == "Haze" or weather == "Clear":
            Frame(window, width = 800, height = 350, bg = "#f78954").place(x = 0, y = 50)
            img = ImageTk.PhotoImage(Image.open("sunny2.png"))
            Label(window, image = img, border = 0).place(x = 110, y = 130)
            bcolor = "#f78954"
            fcolor = "white"

        elif cel > 10 and weather == "Clouds":
            Frame(window, width = 800, height = 350, bg = "#7492b3").place(x = 0, y = 50)
            img = ImageTk.PhotoImage(Image.open("cldd.png"))
            Label(window, image = img, border = 0).place(x = 110, y = 130)
            bcolor = "#7492b3"
            fcolor = "white"

        elif cel <= 10 and weather == "Clouds":
            Frame(window, width = 800, height = 350, bg = "#7492b3").place(x = 0, y = 50)
            img = ImageTk.PhotoImage(Image.open("ccold3.png"))
            Label(window, image = img, border = 0).place(x = 110, y = 130)
            bcolor = "#7492b3"
            fcolor = "white"

        elif cel >= 10 and weather == "Rain":
            Frame(window, width = 800, height = 350, bg = "#60789e").place(x = 0, y = 50)
            img = ImageTk.PhotoImage(Image.open("rainny.png"))
            Label(window, image = img, border = 0).place(x = 110, y = 130)
            bcolor = "#60789e"
            fcolor = "white"

        elif cel <= 10 and weather == "Fog" or weather == "Clear":
            Frame(window, width = 800, height = 350, bg = "white").place(x = 0, y = 50)
            img = ImageTk.PhotoImage(Image.open("temp.png"))
            Label(window, image = img, border = 0).place(x = 110, y = 130)
            bcolor = "white"
            fcolor = "black"

        else:
            Frame(window, width = 800, height = 350, bg = "white").place(x = 0, y = 50)
           # img = ImageTk.PhotoImage(Image.open("error.png"))
            label = Label(window, text = weather, border = 0, bg = 'white')
            label.configure(font = (("Microsoft JhengHei UI Light", 18)))
            label.place(x = 160, y = 130)
            bcolor = "white"
            fcolor = "black"

        w_data = weather_data(query)
        result = w_data

        humidity = ("Humidity: {}".format(result['main']['humidity']))
        pressure = ("Pressure: {}".format(result['main']['pressure']))
        up1 = up_timer = ("Wind speed: {} m/s".format(result['wind']['speed']))

        date_month_board = Label(window, text=str(month+"  "+ date),bg=bcolor,fg=fcolor)
        date_month_board.config(font=("Microsoft JhengHei UI Light", 25))
        date_month_board.place(x=295,y=335)          

        data = Label(window, text=str(str(humidity+"%")),bg=bcolor,fg=fcolor)# upper border
        data.config(font=("Microsoft JhengHei UI Light", 15))
        data.place(x=460,y=135)      
        data = Label(window, text=str(str(pressure+" hPa")),bg=bcolor,fg=fcolor)# upper border
        data.config(font=("Microsoft JhengHei UI Light", 15))
        data.place(x=460,y=175)

        data = Label(window, text=str(str(up1)),bg=bcolor,fg=fcolor)# upper border
        data.config(font=("Microsoft JhengHei UI Light", 15))
        data.place(x=460,y=215)

        temp = Label(window, text=str(str(cel) +"°C"),bg=bcolor,fg=fcolor)# upper border
        temp.config(font=("Microsoft JhengHei UI Light", 40))
        temp.place(x=290,y=150)

    label(timer = "Bangkok")

    def cmd1():
        up_timer = str(city1.get())
        label(str(up_timer))

    Button(window, image=img1, command=cmd1, border=0).place(x=648, y=10)

except:

    Frame(window, width=800, height=400, bg='#ffffff').place(x=0, y=0)
    global imgx
    imgx = ImageTk.PhotoImage(Image.open("oninternet2.png"))

    Label(window, image=imgx, border=0).pack(expand=True)  # place(x=100,y=100)

window.mainloop()

import tkinter as tk
import requests
import json
win =tk.Tk()
win.title("Weather")
win.geometry("500x500")
api="your api key"
url="http://api.openweathermap.org/data/2.5/weather?"
def weather():
    location=entry.get()
    answer = url + "appid=" + api + "&q=" + location
    response = requests.get(answer)
    res = response.json()
    if res["cod"] != 404:
        x =res["main"]
        temperature=x["temp"]
        temp=temperature-273.15
        tempc=round(temp,2)
        pre = x["pressure"]
        hum=x["humidity"]
        y=res["weather"]
        weather_description= y[0]["description"]
        label1=tk.Label(win, text=f'temperature (in kelvin unit)={temperature}K,\n'f'temperature (in celsius unit)={tempc}°C,\n'f'atmospheric pressure={pre},\n'f'humidity={hum},\n'f'description={weather_description}')
        label1.grid(row=2,column=0)
    else:
        label2=tk.Label(win, text="Enter a city")
        label2.grid(row=2,column=0)
label = tk.Label(win,text="Enter a city name here:", bg='#add8e6')
label.grid(row=0,column=0)
label.config(font=("times",20,"bold"))

entry = tk.Entry(win)
entry.grid(row=1,column=0,padx=100)
button = tk.Button(win,text="Search",command=weather)
button.grid(row=1,column=1)
win.mainloop

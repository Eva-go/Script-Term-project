import webbrowser
from tkinter import *
window=Tk()
window.geometry("400x600+750+200")

def map_event():
    url='map.html'

    webbrowser.open(url)
map_butten=Button(window,text="지도열기",command=map_event)
map_butten.grid(row=0,column=0)

window.mainloop()


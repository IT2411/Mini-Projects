#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import tkintermapview
import json
import requests
from PIL import ImageTk,Image


root = Tk()
root.title('')
root.geometry('1250x900')

def add_marker_event(coords):
    map_widget.delete_all_marker()
    city = tkintermapview.convert_coordinates_to_city(coords[0],coords[1])
    new_marker = map_widget.set_marker(coords[0], coords[1], text=city)
    weather_report(city)
    
    
def weather_report(place):
    global temp_label, weather_desc_label, humidity_label
    
    try:
        api_request = requests.get('http://api.weatherstack.com/current?access_key= [YOUR API KEY] &query=New%20York' + place)
        ans = json.loads(api_request.content)
    except Exception as e:
        ans = "Error...."
    
    
    temp = "Temperature in "+ place + " is : " + str(ans['current']['temperature']) + " Celcius"
    weather_desc ="The weather is : " + ", ".join(ans['current']['weather_descriptions'])
    humidity = "The humidity is : " + str(ans['current']['humidity'])
    
    temp_label.config(text=temp)
    weather_desc_label.config(text=weather_desc)
    humidity_label.config(text=humidity)
    

my_frame = LabelFrame(root)
my_frame.pack()

map_widget = tkintermapview.TkinterMapView(my_frame, width=1200, height=800, corner_radius=0)
map_widget.set_position(18.533,73.867)
map_widget.set_zoom(7)

map_widget.add_right_click_menu_command(label="Add Marker",
                                        command=add_marker_event,
                                        pass_coords=True)
map_widget.pack()


temp_label = Label(root)
temp_label.pack()

weather_desc_label = Label(root)
weather_desc_label.pack()

humidity_label = Label(root)
humidity_label.pack()



root.mainloop()


# In[ ]:





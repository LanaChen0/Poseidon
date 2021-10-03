#!/usr/bin/python
# -*- coding: UTF-8 -*-

###Notice: Before send email, 
###Go and Set: https://www.google.com/settings/security/lesssecureapps


import flask
from flask import Flask,request, render_template, url_for
import folium
#from folium.plugins import FastMarkerClusterCr
from folium.plugins import Fullscreen
from folium import FeatureGroup, LayerControl, Map, Marker

import os
import random

import smtplib
from email.mime.text import MIMEText
from datetime import datetime as dt
import pandas as pd
import numpy as np

def SendHighTempEmail():
    print('Start Email')

    #sender id and passward
    gmail_user = "XXX@gmail.com" #sender mail id
    gmail_passwd = "XXX"#sender mail password
    str_messege='Please pay attention. High temperature may cause fire forest.'
    msg = MIMEText(str_messege)#context
    msg['Subject'] = '[No-reply] High Temperature Warning!' #title
    msg['From'] = gmail_user
    msg['To'] = 'XXX@gmail.com' #reciever, set it by user.
    
    #send mail
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(gmail_user, gmail_passwd)
            smtp.send_message(msg)
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)
    print('Email End')
    
    
#Init app
app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    return render_template("homepage.html")

@app.route("/Forests",methods=['POST','GET'])
def result_Forests():
    return render_template("Forests.html")

@app.route("/FireForests",methods=['POST','GET'])
def result_FireForests():
    
    #Draw these stations temperature on maps by NASA.
    continents=[
        'Africa','Asia','Europe',\
        'North America','Oceania','South America','Caribbean Islands',\
        'Gulf of Mexico'
        ]
    #[Simulate] NASA data only temperatures, to fix it,
    # we assumed one point of the area as the area.
    l_lat_lon=[
        [1.35,17],[32.865,120],[53.54,28.40],\
        [39.35,111.73],[-35.5,150],[-20.63,-60],[18,-77.30],\
        [23,-80]
    ]
    map=folium.Map(l_lat_lon[4],zoom_start=5)

    #[simulation] Randomly simulate wildfires forests locations in Australia.
    l_wildfire=[]
    l_wildfire.append([-35.5,150])
    for i in range(30):
        l_wildfire.append( [random.uniform(-35,-30),random.uniform(142,151)] )
        folium.Circle(location=l_wildfire[i],radius=3000,color='red',fill=True,fill_opacity=0.5,popup='wildfire:'+str(l_wildfire[i])).add_to(map)

    for i in range(len(continents)):
        df=pd.read_csv('./dataset/NewNASA_temparature/land_'+continents[i]+'.csv')
        l_temperature=list(df['temperature'])
        curr_temperature=l_temperature[-1]#latest month temperature
        #If too high, send_notification_mail.
        if curr_temperature > 1.27:
            SendHighTempEmail()

        map.add_child(folium.Marker(location=l_lat_lon[i],popup='Temperature:'+str(curr_temperature)+' Degree Celius'))

    return map._repr_html_()


@app.route("/Reservoirs",methods=['POST','GET'])
def result_Reservoirs():
    map=folium.Map([-35.5,150],radius=30000,zoom_start=8,color='green',fill=True,fill_opacity=0.5)

    #[simulation] simulate wildfires forests locations in Australia.
    l_wildfire=[]
    l_wildfire.append([-25.5,130])
    for i in range(30):
        l_wildfire.append( [random.uniform(-35,-30),random.uniform(142,151)] )
        folium.Circle(location=l_wildfire[i],radius=3000,color='red',fill=True,fill_opacity=0.5,popup='wildfire:'+str(l_wildfire[i])).add_to(map)

    #[silulatation]#read Contour map data by google maps
    for i in range(1,4):
        if i==1:
            opacity=0.1
        elif i==2:
            opacity=0.3
        else:
            opacity=0.5
        route=pd.read_csv('./dataset/Reservoir/Reservoir_'+str(i)+'.csv',index_col=False)
        l_lat,l_lon=route.iloc[:,0],route.iloc[:,1]
        route=[]
        for lat,lon in zip(l_lat,l_lon):
            route.append([lat,lon])
        folium.Polygon(route,color='blue',fill=True,fill_opacity=opacity,popup='Reservoir').add_to(map)
    
    return map._repr_html_()

@app.route("/Whales",methods=['POST','GET'])
def result_Whales():
    taiwan=[23.58,121.58]#Taiwan, our hometown.
    
    #Read temperature data and display them on maps.
    map=folium.Map(taiwan,zoom_start=7)

    #[simulation] simulate whales swimming routes.
    df=pd.read_csv('dataset/WhalesRoute/WhalesRoute.csv',index_col=False)
    lat,lon=df['lat'],df['lon']
    route=[]
    for la,lo in zip(lat,lon):
        route.append( [la,lo] )

    for point in route:
        size=random.randint(5000,30000)
        if size > 20000:
            color='red'
        elif size > 10000:
            color='yellow'
        else:
            color='green'
        folium.Circle(location=point,radius=size,color=color,fill=True,fill_opacity=0.5,popup='whale route').add_to(map)
    

    return map._repr_html_()



@app.route("/AboutUs",methods=['POST','GET'])
def AboutUs():
    return render_template("AboutUs.html")

#Run Server
if __name__=="__main__":
    app.run('0.0.0.0', 5000,debug=True)
    
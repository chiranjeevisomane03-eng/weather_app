import requests
import streamlit as st
import time
import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("WEATHER_API_KEY")
st.image(r"D:\CSE ENG\My projects\home_logo.jpg",width="content")
with st.sidebar:
    st.image(r"logo.png", width=180)


city_name=st.text_input("Enter the Location ",placeholder="eg Virginia,Arizona,New-York")
request=requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=yes")
data=request.json()
#Data Extraction
if(request.status_code==200):
    with st.skeleton(height=100):
          time.sleep(2)
          st.success("✅ Location located in the database",icon="spinner",title="Live")
    weather_status=data["current"]["condition"]["text"]
    wind_speed=data["current"]["wind_kph"]
    temperature=data["current"]["temp_c"]
    feels_like=data["current"]["feelslike_c"]
    pressure_HG=data["current"]["pressure_in"]
    humidity=data["current"]["humidity"]
    a,b,c=st.columns([1,1,1])
    with a:
        st.metric(label="Temperature",value=f"{temperature}°C")

    with b:
         st.metric(label="Feels like",value=f"{feels_like}°C")

    with c:
         st.metric(label="Wind Speed",value=f"{wind_speed} km/h")
    p,q,r=st.columns([1,1,1])
    with p:
       st.image(f"https:{data["current"]["condition"]["icon"]}")
       code = data["current"]["condition"]["code"]
       if code == 1000:
              st.markdown("☀️ **Sunny / Clear**")
       elif code == 1003:
              st.markdown("⛅ **Partly cloudy**")
       elif code == 1006:
              st.markdown("☁️ **Cloudy**")
       elif code == 1009:
              st.markdown("☁️ **Overcast**")

       elif code == 1030:
              st.markdown("🌫️ **Mist**")
       elif code == 1135:
              st.markdown("🌫️ **Fog**")
       elif code == 1147:
              st.markdown("❄️ **Freezing fog**")

       elif code == 1063:
              st.markdown("🌦️ **Patchy rain possible**")
       elif code == 1072:
              st.markdown("🌧️ **Patchy freezing drizzle possible**")
       elif code == 1150:
              st.markdown("🌧️ **Patchy light drizzle**")
       elif code == 1153:
              st.markdown("🌧️ **Light drizzle**")
       elif code == 1168:
              st.markdown("🌧️ **Freezing drizzle**")
       elif code == 1171:
              st.markdown("🌧️ **Heavy freezing drizzle**")
       elif code == 1180:
              st.markdown("🌦️ **Patchy light rain**")
       elif code == 1183:
              st.markdown("🌧️ **Light rain**")
       elif code == 1186:
              st.markdown("🌧️ **Moderate rain at times**")
       elif code == 1189:
              st.markdown("🌧️ **Moderate rain**")
       elif code == 1192:
              st.markdown("🌧️ **Heavy rain at times**")
       elif code == 1195:
              st.markdown("🌧️ **Heavy rain**")
       elif code == 1198:
              st.markdown("🌧️ **Light freezing rain**")
       elif code == 1201:
              st.markdown("🌧️ **Moderate or heavy freezing rain**")
       elif code == 1240:
              st.markdown("🌦️ **Light rain shower**")
       elif code == 1243:
              st.markdown("🌧️ **Moderate or heavy rain shower**")
       elif code == 1246:
              st.markdown("⛈️ **Torrential rain shower**")
       elif code == 1066:
              st.markdown("🌨️ **Patchy snow possible**")
       elif code == 1069:
              st.markdown("🌨️ **Patchy sleet possible**")
       elif code == 1087:
              st.markdown("🌩️ **Thundery outbreaks possible**")
       elif code == 1204:
              st.markdown("🌨️ **Light sleet**")
       elif code == 1207:
              st.markdown("🌨️ **Moderate or heavy sleet**")
       elif code == 1210:
              st.markdown("🌨️ **Patchy light snow**")
       elif code == 1213:
              st.markdown("🌨️ **Light snow**")
       elif code == 1216:
              st.markdown("🌨️ **Patchy moderate snow**")
       elif code == 1219:
              st.markdown("🌨️ **Moderate snow**")
       elif code == 1222:
              st.markdown("🌨️ **Patchy heavy snow**")
       elif code == 1225:
              st.markdown("❄️ **Heavy snow**")
       elif code == 1237:
              st.markdown("🧊 **Ice pellets**")
       elif code == 1249:
              st.markdown("🌨️ **Light sleet showers**")
       elif code == 1252:
              st.markdown("🌨️ **Moderate or heavy sleet showers**")
       elif code == 1255:
              st.markdown("🌨️ **Light snow showers**")
       elif code == 1258:
              st.markdown("❄️ **Moderate or heavy snow showers**")
       elif code == 1261:
              st.markdown("🧊 **Light showers of ice pellets**")
       elif code == 1264:
              st.markdown("🧊 **Moderate or heavy showers of ice pellets**")
       elif code == 1273:
              st.markdown("⛈️ **Patchy light rain with thunder**")
       elif code == 1276:
              st.markdown("⛈️ **Moderate or heavy rain with thunder**")
       elif code == 1279:
              st.markdown("🌩️ **Patchy light snow with thunder**")
       elif code == 1282:
              st.markdown("🌩️ **Moderate or heavy snow with thunder**")
    with q:
       st.metric(label="Atmospheric Pressure",value=f"{pressure_HG}mm")
    with r:
       st.metric(label=" Relative Humidity", value=f"{humidity}%")
elif(request.status_code!=200):
      with st.skeleton():
            time.sleep(10)
            st.error("🚨Could not find the location in database \n"+"Please check name and try again")
      


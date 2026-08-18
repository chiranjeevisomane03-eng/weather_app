import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import time
import os
import requests
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")
st.image(r"D:\CSE ENG\My projects\home_logo.jpg",width="content")
location=requests.get("http://ip-api.com/json/")
address=location.json()
if(address["status"]=="success"):
    with st.skeleton():
        time.sleep(1)
    st.success("✅"+"Location Detected!",icon="spinner",title="Live")
request=requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={address["city"]}&aqi=yes")
request=request.json()
a,c,d=st.columns([1.9,1.5,1.5])
with a:
    st.subheader(f"Country-{address["country"]}")
    st.subheader(f"State-{address["regionName"]}")
    st.subheader(f"City-{address["city"]}")

with c:
    st.metric("Temperature",value=f"{request["current"]["temp_c"]}°C")
    st.metric("Relative humidity",value=f"{request["current"]["humidity"]}%")

with d:
    st.metric("Feels Like",value=f"{request["current"]["feelslike_c"]}°C")
    st.image(f"https:{request["current"]["condition"]["icon"]}")
    code = request["current"]["condition"]["code"]
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
    







with st.sidebar:
    st.image(r"logo.png", width=180)
    st.link_button("Source","https://www.weatherapi.com/",width="stretch")
    st.button("Buy me a coffee",width="stretch")
    time.sleep(0.5)
#python -m streamlit run home.py
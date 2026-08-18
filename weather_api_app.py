import requests
import sys
print("WELCOME to the WEATHER API   ------POWERED BY OPEN METEO"+"\n")
city_name=str(input("Please enter the City who's you want to fetch geographical details-"))
request=requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}")
data=request.json()
if("results" in data):
    inner_Data=data["results"]
else:
    sys.exit("\n"+"The city which you tried to look is not present in our database..."+"\n"+"The program will be terminated")
    



#ACTUAL USEFUL SHIT
refined_data=inner_Data[0]
lat=float(refined_data["latitude"])
long=float(refined_data["longitude"])
elevation=float(refined_data["elevation"])
weather_info=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m")
final_data=weather_info.json()
print(f"The following are the geographical details of {city_name}:"+"\n")
print(f"The current temperature is :{final_data["current"]["temperature_2m"]}"+"°C")
print(f"The latitude is :{lat}")
print(f"The longitude is :{long}")
print(f"Elevation from sea is :{elevation}")
print(f"The timezone is:{final_data["timezone"]}")






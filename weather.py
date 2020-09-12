# importing requests,json and datetime
import requests, json, datetime
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

#this should be locations selected by the user......VERY IMPORTANT
Location = "singapore"
API_KEY = 
URL = BASE_URL + "q=" + Location + "&appid=" + API_KEY

# HTTP request
response = requests.get(URL)

# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
  
   # getting the main dict block
   main = data['main']

   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # getting the timezones
   timeZone = data['timezone']
   zone = res = datetime.timedelta(seconds = timeZone)

 #  weather report
   report = data['weather'][0]

   print("Location: {}".format(Location))
   print("UTC Timezone: {}".format(zone))
   print('Temperature: {}'.format(temperature))
   print("Humidity: {}".format(humidity))
   print("Pressure: {}".format(pressure))
   print("Weather Report: {}".format(report['description']))
else:
   # showing the error message
   print("Error in the HTTP request")








# coding: utf-8

# In[4]:


# Python program to find current weather details of any city using openweathermap api 
  
# import required libraries for this program 
import requests, json
    
# provide city name as input to check the temperature.
City_Name=input("Enter the name of the city : ")

# use the openweathermp API along with City_Name for which we need to check temperature.
URL = "http://api.openweathermap.org/data/2.5/weather?"+"&q="+City_Name+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric'

# get method of requests module return response object 
URL_Response = requests.get(URL)

# json method of response object convert json format data into python format data 
Python_Response = URL_Response.json()

# Now Python_Response contains list of nested dictionaries 
# Check the value of "cod" key, if it is not equal to "404", means city is found otherwise, city is not found 
if Python_Response["cod"] != "404": 
    # store the value of "main" key in variable y
    y = Python_Response["main"]
    # store the value corresponding to the "temp" key of y 
    current_temperature = y["temp"]
    # print the temperature value
    print(" Temperature = " + str(current_temperature))
else: 
    print(" City Not Found ") 


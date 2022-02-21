from ctypes import sizeof
import requests as rq
import numpy as np
import os 
os.system("cls") # Clear screen

# Peticion a la PAIS
url = "https://context-airis.apsevilla.com/v2/entities/"
#querystring = {"type":"SeaConditionsForecast","limit":"72","attrs":"waterLevel,tide","q":"name==Chipiona-Sevilla","options":"values"}
querystring = {"type":"TideModel","limit":"72","attrs":"waterLevel,tide","q":"name==Chipiona-Sevilla","options":"values"}
payload = ""
response = rq.request("GET", url, data=payload, params=querystring)


A = np.array(response.json())

print(A)
#R = A[:,0]-A[:,1]

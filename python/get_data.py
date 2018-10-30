
# importing the requests library 
import requests 
import json
   
# api-endpoint 
URL = "https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json"

#callsign for the flight you want to pull data for   
callsign= "N65620"  

# defining a params dict for the parameters to be sent to the API (I am filtering by a specific callsign)
PARAMS = {'fCall': callsign}  
   
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 

#writing to a local file
filename= callsign +".txt"
with open(filename, 'w') as outfile:  
    json.dump(data, outfile)
  

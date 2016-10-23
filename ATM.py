import requests
import json
import secrets

url = 'http://api.reimaginebanking.com'
key = 'key={}'.format(secrets.API_KEY)
response="sdkjfa"

def get_ATM(atm_info): 
    #while(len(response.json())["data"]==0):
    """
    closest_ATMs={
    "lat": 0
    "lng": 0
    "rad": 0
  }
  """
    urj='/atms?'
    uri="lat="+str(atm_info["lat"])+"&"
    urk="lng="+str(atm_info["lng"])+"&"
    urm="rad="+str(atm_info["rad"])+"&"
    actual_url=url+urj+uri+urk+urm+key
    response=requests.get(actual_url, json=atm_info)
    print 'atm'
    print response.json()
    print response.json()["data"]
    print len(response.json()["data"])

    if len(response.json()["data"]) == 0:
        print ("increase rad size")
        if len(response.json()["data"])==0 and atm_info["rad"] >= 25:
            print("There is no ATM near your location")
    return response.json()["data"]
  

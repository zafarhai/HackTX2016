import requests
import json

url = 'http://api.reimaginebanking.com'
key = 'key={}'.format(secrets.API_KEY)
response

def get_ATM(account_info): 
  do{
	"""
  	urj='/atms?'
  	closest_ATMs={
    "lat": 0
    "lng": 0
    "rad": 0
  }
  """
  uri="lat="+closest_ATMs["lat"]+"&"
  urk="lng="+closest_ATMs["lng"]+"&"
  urm="rad="+closest_ATMs.["rad"]+"&"
  actual_url=url+urj+uri+urk+urm+key
  response=requests.get(actual_url, json=closest_ATMs)
  if(len(response.json())["data"]==0)
  print ("increase rad size")
  if(len(response.json())["data"]==0&&closest_ATMs["rad"]>=25):
    print("There is no ATM near your location")
    break
  while(len(response.json())["data"]==0)
  return response.json()
  }
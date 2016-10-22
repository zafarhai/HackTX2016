import requests
import json

url = 'http://api.reimaginebanking.com'
key = '?key={}'.format(secrets.API_KEY)

def post_account(account_info): 
	"""
  	urj='/customers'
  	account_info={
    "_id": "string",
    "type": "Credit Card",
    "nickname": "string",
    "rewards": 0,
    "balance": 0,
    "account_number": "string",
    "customer_id": "string"
  }
  """
  actual_url=url+urj+key
  response=requests.post(actual_url, json=account_info)
  return response.json()

def get_account(customer_id=None):
	accounts = []
    uri = '/accounts'

    if customer_id is None:
        actual_url = url+uri+key
        reqeust = requests.get(actual_url)
        for a in request.json():
            print "id: {0}\n\tname: {1} {2}".format(a['_id'], a['first_name'], a['last_name'])
            accounts.add(a)

    else:
        for id in ids:
            id_uri = "{0}/{1}".format(uri, str(id))
            actual_url = url+id_uri+key
            request = requests.get(actual_url)
            for a in request.json():
                accounts.add(a)

    return accounts

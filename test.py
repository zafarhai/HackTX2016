
import requests
import json

import secrets

url = 'http://api.reimaginebanking.com'
key = '?key={}'.format(secrets.API_KEY)


def post_customer(info):
    uri = '/customers'

    """
    info = {
        "first_name": cust["string2",
        "last_name": "string2",
        "address": {
            "street_number": "string2",
            "street_name": "string",
            "city": "string",
            "state": "TX",
            "zip": "78705"
            }
    """
    final_url = url+uri+key
    res = requests.post(final_url, json=info)
    return res.json()
}

final_url = url+uri+key
req = requests.post(final_url, json=info)
print req.json()
print req
print ''

def get_customers(ids=None):

req = requests.get(final_url)
for a in req.json():
    print "id: {0}\n\tname: {1} {2}".format(a['_id'], a['first_name'], a['last_name'])

#print req.json()
print req


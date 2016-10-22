
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
        }
    """
    final_url = url+uri+key
    res = requests.post(final_url, json=info)
    return res.json()


def get_id(f_name, l_name):
    customers = get_customers()
    id = None
    for c in customers:
        if c['first_name'] == f_name and c['last_name'] == l_name:
            id = c['_id']

    return id


def get_customers(ids=None):
    customers = []
    uri = '/customers'

    if ids is None:
        final_url = url+uri+key
        req = requests.get(final_url)
        for a in req.json():
            print "id: {0}\n\tname: {1} {2}".format(a['_id'], a['first_name'], a['last_name'])
            customers.add(a)

    else:
        for id in ids:
            id_uri = "{0}/{1}".format(uri, str(id))
            final_url = url+id_uri+key
            req = requests.get(final_url)
            for a in req.json():
                customers.add(a)

    return customers



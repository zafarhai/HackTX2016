
from flask import Flask
from flask import session, request, jsonify
from flask import render_template, url_for, redirect
app = Flask(__name__)

from test import *
from accounts import *
#import ATM

@app.route("/")
def hello():
    return redirect(url_for('login')) 

@app.route("/login", methods=['GET','POST'])
def login():
    
    if request.method == 'GET':
	return render_template('login.html')

    if request.method == 'POST':

    	fname = request.form.get("firstname")
    	lname = request.form.get("lastname")

        _id = get_id(fname, lname)
        if _id is None:
            return redirect(url_for('register'))
        else:
            customer = get_customers([_id])[0] 
            print 'login customer'
            print customer
            return redirect(url_for('customer', _id = customer['_id']))
    	print fname

@app.route("/register", methods=['GET', 'POST'])
def register():

    if request.method == 'GET':
        return render_template('register.html') 

    if request.method == 'POST':
        fname = request.form.get("firstname")
        lname = request.form.get("lastname")
        street_number = request.form.get("street_number")
        street_name = request.form.get("street_name")
        city = request.form.get("city")
        state = request.form.get("state")
        zipcode = request.form.get("zip")

        address = {
            "street_number": street_number,
            "street_name": street_name,
            "city": city,
            "state": state,
            "zip": zipcode 
            }
        info = {
            "first_name": fname,
            "last_name": lname,
            "address": address            
            }

        customer = post_customer(info) 
        print(customer)
        
        return redirect(url_for('customer', _id = customer['_id']))

@app.route("/customer/<_id>")
def customer(_id):
     
    if request.method == 'GET':
        print _id
        customer = get_customers([_id])[0] 
        print 'customer'
        print customer
        accounts = get_account_by_customer(customer['_id']) 

        return render_template('customer.html', customer = customer, accounts = accounts)

    if request.method == 'POST':
        account_type = request.form.get("account_type")
        nickname = request.form.get("nickname")
        rewards = request.form.get("rewards")
        balance = request.form.get("balance")
        account_number = request.form.get("account_no")

  	account_info={
            "type": account_type,
            "nickname": nickname,
            "rewards": rewards,
            "balance": balance,
            "account_number": account_number,
          }

        account = post_account(_id, account_info) 

        return redirect(url_for('customer', _id=_id))

@app.route("/accounts/<_id>")
def account(_id):

    if request.method == 'GET':
        account = get_account_by_id(_id)
        return render_template('account.html', account = account)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

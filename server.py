
from flask import Flask
from flask import session, request, jsonify
from flask import render_template, url_for, redirect
app = Flask(__name__)

import test
import accounts
import ATM

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

		id = test.get_id(fname, lname)
		if id is None:
			return redirect(url_for('register'))
		else:
			customer = test.get_customers([id])[0] 
			return redirect(url_for('customer'), id = customer['_id'])
		print (fname)

@app.route("/register")
def register():

    if request.method == 'GET':
        render_template('register.html') 

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
        
        return redirect(url_for('customer'), id = customer['_id'])

@app.route("/customer/{id}")
def customer():
     
    if request.method == 'GET':
        customer = test.get_customers([id])[0] 
        accounts = get_account(customer['_id']) 

        #return render_template('




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

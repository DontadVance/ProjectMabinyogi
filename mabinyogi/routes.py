'''
- This file serves to handle all page routing and will manage passing back and forth information between Flask and the HTML templates

- Each page will be declared by their own function as seen below
'''
from flask import render_template, url_for, redirect
from mabinyogi import app, forms #importing the flask application to specify routes
from mabinyogi.cluster import mage_collection, rogue_collection, warrior_collection

#we define a specific web page route by using the @app.route decorator, think of it as adding a route to our application
@app.route('/')
@app.route('/home') #notice we can specify more than one routing name for the same route
def homepage():
    form = forms.CharacterForm()
    if form.validate_on_submit():
        return redirect(url_for('homepage'))
    return render_template('index.html')

@app.route('/about')
def aboutpage():
	return render_template('about.html')

'''
- This file serves to handle all page routing and will manage passing back and forth information between Flask and the HTML templates

- Each page will be declared by their own function as seen below
'''
from flask import render_template, url_for, redirect
from mabinyogi import app #importing the flask application to specify routes
from mabinyogi.cluster import mage_collection, rogue_collection, warrior_collection
from mabinyogi.forms import CharacterForm

#we define a specific web page route by using the @app.route decorator, think of it as adding a route to our application
@app.route('/', methods=('GET','POST'))
@app.route('/home', methods=('GET','POST')) #notice we can specify more than one routing name for the same route
def homepage():
    form = CharacterForm()
    if form.validate_on_submit():
        return redirect(url_for('homepage'))
    return render_template('index.html', form=form)

@app.route('/about')
def aboutpage():
	return render_template('about.html')

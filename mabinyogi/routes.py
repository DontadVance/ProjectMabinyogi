'''
- This file serves to handle all page routing and will manage passing back and forth information between Flask and the HTML templates

- Each page will be declared by their own function as seen below
'''
from flask import render_template, url_for, redirect, request
from mabinyogi import app #importing the flask application to specify routes
from mabinyogi.cluster import mage_collection, rogue_collection, warrior_collection
from mabinyogi.forms import CharacterForm

#we define a specific web page route by using the @app.route decorator, think of it as adding a route to our application
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')

@app.route('/about')
def aboutpage():
	return render_template('about.html')

@app.route('/create', methods=('GET','POST'))
def createpage():
    form = CharacterForm()
    if form.validate_on_submit():
        warrior_collection.insert({'char_name': request.form.get('char_name'), #temporarily using warrior_collection alone to verify functionality. 
                                'char_race': request.form.get('char_race'),
                                'char_stature': request.form.get('char_stature'),
                                'char_class': request.form.get('char_class')})
        return redirect(url_for('homepage'))
    return render_template('form.html', form=form)

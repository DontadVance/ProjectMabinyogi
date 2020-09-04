'''
- This file serves to handle all page routing and will manage passing back and forth information between Flask and the HTML templates

- Each page will be declared by their own function as seen below
'''
from flask import render_template, url_for, redirect
from mabinyogi import app, cluster #importing the flask application to specify routes
from cluster import mage_collection, rogue_collection, warrior_collection

#we define a specific web page route by using the @app.route decorator, think of it as adding a route to our application
@app.route('/')
@app.route('/home') #notice we can specify more than one routing name for the same route
def homepage():
    return render_template('index.html') #we pass in the HTML file to render, you may change this accordingly
    '''
    -the app will render an HTML template by using the render_template Flask function
    -we must return that render_template function from our page function so that the application may be returned data when calling the page
        o i.e. when the app calls the homepage function to run our home page, it will be returned data from the render_template function
    '''
@app.route('/about')
def aboutpage():
	return render_template('about.html')

# @app.route('/form', methods=('GET', 'POST'))
#def form():
#    form = CharacterForm()
#    if form.validate_on_submit():
#        return redirect(url_for('homepage'))
#	return render_template('form.html')

from flask import ( Blueprint, redirect, render_template, request )
from . import models

# Create the Blueprint instance - Blueprint does our endpoint routing so this will be http://127.0.0.1:5000/facts

bp = Blueprint('fact', __name__, url_prefix="/facts") 

@bp.route('/new') # Point Blueprint to /facts/new.html and our form
def new():
    return render_template('facts/new.html')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        submitter = request.form['submitter'] # Grab submitter name
        fact = request.form['fact'] # Grab the fact from our field for it in form
        
        # print(request.form)

        new_fact = models.Fact(submitter=submitter, fact=fact) # Call on Fact class in models.py thru new_fact variable
        models.db.session.add(new_fact) # Add new fact to our database
        models.db.session.commit()

        return redirect('/facts')

    results = models.Fact.query.all() # Query all of our Facts in the Facts database table and assign to 'results' variable
    # for result in results: # For loop to go thru all facts or results in Facts table and print them
    #     print(result)    

    print(request.form) # Use request object to access user given data on form. Be sure and import request from flask
    return render_template('facts/index.html', facts=results) # Pass facts from database into results variable so template can access


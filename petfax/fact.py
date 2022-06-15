from flask import ( Blueprint, redirect, render_template, request )

# Create the Blueprint instance - Blueprint does our endpoint routing so this will be http://127.0.0.1:5000/facts

bp = Blueprint('fact', __name__, url_prefix="/facts") 

@bp.route('/new') # Point Blueprint to /facts/new.html and our form
def new():
    return render_template('facts/new.html')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')

    print(request.form) # Use request object to access user given data on form. Be sure and import request from flask
    return render_template('facts/index.html')


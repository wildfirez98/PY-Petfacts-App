from flask import ( Blueprint, render_template )

# Create the Blueprint instance - Blueprint does our endpoint routing so this will be http://127.0.0.1:5000/facts

bp = Blueprint('fact', __name__, url_prefix="/facts") 

@bp.route('/new') # Point Blueprint to /facts/new.html and our form
def new():
    return render_template('facts/new.html')
from flask import ( Blueprint, render_template, json )

bp = Blueprint('pet', __name__, url_prefix="/pets") # Create the Blueprint instance

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

pets = json.load(open('pets.json'))
print(pets)
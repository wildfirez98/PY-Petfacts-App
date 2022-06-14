from flask import ( Blueprint, render_template, json )

# Create the Blueprint instance - Blueprint does our endpoint routing so this will be http://127.0.0.1:5000/pets

bp = Blueprint('pet', __name__, url_prefix="/pets") 

pets = json.load(open('pets.json')) # Assign pets.json to a variable named pets

@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def show(id):
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)


print(pets)
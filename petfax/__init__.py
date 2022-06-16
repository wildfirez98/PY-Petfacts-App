from flask import Flask
from flask_migrate import Migrate # Import Migrate tool from package Flask-Migrate so we can migrate our models on the command line

# Create Application factory function

def create_app():
    app = Flask(__name__)

    # Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password1234@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             
    from . import models # Import model.py so we can access 'db' variable
    models.db.init_app(app) # We now have access to all the built-in SQLAlchemy class methods through models.db. Call the init_app method on it and pass it the app instance.
    migrate = Migrate(app, models.db) # Create migrate variable

    # Routes

    @app.route('/')
    def hello():
        return "Hello, PetFacts!"

    # Register pet blueprint endpoint
    from . import pet
    app.register_blueprint(pet.bp) # Pointing to pet.py on same file level
    
    # Register fact blueprint endpoint
    from . import fact
    app.register_blueprint(fact.bp) # Pointing to fact.py on same file level

    return app


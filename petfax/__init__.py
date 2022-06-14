from flask import Flask

# Create Application factory function

def create_app():
    app = Flask(__name__)

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
    
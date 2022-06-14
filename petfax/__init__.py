from flask import Flask

# Create Application factory function

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, PetFacts!"

    # Register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)
    
    return app
    
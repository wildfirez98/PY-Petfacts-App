# Initial setup without an Application factory
#
# # Flask config setup
# from flask import Flask
# app = Flask(__name__) # Create the 'app' instance

# # Index route
# @app.route('/') # Decorator - specify the route
# def index():
#     return "Hello, this is PetFacts!"

# # Pets index route
# @app.route('/pets')
# def pets():
#     return "These are our pets available for adoption!"

from petfax import create_app # Import __init__.py Application store from petfax folder
app = create_app() # Create app instance so we can use app. etc... thru out program
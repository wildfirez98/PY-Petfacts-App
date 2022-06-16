from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Create a variable named 'db' to our instance of SQLAlchemy class

# Create Class/Model for use with Migrations
class Fact(db.Model):
    __tablename__= 'facts' # Create the table name

    id = db.Column(db.Integer, primary_key=True) # Primary key column for the table
    submitter = db.Column(db.String(250)) # Type is String with a character limit of 250
    fact = db.Column(db.Text)
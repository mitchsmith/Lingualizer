# db_create.py
from app import db
from models import SegmentPrototype

# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()
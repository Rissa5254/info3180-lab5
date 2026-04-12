# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime, timezone

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True )
    title = db.Column(db.String(128))
    description = db.Column(db.Text)
    poster = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

    def __repr__(self):
        return '<Movie %r>' % (self.title)
            
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, ForeignKey, DateTime, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from datetime import datetime

DATABASE_URL = 'postgresql:///blogly_users_db'

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models
class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(String(50), nullable=False, unique=True)
    last_name = db.Column(String(50), nullable=False, unique=True)
    image_url = db.Column(String(255), nullable=True, default='/static/default_icon.png')
    
    def __repr__(self):
        return f"<User id={self.id} first_name={self.first_name} last_name={self.last_name} image_url={self.image_url}>"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    title = db.Column(String(50), nullable=False, default='Title')
    content = db.Column(String(), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # Explicitly name the foreign key constraint
    user = db.relationship("User", backref="posts", cascade="all, delete")
    
    def __repr__(self):
        return f"<Post id={self.id} title={self.title} content={self.content} created_at={self.created_at} user_id={self.user_id}>"

class Tag(db.Model):
    __tablename__ = "tags"
    
    id = db.Column(Integer, primary_key=True)
    tag_name = db.Column(String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f"<Tag id={self.id} tag_name={self.tag_name}>"
    
class PostTag(db.Model):
    __tablename__ = "posts_tags"
    
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(Integer, ForeignKey("posts.id"), primary_key=True)
    tag_id = db.Column(Integer, ForeignKey("tags.id"), primary_key=True)

    post = db.relationship("Post", backref="tags", cascade="all, delete")
    tag = db.relationship("Tag", backref="posts", cascade="all, delete")

    def __repr(self):
        return f"<PostTag post_id={self.post_id} tag_id={self.tag_id}>"

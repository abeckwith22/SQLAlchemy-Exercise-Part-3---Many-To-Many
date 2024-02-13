from models import User, Post, Tag, PostTag, db
from app import app

def seed():
    app.app_context().push()

    # Create all tables
    db.drop_all()
    db.create_all()

    users = [
        User(first_name='Alan', last_name='Alda'),
        User(first_name='Joel', last_name='Burton'),
        User(first_name='Jane', last_name='Smith')
    ]

    db.session.add_all(users)
    # Create posts
    posts = [
        Post(title='AITA for blowing up my neighbors car?', content='Lorem Ipsum', user_id=1),
        Post(title='Do you love birds as much as I do?', content='Lorem Ipsum', user_id=1),
        Post(title='Check out this cool underground hospital I found!', content='Lorem Ipsum', user_id=2),
        Post(title='who would win?', content='Lorem Ipsum', user_id=2),
        Post(title='Why is everyone so mean to me?', content='Lorem Ipsum', user_id=3),
        Post(title='I love creating SQL models in python', content='Lorem Ipsum', user_id=3)
    ]
    db.session.add_all(posts)

    tags = [
        Tag(tag_name='travel'),
        Tag(tag_name='food'),
        Tag(tag_name='fitness'),
        Tag(tag_name='fashion'),
        Tag(tag_name='nature'),
        Tag(tag_name='photography'),
        Tag(tag_name='art'),
        Tag(tag_name='music'),
        Tag(tag_name='beauty'),
        Tag(tag_name='pets')    
    ]

    db.session.add_all(tags)

    posts_tags = [
        PostTag(post_id=3, tag_id=8),
        PostTag(post_id=2, tag_id=5),
        PostTag(post_id=6, tag_id=2),
        PostTag(post_id=4, tag_id=7),
        PostTag(post_id=1, tag_id=10),
        PostTag(post_id=5, tag_id=3),
        PostTag(post_id=3, tag_id=6),
        PostTag(post_id=2, tag_id=4),
        PostTag(post_id=1, tag_id=1),
        PostTag(post_id=6, tag_id=4)
    ]

    db.session.add_all(posts_tags)

    db.session.commit()


if __name__ == '__main__':
    seed()
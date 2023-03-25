from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(238),nullable=False)

#creating the tweet table 
class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(280), nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)

#creating a like reletionship between user and tweet(many to many)

likes_table = db.Table(
    'likes',
    db.Column(
    'user_id',db.Integer,
    db.ForeignKey('users.id'),
    primary_key=True
    ),
    db.Column(
    'tweet_id',db.Integer,
    db.ForeignKey('tweets.id'),
    primary_key=True
    ),
    db.Column(
    'created_at',db.Integer,
    default=datetime.datetime.utcnow,
    nullable=False
    )
)

#back references 
tweets = db.relationship('Tweet', backref='user',cascade="all,delete")

liking_users = db.relationship(
    'user', secondary = likes_table,
    lazy= 'subquery' ,
    backref = db.backref('liked_tweets',lazy=True)
)
from flask import Blueprint, jsonify, abort, request
from ..models import Tweet, User,db


bp = Blueprint('tweets',__name__, url_prefix='/tweets')

@bp.route('', methods=['GET'])
def index():
    tweets = Tweet.query.all()
    result = []
    for t in tweets:
        result.append(t.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Tweet.query.get_or_404(id)
    return jsonify(t.serialize())



@bp.route('', methods=['POST'])
def create():
    #req body must contain user_id and content 
    if 'user_id' not in request.json or 'content' not in request.json:
        return abort(400)
    
    #user with id of user_id must exist 
    User.query.get_or_404(request.json['user_id'])
    #contruct Tweet
    t = Tweet(
        user_id=request.json['user_id'],
        content=request.json['content']
    )
    db.session.add(t)
    db.session.commit()

    return jsonify(t.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    t = Tweet.query.get_or_404(id)
    try:
        db.session.delete(t) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>/liking_users', methods=['GET'])
def liking_users(id: int):
    t = Tweet.query.get_or_404(id)
    result = []
    for u in t.liking_users:
        result.append(u.serialize())
    return jsonify(result)
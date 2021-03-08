from app import app
from flask import request, jsonify
from app.models import user_schema

user = user_schema.User()

@app.route("/")
def get_initial_response():
    """Welcome message for the API."""
    # Message to the user
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Flask API'
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    return resp


@app.route("/api/v1/users", methods=['POST'])
def create_user():
    try:
        # Create new users
        if request.method == "POST":
            response =  user.create(request.json)
            return response, 201
    except SystemError:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "", 500


@app.route("/api/v1/users/<string:user_id>/", methods=['GET'])
def fetch_users(user_id):
    try:
        # Create new users
        if request.method == "GET":
            return user.find_by_id(user_id), 200
    except SystemError:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "", 500

@app.route("/api/v1/users/<string:user_id>", methods=['PUT'])
def update_user(user_id):
    try:
        # Create new users
        if request.method == "PUT":
            response =  user.update(request.json)
            return response, 201
    except SystemError:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "", 500

@app.route("/api/v1/users/<string:user_id>", methods=['DELETE'])
def remove_user(user_id):
    if request.method == "DELETE":
        user.delete(user_id)
        return "Record Deleted"


@app.errorhandler(404)
def page_not_found(e):
    """Send message to the user with notFound 404 status."""
    # Message to the user
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp
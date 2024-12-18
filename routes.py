from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/search', methods=['GET'])
def search():
    return jsonify({"message": "API is working!"})

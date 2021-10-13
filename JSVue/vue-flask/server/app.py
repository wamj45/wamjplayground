from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

COURSES = [
    {
        'title': 'Effective JavaScript: 68 Specific Ways to Harness the Power of JavaScript ',
        'author': 'David Herman',
        'paperback': True
    },
    {
        'title': 'JavaScript: The Good Parts',
        'author': 'Douglas Crockford',
        'paperback': False
    },
    {
        'title': 'Eloquent JavaScript: A Modern Introduction to Programming',
        'author': 'Marijn Haverbeke',
        'paperback': True
    }
]


@app.route('/courses', methods=['GET'])
def all_courses():
    return jsonify({
        'status': 'success',
        'courses': COURSES
    })


if __name__ == '__main__':
    app.run()

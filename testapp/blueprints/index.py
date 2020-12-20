from flask import render_template, Blueprint, jsonify


TestIndex = Blueprint('TestIndex', __name__, template_folder='templates')


@TestIndex.route('/', defaults={'path': 'index.html'})
@TestIndex.route('/<path>')
def index(path):

    try:
        return render_template('layouts/default.html', content=render_template('index.html'))
    except:
        return render_template('layouts/other-default.html', content=render_template('404.html'))


@TestIndex.route('/testing')
def testing():
    return jsonify({"message": 'Testing!!! Hello :)'})

from sherlock import app
from flask import render_template
from flask import request
from flask import jsonify


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze_text', methods = ['POST'])
def analyze_text():
    return jsonify(
        data = request.get_data(as_text=True)
    )
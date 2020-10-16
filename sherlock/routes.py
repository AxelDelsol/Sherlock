from sherlock import app
from flask import render_template
from flask import request
from flask import Response
from flask import jsonify
from sherlock.analyzer import get_people_from_text, AnalysisException


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze_text', methods = ['POST'])
def analyze_text():
    try:
        people = get_people_from_text(request.get_data(as_text=True))
        # people_info = get_information_from(people)
        # people_link = get_link_information_from(people)
        # return jsonify(info=people_info, link=people_link);
        return jsonify(
            data = people
            )
    except AnalysisException as ex:
        return jsonify(
            message = ex.message, 
            status = ex.status, 
            mimetype='application/json'
        )
    
    
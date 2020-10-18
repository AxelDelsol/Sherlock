from sherlock import app
from flask import render_template, request, Response, jsonify
from sherlock.analyzer import get_people_from_text, AnalysisException
from sherlock.person import Person, get_information_from
from sherlock.common_fact import CommonFact, find_common_facts_from


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze_text', methods = ['POST'])
def analyze_text():
    try:
        return process_request(request)
    except AnalysisException as ex:
        return process_error(ex)
    
    
def process_request(request):
    people = get_people_from_text(request.get_data(as_text=True))
    people_info = get_information_from(people)
    people_facts = find_common_facts_from(people_info)
    return jsonify(
        people = [p.to_dict() for p in people_info],
        facts =  [f.to_dict() for f in people_facts]
        )

def process_error(ex):
    return jsonify(
            message = ex.message, 
            status = ex.status, 
            mimetype='application/json'
            )
   
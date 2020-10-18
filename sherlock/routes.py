from sherlock import app
from flask import render_template, request, Response, jsonify
from sherlock.analyzer import get_people_from_text, AnalysisException
from sherlock.person import Person, get_information_from
from sherlock.common_fact import CommonFact, find_common_facts_from

# This route allows to easily test the API and analyze a text.
# The output is also printed (Json format).
@app.route('/')
def index():
    return render_template('index.html')


# Main route of the API. Does the following
# 1) Analyze the given text
# 2) Extract people found in the text
# 3) Retrieve information about them
# 4) Find common facts
# 
# If everything goes well (Code 200) :
# JSON string with 2 keys : facts and people.
# facts is an array of CommonFact.
# CommonFact json keys: attribute, people_concerned (array of wikidata_id), values.
# people is an array of People.
# People json keys : wikidata_id, label, description, first_names (array), last_name, nationality, birthdate, is_alive
# 
# If something failed, the error code and a message explaining the error is returned as a reponse. 
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
   
import textrazor
import re
import os

# This function analyses the text and output a list of wikidata IDs
def get_people_from_text(text):
    textrazor.api_key = os.environ['TEXTRAZOR_API_KEY']
    client = create_client()

    try:
        response = client.analyze(text)
        people = {e.wikidata_id for e in response.entities()}
        return list(people)
    except textrazor.TextRazorAnalysisException as ex:
       raise AnalysisException(str(ex))

    
def create_client():
    client = textrazor.TextRazor()
    client.set_extractors(['entities'])
    client.set_entity_freebase_type_filters(['/people/person'])
    return client


class AnalysisException(Exception):
    def __init__(self, message):
        self.message = message
        self.status = self.status_from_message(message)

    def status_from_message(self, message):
        m = re.search(r"(\d+)", message)
        return int(m.group(0))


import json
import sys
from SPARQLWrapper import SPARQLWrapper, JSON

# Data class to store information about a person.
# Use function create_person_from instead of the constructor to create a Person.
class Person:
    def __init__(self, wikidata_id):
        self.wikidata_id = wikidata_id
        self.label = ""
        self.description = ""
        self.first_names = []
        self.last_name = ""
        self.nationality = ""
        self.birthdate = ""
        self.is_alive = None
        
    # Dictionary representation of a Person (can be used to convert into JSON string)
    def to_dict(self):
        return self.__dict__


# Creates a person from his wikidata_id.
# If something wrong happens (wrong wikidata_id for example), None is returned
def create_person_from(wikidata_id):
    person = Person(wikidata_id)
    endpoint_url = "https://query.wikidata.org/sparql"
    query = create_query_from(wikidata_id)
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()["results"]["bindings"]

    if not result:
        return None

    data = result[0]
    
    person.label       = data["personLabel"]["value"]
    person.description = data["personDescription"]["value"]
    person.first_names  = data["firstNamesLabel"]["value"].split(',')
    person.last_name   = data["lastNameLabel"]["value"]
    person.nationality = data["nationalityLabel"]["value"]
    person.birthdate   = data["birthDateLabel"]["value"]
    person.is_alive    = "deathDateLabel" not in data

    return person

def create_query_from(wikidata_id):
    query_template = """SELECT
?personLabel ?personDescription ?lastNameLabel ?nationalityLabel ?birthDateLabel ?deathDateLabel (GROUP_CONCAT(DISTINCT ?firstNameLabel; SEPARATOR=",") AS ?firstNamesLabel)
WHERE {
  BIND(wd:%s AS ?person).
  ?person wdt:P31 wd:Q5;
          wdt:P735 ?firstName;
          wdt:P734 ?lastName;
          wdt:P27 ?nationality;
          wdt:P569 ?birthDate.
  OPTIONAL { ?person wdt:P570 ?deathDate}.
  SERVICE wikibase:label { 
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en".
      ?person rdfs:label ?personLabel;
              schema:description  ?personDescription.
      ?firstName rdfs:label ?firstNameLabel.
      ?lastName rdfs:label ?lastNameLabel.
      ?nationality rdfs:label ?nationalityLabel.
      ?birthDate rdfs:label ?birthDateLabel.
      ?deathDate rdfs:label ?deathDateLabel.
  }
}
GROUP BY ?personLabel ?personDescription ?lastNameLabel ?nationalityLabel ?birthDateLabel ?deathDateLabel
"""
    return query_template % wikidata_id


def get_information_from(people):
    people_info = []

    for p in people:
        person = create_person_from(p)
        if person:
            people_info.append(person)

    return people_info
from itertools import combinations
from sherlock.person import Person
from collections.abc import Iterable

# Data class to store a common fact between people
class CommonFact:
    def __init__(self, people, attribute, values):
        self.people_concerned = people
        self.attribute = attribute
        self.values = values

    # Dictionary representation of a Person (can be used to convert into JSON string)
    def to_dict(self):
        return self.__dict__

# Tries to find common fact between every pair of person in people.
def find_common_facts_from(people):
    facts = []

    # Combinations returns all pairs
    for (p1, p2) in combinations(people ,2):
        facts.extend(cross_information_between(p1, p2))

    return facts

# Tries to find common facts between 2 instances of the Person class.
# It uses a dictionary representation of a Person (key, value) to be generic.
# If a value is a list (e.g multiple first names), we consider the intersection of the lists as a common fact.
# Otherwise, we compare the values and checks if they are equals.
def cross_information_between(person1, person2):
    facts = []
    person1_dict = person1.to_dict()
    person2_dict = person2.to_dict()

    for (key1,value1) in person1_dict.items():
        if key1 in person2_dict:
            value2 = person2_dict[key1]
            result = None
            if isinstance(value1, list) and isinstance(value2, list):
                result = list(set(value1).intersection(value2))     
            else:
                if value1 == value2:
                    result = [value1]

            if result:
                fact = CommonFact(
                        [person1.wikidata_id, person2.wikidata_id], 
                        key1, 
                        result)
                facts.append(fact)
    return facts
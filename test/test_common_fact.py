import unittest
from sherlock.person import Person, create_person_from
from sherlock.common_fact import CommonFact, find_common_facts_from
import os
import json

class TestCommonFact(unittest.TestCase):

    def test_bob_marley_robert_pattinson_share_first_name(self):
        bob = create_person_from("Q409")
        robert = create_person_from("Q36767")

        facts = find_common_facts_from([bob, robert])

        self.assertEqual(len(facts), 1)
        fact = facts[0]

        self.assertEqual(fact.attribute, "first_names")
        fact.people_concerned.sort()
        self.assertEqual(fact.people_concerned, ["Q36767", "Q409"])
        self.assertEqual(fact.values, ["Robert"])

    def test_bob_marley_donald_trump_share_nothing(self):
        bob = create_person_from("Q409")
        donald = create_person_from("Q22686")
        #robert = create_person_from("Q36767")

        facts = find_common_facts_from([bob, donald])
        self.assertEqual(len(facts), 0)

    def test_barack_obama_donald_trump_share_first_name_is_alive(self):
        barack = create_person_from("Q76")
        donald = create_person_from("Q22686")

        facts = find_common_facts_from([barack, donald])
        facts.sort(key=lambda f: f.attribute)
        self.assertEqual(len(facts), 2)

        self.assertEqual(facts[0].attribute, "is_alive")
        facts[0].people_concerned.sort()
        self.assertEqual(facts[0].people_concerned, ["Q22686", "Q76"])
        self.assertEqual(facts[0].values, [True])

        self.assertEqual(facts[1].attribute, "nationality")
        facts[1].people_concerned.sort()
        self.assertEqual(facts[1].people_concerned, ["Q22686", "Q76"])
        self.assertEqual(facts[1].values, ["United States of America"])

        

if __name__ == '__main__':
    unittest.main()
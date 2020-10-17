import unittest
from sherlock.person import Person, create_person_from
import os
import json

class TestPerson(unittest.TestCase):

    def test_bob_marley_dead(self):
        bob = create_person_from("Q409")
        self.assertEqual(bob.wikidata_id, "Q409")
        self.assertEqual(bob.label, "Bob Marley")
        self.assertEqual(bob.description, "Jamaican singer, songwriter and musician")
        bob.first_names.sort()
        self.assertEqual(bob.first_names, ["Nesta", "Robert"])
        self.assertEqual(bob.last_name, "Marley")
        self.assertEqual(bob.nationality,"Jamaica")
        self.assertEqual(bob.birthdate, "1945-02-06T00:00:00Z")
        self.assertFalse(bob.is_alive)

    def test_Tim_Berners_Lee_alive(self):
        tim = create_person_from("Q80")
        self.assertEqual(tim.wikidata_id, "Q80")
        self.assertEqual(tim.label, "Tim Berners-Lee")
        self.assertEqual(tim.description, "British computer scientist, inventor of the World Wide Web")
        tim.first_names.sort()
        self.assertEqual(tim.first_names, ["John", "Timothy"])
        self.assertEqual(tim.last_name, "Berners-Lee")
        self.assertEqual(tim.nationality,"United Kingdom")
        self.assertEqual(tim.birthdate, "1955-06-08T00:00:00Z")
        self.assertTrue(tim.is_alive) # Hopefully this test will pass for a long time

    def test_gardield_is_not_human(self):
        garfield = create_person_from("Q767120")
        self.assertIsNone(garfield)

if __name__ == '__main__':
    unittest.main()
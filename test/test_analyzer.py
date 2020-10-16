import unittest
from sherlock.analyzer import get_people_from_text, AnalysisException
import os

class TestAnalyzer(unittest.TestCase):

    real_api_key = os.environ['TEXTRAZOR_API_KEY']
    fake_api_key = 'fakekey'

    def test_wrong_api_key_returns_401(self):
        os.environ['TEXTRAZOR_API_KEY'] = self.fake_api_key
        with self.assertRaises(AnalysisException) as ex:
            get_people_from_text('Barack Obama')
        
        the_exception = ex.exception
        self.assertEqual(the_exception.status, 401)

    def test_empty_text_returns_400(self):
        os.environ['TEXTRAZOR_API_KEY'] = self.real_api_key
        with self.assertRaises(AnalysisException) as ex:
            get_people_from_text('')
        
        the_exception = ex.exception
        self.assertEqual(the_exception.status, 400)

    def test_normal_text_works_well(self):
        os.environ['TEXTRAZOR_API_KEY'] = self.real_api_key
        people = get_people_from_text("Barack Obama.")
        self.assertEqual(len(people), 1)
        self.assertEqual(people[0], "Q76")

    def test_people_are_unique(self):
        os.environ['TEXTRAZOR_API_KEY'] = self.real_api_key
        people = get_people_from_text("Barack Obama. Barack Obama")
        self.assertEqual(len(people), 1)
        self.assertEqual(people[0], "Q76")

    def test_larger_texts_are_fine(self):
        text = r"La France s’apprête à replonger en apnée « au moins jusqu’à l’été 2021 ». Voilà le message qu’est venu apporter Emmanuel Macron à ses concitoyens, mercredi 14 octobre, alors que l’épidémie due au coronavirus représente à nouveau, selon les termes du chef de l’Etat, une « situation préoccupante » sur le territoire national, avec près de 20 000 nouveaux cas déclarés par jour et une occupation à 32 % des services de réanimation dans les hôpitaux par des patients atteints du Covid-19. « Nos soignants sont très fatigués (…). Nous n’avons pas de lits en réserve », a-t-il prévenu, alors que le virus s’est répandu sur l’ensemble du pays, empêchant ces transferts de malades entre les régions qui avaient été possibles en mars et avril."

        people = get_people_from_text(text)
        self.assertEqual(len(people), 1)
        self.assertEqual(people[0], "Q3052772")

if __name__ == '__main__':
    unittest.main()
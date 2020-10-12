import unittest
from repo import Repository, DuplicateException
from service import Service, SentenceException

class TestSecondF(unittest.TestCase):
    def test_repo_add(self):
        r = Repository("sentencestest.txt")
        r.add_sentence("hello there")
        sentence = r.getSentenceByIndex(2)
        
        self.assertEqual("hello there", sentence)

    def test_repo_add_duplicate(self):
        r = Repository("sentencestest.txt")
        self.assertRaises(DuplicateException, r.add_sentence, "hello there")

    def test_service_add(self):
        r = Repository("sentencestest.txt")
        s = Service(r)
        s.add_sentence("here goes anna")
        sentence = r.getSentenceByIndex(3)

        self.assertEqual("here goes anna", sentence)

    def test_service_add_no_word(self):
        r = Repository("sentencestest.txt")
        s = Service(r)
        self.assertRaises(SentenceException, s.add_sentence, "")

    def test_service_word_less_3_letters(self):
        r = Repository("sentencestest.txt")
        s = Service(r)
        self.assertRaises(SentenceException, s.add_sentence, "here i go")

if __name__ == "__main__":
    unittest.main()

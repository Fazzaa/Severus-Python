import unittest
from frame import Frame
from dialogmanager import DialogManager
from patterns import *

class TestFrameMethods(unittest.TestCase):
    
    def test_potions_added(self):
        f = Frame()
        self.assertEqual(f.get_potions_length(), 3)

    def test_check_response(self):
        f = Frame()
        f.set_potion_name("Pozione Polisucco")
        self.assertTrue(f.check_response("mosche crisopa"))

class TestDialogueManagerMethods(unittest.TestCase):

    def test_passive_pattern(self):
        dm = DialogManager()
        answer = "Crisopa fly is used in the potion"
        result = dm.get_matched_patterns_from_dependency("passive_pattern", passive_pattern, answer)[0]
        self.assertEqual(result[1].text, "Crisopa fly")

    def test_pattern_aux(self):
        dm = DialogManager()
        answer = "the answer is Crisopa Fly..."
        result = dm.get_matched_patterns_from_dependency("pattern_aux", pattern_aux, answer)[0]
        self.assertEqual(result[1].text, "Crisopa Fly")

    def test_pattern_verb(self):
        dm = DialogManager()
        answer = "the potion contains Crisopa fly"
        result = dm.get_matched_patterns_from_dependency("pattern_2", pattern_verb, answer)[0]
        self.assertEqual(result[1].text, "Crisopa fly")

if __name__ == '__main__':
    unittest.main()
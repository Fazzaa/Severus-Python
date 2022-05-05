import unittest
from frame import Frame
from dialogmanager import *
from patterns import *

class TestFrameMethods(unittest.TestCase):
    
    def test_potions_added(self):
        f = Frame()
        self.assertEqual(f.get_potions_length(), 3)

    def test_check_response(self):
        f = Frame()
        f.set_potion_name("Polyjuice potion")
        self.assertTrue(f.check_response({"Crisopa flies"}))

class TestDialogueManagerMethods(unittest.TestCase):

    def test_passive_pattern_common(self):
        answer = "puffer fish eyes is used in the potion"
        result = get_matched_patterns_from_dependency("passive_pattern_common", passive_pattern_common, answer)
        self.assertEqual(result, "puffer fish eyes")

    def test_passive_pattern_propn(self):
        answer = "Puffer Fish Eyes is used in the potion"
        result = get_matched_patterns_from_dependency("passive_pattern_propn", passive_pattern_propn, answer)
        self.assertEqual(result, "Puffer Fish Eyes")

    def test_passive_pattern_common_2(self):
        answer = "Murtlap's tentacle is used in the potion"
        result = get_matched_patterns_from_dependency("passive_pattern_common", passive_pattern_common, answer)
        self.assertEqual(result, "Murtlap's tentacle")

    def test_pattern_aux(self):
        answer = "the answer is Crisopa Flies..."
        result = get_matched_patterns_from_dependency("pattern_aux", pattern_aux, answer)
        self.assertEqual(result, "Crisopa Flies")

    def test_pattern_verb(self):
        answer = "the potion contains Crisopa flies"
        result = get_matched_patterns_from_dependency("pattern_verb", pattern_verb, answer)
        self.assertEqual(result, "Crisopa flies")

    def test_pattern_name(self):
        f = Frame()
        answer = "my name is Andrea Fancellu"
        find_pattern_name(f, pattern_name, answer)
        self.assertEqual(f.get_student_name(), "Andrea Fancellu")
 
class TestPatterns(unittest.TestCase):
    
    def test_passive_pattern_common(self):
        answer = "puffer fish eyes is used in the potion"
        result = get_matched_patterns_from_dependency("passive_pattern_common", passive_pattern_common, answer)
        self.assertEqual(result, "puffer fish eyes")

    def test_passive_pattern_propn(self):
        answer = "Puffer Fish Eyes is used in the potion"
        result = get_matched_patterns_from_dependency("passive_pattern_propn", passive_pattern_propn, answer)
        self.assertEqual(result, "Puffer Fish Eyes")

    def test_passive_pattern_common_2(self):
        answer = "Murtlap's tentacle is used in the potion"
        result = get_matched_patterns_from_dependency("passive_pattern_common", passive_pattern_common, answer)
        self.assertEqual(result, "Murtlap's tentacle")

    def test_pattern_aux(self):
        answer = "the answer is Crisopa Flies..."
        result = get_matched_patterns_from_dependency("pattern_aux", pattern_aux, answer)
        self.assertEqual(result, "Crisopa Flies")

    def test_pattern_verb(self):
        answer = "the potion contains Crisopa flies"
        result = get_matched_patterns_from_dependency("pattern_verb", pattern_verb, answer)
        self.assertEqual(result, "Crisopa flies")

    def test_pattern_name(self):
        f = Frame()
        answer = "my name is Andrea Fancellu"
        find_pattern_name(f, pattern_name, answer)
        self.assertEqual(f.get_student_name(), "Andrea Fancellu")        

if __name__ == '__main__':
    unittest.main()
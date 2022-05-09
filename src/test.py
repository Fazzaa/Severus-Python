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
        self.assertTrue(f.check_response({"crisopa flies"}))

class TestDialogueManagerMethods(unittest.TestCase):

    def test_passive_pattern_common(self):
        answer = "puffer fish eyes is used in the potion"
        result = get_matched_patterns_from_dependency("passive_pattern_common", passive_pattern_common, answer)
        self.assertEqual(result, "puffer fish eyes")

    def test_passive_pattern_2(self):
        answer = "Puffer Fish Eyes is used in the potion"
        result = get_matched_patterns_from_dependency("passive_pattern_2", passive_pattern_2, answer)
        self.assertEqual(result, "puffer fish eyes")

    def test_passive_pattern_common_2(self):
        answer = "Murtlap's tentacle is used in the potion"
        result = get_matched_patterns_from_dependency("passive_pattern_common", passive_pattern_common, answer)
        self.assertEqual(result, "murtlap's tentacle")

    def test_pattern_aux(self):
        answer = "the answer is Crisopa Flies..."
        result = get_matched_patterns_from_dependency("pattern_aux_1", pattern_aux_1, answer)
        self.assertEqual(result, "crisopa flies")

    def test_pattern_verb(self):
        answer = "the potion contains Crisopa flies"
        result = get_matched_patterns_from_dependency("pattern_verb_1", pattern_verb_1, answer)
        self.assertEqual(result, "crisopa flies")

    def test_pattern_name(self):
        f = Frame()
        answer = "my name is Andrea Fancellu"
        find_pattern_name(f, pattern_name, answer)
        self.assertEqual(f.get_student_name(), "Andrea Fancellu")
        
class TestSentences(unittest.TestCase):
          
    def test_all_sentence(self):
        
        snts= ["X is contained in the potion","X are contained in the potion",
               "X is used in the potion","X are used in the potion",
               "X is needed in the potion","X are needed in the potion",
               "The potion contains X","The potion uses X","The potion needs X", 
               "X", "The answer is X"]
        file = open("data/potions.txt", "r")
        err, ok = 0,0
        for line in file:
            ing_list = list(line.strip("\n").split(','))
            ing_list.pop(0)
            for ing in ing_list:
                for snt in snts:
                    s = snt.replace("X", ing)                    
                    isolated_ing = test_patterns(s)[0]
                    if isolated_ing != ing:
                        print(f"*The match from patter is: {isolated_ing}\n-The starting sentence is: {s}\nThe real ingredient is {ing}\n\n")
                        err+=1
                    else:
                        ok+=1
        print(f"Total Error = {err}")
        print(f"Total Correct = {ok}")
        file.close()

if __name__ == '__main__':
    unittest.main()
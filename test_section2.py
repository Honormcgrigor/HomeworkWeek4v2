import unittest
from section2 import main, split_word, num_letters, there_are_no_repetitions


class TestListWorks(unittest.TestCase):

    def test_does_it_split_word(self):
        expected = ['h', 'e', 'l', 'p']
        result = split_word('help')
        self.assertEqual(expected, result)
        #for the code to run, the expected and result must be equal
class TestIfRepetition(unittest.TestCase):
    # def test_there_are_no_repetitions(self):
    #     self.assertTrue(are_there_repetitions(True, item=[1,1,1], item_list=self.count_list))
    # if I knew how, I would like to test using self.assertFalse and self.assertTrue here
    def test_there_are_repetitions(self):
        expected = False
        result = there_are_no_repetitions([1,2,1])
        self.assertEqual(expected, result)

    def test_there_are_no_repetitions(self):
        expected = True
        result = there_are_no_repetitions([1,1,1])
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

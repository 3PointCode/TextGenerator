from bigram_model import successors_generator, generate_text
import unittest
from io import StringIO

class TestBigramTextGenerator(unittest.TestCase):
    def test_successor_generator(self):
        reader = StringIO("test text. this text is for testing.")
        expected_successor_map = {
            'for': ['testing'],
             'is': ['for'],
             'test': ['text'],
             'text': ['this', 'is'],
             'this': ['text']
        }
        result_successor_map = successors_generator(reader)
        self.assertEqual(result_successor_map, expected_successor_map)
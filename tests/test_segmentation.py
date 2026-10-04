import importlib.util
import pathlib
import unittest

path = pathlib.Path(__file__).resolve().parents[1] / 'dictionary-word-segmentation/word_segmentation.py'
spec = importlib.util.spec_from_file_location('segmentation', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class SegmentationTests(unittest.TestCase):
    def test_minimum_word_count(self):
        self.assertEqual(module.split_string('abc', {'a', 'b', 'c', 'ab', 'abc'}), ['abc'])
    def test_backtracks_when_longest_prefix_cannot_finish(self):
        self.assertEqual(module.split_string('abcd', {'abc', 'ab', 'cd'}), ['ab', 'cd'])
    def test_empty_and_impossible(self):
        self.assertEqual(module.split_string('', {'a'}), [])
        self.assertIsNone(module.split_string('x', {'a'}))

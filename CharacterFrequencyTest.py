import unittest
import CharacterFrequency


class MyTestCase(unittest.TestCase):
    def test_something(self):
        word = "semicolon.africa"
        expected = CharacterFrequency.character_frequency(word)
        actual = {'s': [1], 'e': [1], 'm': [1], 'i': [2], 'c': [2], 'o': [2], 'l': [1], 'n': [1], '.': [1], 'a': [2], 'f': [1], 'r': [1]}
        self.assertEqual(actual, expected)

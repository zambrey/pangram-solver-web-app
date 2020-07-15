import pygtrie as trie
from typing import List, Set, Tuple

with open('words_alpha.txt') as word_file:
    valid_words = word_file.read().split()

dictionary = trie.CharTrie.fromkeys(valid_words, True)


class pangramgame:
    def __init__(self, letters: List[str], required: List[str], lenRange: Tuple[int, int]):
        self._letters = set([s.lower() for s in letters])
        self._vowels = self._letters.intersection(
            set(['a', 'e', 'i', 'o', 'u']))
        self._consonants = self._letters - self._vowels
        self._required = set([s.lower() for s in required])
        self._lenRange = lenRange
        # self._dictionary = self._loadDictionary()
        self._dictionary = dictionary

    def _loadDictionary(self):
        with open('words.txt') as word_file:
            valid_words = word_file.read().split()

        return trie.CharTrie.fromkeys(valid_words, True)

    def _isPossibleWord(self, word: str) -> bool:
        # Must have required letters
        if len(self._required.intersection(word)) != len(self._required):
            return False

        # Verify in dict
        if word not in self._dictionary:
            return False

        return True

    def _solveHelper(self, curr: str, result: List[str]):
        if not self._dictionary.has_node(curr) or len(curr) > self._lenRange[1]:
            return

        if (self._lenRange[0] <= len(curr) <= self._lenRange[1]):
            if (self._isPossibleWord(curr)):
                # print(curr)
                result.append(curr)

        for l in self._letters:
            self._solveHelper(curr+l, result)

    def solve(self) -> List[str]:
        result = []
        self._solveHelper("", result)
        return result

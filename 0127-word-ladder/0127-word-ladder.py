from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        # endWord must exist in the dictionary
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:

            word, steps = queue.popleft()

            # Generate all possible one-letter transformations
            for i in range(len(word)):

                for ch in 'abcdefghijklmnopqrstuvwxyz':

                    if ch == word[i]:
                        continue

                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word == endWord:
                        return steps + 1

                    if new_word in wordSet:
                        # Remove immediately to avoid revisiting
                        wordSet.remove(new_word)

                        queue.append(
                            (new_word, steps + 1)
                        )

        return 0
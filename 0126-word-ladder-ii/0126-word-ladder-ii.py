from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # parent[word] = words that can reach this word
        parent = defaultdict(list)

        current_level = {beginWord}
        found = False

        # BFS
        while current_level and not found:

            # Remove words already processed at previous levels
            wordSet -= current_level

            next_level = set()

            for word in current_level:

                for i in range(len(word)):

                    for ch in 'abcdefghijklmnopqrstuvwxyz':

                        if ch == word[i]:
                            continue

                        new_word = (
                            word[:i] + ch + word[i + 1:]
                        )

                        if new_word in wordSet:

                            next_level.add(new_word)

                            # Store parent relationship
                            parent[new_word].append(word)

                            if new_word == endWord:
                                found = True

            current_level = next_level

        # If no transformation exists
        if not found:
            return []

        # DFS to build paths
        result = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for prev in parent[word]:
                path.append(prev)
                dfs(prev)
                path.pop()

        dfs(endWord)

        return result
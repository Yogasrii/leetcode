class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        # Frequency of each word
        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        result = []

        # Try each possible starting offset
        for start in range(word_len):
            left = start
            right = start
            current_count = 0
            seen = {}

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                # If word is not in words, reset the window
                if word not in word_freq:
                    seen.clear()
                    current_count = 0
                    left = right
                    continue

                seen[word] = seen.get(word, 0) + 1
                current_count += 1

                # Too many occurrences of this word
                while seen[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                    current_count -= 1

                # All words are present
                if current_count == word_count:
                    result.append(left)

                    # Move window forward for next possible match
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                    current_count -= 1

        return result
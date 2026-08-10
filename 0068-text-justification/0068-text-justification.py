class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):

            # Find how many words fit in this line
            line_length = len(words[i])
            j = i + 1

            while j < len(words):
                if line_length + 1 + len(words[j]) > maxWidth:
                    break

                line_length += 1 + len(words[j])
                j += 1

            line_words = words[i:j]

            # Last line or line with only one word
            if j == len(words) or len(line_words) == 1:

                line = " ".join(line_words)

                # Add spaces at the end
                line += " " * (maxWidth - len(line))

                result.append(line)

            else:
                # Number of spaces that need to be distributed
                total_spaces = maxWidth - sum(len(word) for word in line_words)

                gaps = len(line_words) - 1

                # Minimum spaces per gap
                spaces = total_spaces // gaps

                # Extra spaces
                extra = total_spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (spaces + (1 if k < extra else 0))

                line += line_words[-1]

                result.append(line)

            i = j

        return result
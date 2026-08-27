class Solution:
    def shortestPalindrome(self, s):
        rev = s[::-1]

        # Create combined string
        combined = s + "#" + rev

        # Build KMP LPS array
        lps = [0] * len(combined)

        for i in range(1, len(combined)):
            j = lps[i - 1]

            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]

            if combined[i] == combined[j]:
                j += 1

            lps[i] = j

        # Length of longest palindromic prefix
        longest = lps[-1]

        # Characters after the palindrome
        remaining = s[longest:]

        return remaining[::-1] + s
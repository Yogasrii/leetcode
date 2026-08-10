class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        # Count characters required from t
        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        left = 0
        right = 0

        formed = 0
        required = len(need)

        min_length = float("inf")
        min_left = 0

        while right < len(s):

            # Add current character
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # Check if requirement for this character is satisfied
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Try to shrink the window
            while left <= right and formed == required:

                # Update minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left

                # Remove left character
                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

            right += 1

        if min_length == float("inf"):
            return ""

        return s[min_left:min_left + min_length]
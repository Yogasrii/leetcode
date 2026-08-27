class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for a, b in zip(s, t):
            # Check s → t mapping
            if a in s_to_t and s_to_t[a] != b:
                return False

            # Check t → s mapping
            if b in t_to_s and t_to_s[b] != a:
                return False

            s_to_t[a] = b
            t_to_s[b] = a

        return True
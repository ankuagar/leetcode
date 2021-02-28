#!/usr/bin/env python3
import unittest
from copy import deepcopy
class Solution:
    def reverseString(self, s):
        """
        Modifying s in place but with a return
        """
        if len(s) == 0 or len(s) == 1:
            pass
        else:
            s[:] = self.reverseString(s[1:]) + [s[0]]
        return s

    def reverseString1(self, s):
            """
            Do not return anything, modify s in-place instead.
            """
            def helper(start, end):
                if len(s[start:end+1]) == 0 or len(s[start:end+1]) == 1:
                    pass
                else:
                    helper(start+1, end-1)
                    s[start], s[end] = s[end], s[start]
                                        
            helper(0, len(s) - 1) # set start and end pointers

t = unittest.TestCase()
sol = Solution()
for s in [[], ["a"], ["a", "b"], ["a", "b", "c"]]:
    print("For: ", s, end="")
    temp = deepcopy(s)
    initialId = id(s)
    sol.reverseString(s)
    t.assertEqual(initialId, id(s))
    t.assertEqual(temp[::-1], s)
    print(": pass")

sol = Solution()
for s in [[], ["a"], ["a", "b"], ["a", "b", "c"]]:
    print("For: ", s, end="")
    temp = deepcopy(s)
    initialId = id(s)
    sol.reverseString1(s)
    t.assertEqual(initialId, id(s))
    t.assertEqual(temp[::-1], s)
    print(": pass")
# Solution 1
class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in hash_map:
                stack.append(char)
            elif not stack or hash_map[stack.pop()] != char:
                return False
        return not stack
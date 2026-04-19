# Last updated: 4/19/2026, 2:38:43 PM
class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in hash_map.values():
                stack.append(char)
            elif char in hash_map.keys():
                if not stack or hash_map[char] != stack.pop():
                    return False
        return not stack
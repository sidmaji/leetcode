---
link: https://leetcode.com/problems/valid-palindrome/
difficulty: Easy
topics:
  - two-pointers
  - string
---
# Valid Palindrome

## Approach
Clean `s` by only keeping alpha-numeric characters with the `.isalnum()` method and converting them to lowercase with `.lower()`.

Iterate through `s` until the index `len(s) // 2`, only going halfway because the middle is being approached from the left and from the right by using `s[i]` as the pointer from the left side and `s[len(s) - i - 1]` as the pointer from the right side. If the current character from both sides do not match, `False` is returned.

If no mismatch is encountered, `True` is returned.

## Solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        for i in range(int(len(s) / 2)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
```

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)
	- Changing `s` to new string, worst case same length `n` where n is length of `s`.
---
link: https://leetcode.com/problems/valid-anagram/
difficulty: Easy
topics:
  - hash-table
  - string
  - sorting
---
# Valid Anagram

## Approach
This solution is very similar to [[383-RansomNote.py]]. First, I addressed the case where the two strings `s` and `t` have different lengths (meaning `t` cannot be an anagram of `s`) by returning `False`.

Afterwards, I set up a hash table to track the frequencies of every character in `s`, kind of like a bank of characters that I can use later.

Then, iterating through each character in `t`, I decrement the frequency of the current character from `s_dict`. If the current character isn't in `s_dict` (meaning `s` doesn't have that character) or if the frequency of it is 0 (meaning there are not enough occurrences of the current character in `s`), then `False` is returned.

Otherwise, `return True` after the `for` loop.

## Solution
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        
        for char in t:
            if char not in s_dict or s_dict[char] == 0:
                return False
            s_dict[char] = s_dict[char] - 1
            
        return True
```

## Complexity
- Time Complexity: O(n + m), where n is the length of `s` and m is the length of `t`.
- Space Complexity: O(n)
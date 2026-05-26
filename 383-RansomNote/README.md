---
link: https://leetcode.com/problems/ransom-note/
difficulty: Easy
topics:
  - hash-table
  - string
  - counting
---
# Ransom Note

## Approach
First, a hash table is initialized that stores all the characters in `magazine` and their frequencies. Then, iterate through `ransomNote` and subtract 1 from the frequency of the current character in `chars`, using it as a word bank.

If the frequency was already 0 (which means there is no remaining occurrence of that character in `magazine` left to use) or if the character doesn't exist as a key in `chars` (which means it was never in `magazine`) then `False` is returned. After the loop, `True` is returned.

## Solution
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        for char in magazine:
            chars[char] = chars.get(char, 0) + 1

        for char in ransomNote:
            if char not in chars or chars[char] == 0:
                return False
            chars[char] -= 1

        return True
```

## Complexity
- Time Complexity: O(n + m), where n is the length of `ransomNote` and m is the length of `magazine`.
- Space Complexity: O(m)
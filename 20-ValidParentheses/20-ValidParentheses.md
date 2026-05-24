---
link: https://leetcode.com/problems/valid-parentheses/
difficulty: Easy
topics:
  - string
  - stack
---
# Valid Parentheses

## Approach
First, a hash map is initialized with every key being the opening bracket and the value being the matching closing bracket (e.g. `"(" : ")"`).

Looping through every character in the provided string, each character is added to the `stack` list if it is a key in `hash_map` (meaning it is a opening bracket). This continues until a closing bracket is encountered.

Then it checks whether the stack is already empty, which means there is no previous opening bracket left that can match with the current closing bracket.

If that condition is satisfied, the `elif` statement gets the last character in `stack` by calling the `pop()` method on `stack`, and it uses this to get the value in `hash_map`.

For example, if the last encountered opening bracket was a square bracket `"["`, then `stack.pop()` will return `"["`. Plugging this into `hash_map` will return `"]"`.

It is then checked whether the current character (which will be a closing bracket) matches this exact bracket. If not, return `False`.

Finally, return `not stack` to make sure the stack is empty and that every opening bracket had a matching closing bracket in the string.

## Solution
```python
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
```

## Complexity
- Time Complexity: O(n)
	- Iterates through the string once, where `n` is the length of `s`.
- Space Complexity: O(n)
	- Worst case, the `stack` stores every opening bracket
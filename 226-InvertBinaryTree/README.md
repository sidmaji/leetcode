---
link: https://leetcode.com/problems/invert-binary-tree/
difficulty: Easy
topics:
  - tree
  - depth-first-search
  - breadth-first-search
  - binary-tree
---
# Invert Binary Tree

## Approach
My approach uses depth-first search. Flipping left and right nodes along the way, the recursive program goes to the leftmost side until it reaches a null, after which it goes back up and to the right, and eventually ends up all the way on the right side of the binary tree.

I used recursion to essentially flip the left and right nodes of the current `root` node, then do the same for the left node by calling on its own function (`self.invertTree()`), then calling it on the right node. This recursively flips the left and right nodes for every node.

To make sure it doesn't hit an error, a conditional statement is added at the top of the function to ensure that it stops without doing anything if the `root` passed in is null.

## Solution
```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
            
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

## Complexity
- Time Complexity: 
- Space Complexity: 
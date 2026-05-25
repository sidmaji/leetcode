---
link: https://leetcode.com/problems/merge-two-sorted-lists/
difficulty: Easy
topics:
  - linked-list
  - recursion
---
# Merge Two Sorted lists

## Approach
The `dummy` `ListNode` is initialized to start the merged list. Then values from `list1` and `list2` are compared, with the smaller value being attached to `head.next`. `head` is always moving as a pointer, but `dummy` stays at the beginning.

`list1` or `list2`, whichever had the smaller value when comparing, is moved forward to the next node. When one or both of the lists are empty, the `while` loop is exited, and whichever list has remaining values, if any, is attached to `head.next`. Finally, `dummy.next` is returned which is the head of the merged list. `dummy` is at the start but it is still a `None`-value `ListNode` so its `.next` value must be returned.

## Solution
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        if list1:
            head.next = list1
        elif list2:
            head.next = list2
        
        return dummy.next # head of merged list
```

## Complexity
- Time Complexity: O(n + m), where n is the length of `list1` and m is the length of `list2`.
- Space Complexity: O(1)
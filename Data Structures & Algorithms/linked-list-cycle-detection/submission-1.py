# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hist = dict()
        while (head != None and head.next != None and head.val not in hist):
            hist[head.val] = 1
            head = head.next
        if head == None or head.next == None:
            return False
        return True
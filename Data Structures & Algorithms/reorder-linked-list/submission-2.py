# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        stack = []
        temp = head
        while temp.next != None:
            stack.append(temp.next)
            temp = temp.next

        front_i = 0
        back_i = len(stack) - 1
        head.next = stack[back_i]
        while front_i < back_i:
            stack[back_i].next = stack[front_i]
            back_i -= 1
            stack[front_i].next = stack[back_i]
            front_i += 1
        

        stack[back_i].next = None
            
        
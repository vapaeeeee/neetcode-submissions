# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        i = 0

        while p2.next:
            p2 = p2.next
            i += 1
            if i > n:
                p1 = p1.next
        if n-i==1:
            head = head.next
            return head
        if p1.next:
            p1.next = p1.next.next
        else:
            return p1.next
        return head
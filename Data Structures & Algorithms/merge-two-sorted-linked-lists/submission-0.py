# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None
        l1 = list1
        l2 = list2

        while l1 or l2:
            if l1 and l2 and l1.val <= l2.val or not l2:
                if not head:
                    head = l1
                    curr = head
                    l1 = l1.next
                else:
                    curr.next = l1
                    l1 = l1.next
                    curr = curr.next
                
            elif l1 and l2 and l1.val > l2.val or not l1:
                if not head:
                    head = l2
                    curr = head
                    l2 = l2.next
                else:
                    curr.next = l2
                    l2 = l2.next
                    curr = curr.next
                
          

        return head

            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast:
            if fast.next is None or fast.next.next is None:
                break
            slow = slow.next
            fast = fast.next.next

        second_list_beginning = slow.next
        slow.next = None
        midpoint = slow

        prev = None
        while second_list_beginning:
            next = second_list_beginning.next
            second_list_beginning.next = prev
            prev = second_list_beginning
            second_list_beginning = next
        second_half_head_previous_original_tail = prev

        curr = None
        l1 = head  # [1, 2]
        l2 = second_half_head_previous_original_tail  # [5, 4, 3]

        while l2:
            l1_next = l1.next
            l2_next = l2.next
            if curr is None:
                curr = l1
                curr.next = l2
                curr = curr.next
            else:
                curr.next = l1
                curr.next.next = l2
                curr = curr.next.next
            l1 = l1_next
            l2 = l2_next
        if curr:
            curr.next = l1


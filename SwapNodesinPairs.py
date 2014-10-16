# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next != None and prev.next.next != None:
            slow = prev.next
            quick = slow.next
            prev.next = quick
            slow.next = quick.next
            quick.next = slow
            prev = slow
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head == None:
            return None
        ptr = head
        i = 0
        while i < n:
            ptr = ptr.next
            i += 1
        if ptr == None:
            head = head.next
            return head
        slow = head
        while ptr.next != None:
            ptr = ptr.next
            slow = slow.next
        slow.next = slow.next.next
        return head
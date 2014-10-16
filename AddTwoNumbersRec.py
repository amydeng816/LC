# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        pointer = dummy
        self.addTwoNumbersRec(l1, l2, 0, pointer)
        return dummy.next
        
    def addTwoNumbersRec(self, n1, n2, add, pointer):
        if n1 == None and n2 == None:
            if add != 0:
                pointer.next = ListNode(add)
            return
        if n1 == None:
            digit = add + n2.val
            add = digit / 10
            n2 = n2.next
        elif n2 == None:
            digit = add + n1.val
            add = digit / 10
            n1 = n1.next
        else:
            digit = add + n1.val + n2.val
            add = digit / 10
            n1 = n1.next
            n2 = n2.next
        pointer.next = ListNode(digit % 10)
        self.addTwoNumbersRec(n1, n2, add, pointer.next)
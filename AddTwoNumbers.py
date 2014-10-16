# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        dummy = ListNode(0)
        temp = dummy
        add = 0
        temp1 = l1
        temp2 = l2
        while temp1 != None and temp2 != None:
            sum = add + temp1.val + temp2.val
            temp.next = ListNode(sum % 10)
            temp = temp.next
            temp1 = temp1.next
            temp2 = temp2.next
            add = sum / 10
        remain = None
        if temp1 == None:
            remain = temp2
        if temp2 == None:
            remain = temp1

        while remain != None:
            if add == 0:
                temp.next = remain
                return dummy.next
            sum = add + remain.val
            temp.next = ListNode(sum % 10)
            temp = temp.next
            remain = remain.next
            add = sum / 10
        if add != 0:
            temp.next = ListNode(1)
        return dummy.next
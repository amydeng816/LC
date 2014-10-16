# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if not lists:
            return None
        tempList = []
        while len(lists) > 1:
            i = 0
            while i < len(lists) - 1:
                tempList.append(self.merge(lists[i], lists[i + 1]))
                i = i + 2
            if len(lists) % 2 == 1:
                tempList.append(lists[len(lists) - 1])
            lists = tempList
            tempList = []
        return lists[0]
    def merge(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
            else:
                temp.next = l1
                temp = temp.next
                l1 = l1.next
        if l1 == None:
            temp.next = l2
        else:
            temp.next = l1
        return dummy.next
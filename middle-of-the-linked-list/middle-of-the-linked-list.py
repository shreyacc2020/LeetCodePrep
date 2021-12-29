# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        count=0
        headCount = 1
        while(ptr):
            count+=1
            ptr = ptr.next
        if count%2 != 0:
            while(headCount<(count/2)):
                head = head.next
                headCount+=1
            return head
        elif count%2 == 0:
            while(headCount<(count/2)):
                head = head.next
                headCount+=1
            head = head.next
            return head
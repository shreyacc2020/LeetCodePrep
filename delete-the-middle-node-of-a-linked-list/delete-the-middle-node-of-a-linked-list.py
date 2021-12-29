# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        middlePtr = head
        count = 0
        countIndex = 0
        while(ptr):
            count+=1
            ptr = ptr.next
        # print(count)
        indexOfMiddleNode = count//2
        # print(indexOfMiddleNode)
        while countIndex<indexOfMiddleNode-1:
            middlePtr = middlePtr.next
            countIndex+=1
        if count>2:
            nxt = middlePtr.next
            prev = middlePtr
            prev.next = middlePtr.next.next
        elif count == 1:
            head = None
        elif count == 2:
            head.next = None
        return head
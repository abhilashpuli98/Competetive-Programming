# Last Updated: 6/22/2026, 12:43:18 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
    def findMiddleLL(self,head):
        slow=fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        return prev
    def merge2Lists(self,h1,h2):
        dummyNode=ListNode()
        temp=dummyNode
        while h1 and h2:
            if h1.val<h2.val:
                temp.next=h1
                h1=h1.next
            else:
                temp.next=h2
                h2=h2.next
            temp=temp.next
        if h1:
            temp.next=h1
        if h2:
            temp.next=h2
        return dummyNode.next

    def mergeSort(self,head):
        if not head or not head.next:
            return head
        middle=self.findMiddleLL(head)
        left_head=head
        right_head=middle.next
        middle.next=None
        left_head=self.mergeSort(left_head)
        right_head=self.mergeSort(right_head)
        return self.merge2Lists(left_head,right_head)
        
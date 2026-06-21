# Last Updated: 6/22/2026, 12:44:36 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or not head or not head.next:
            return head
        leng=0
        temp=head
        while temp:
            temp=temp.next
            leng+=1
        k=k%leng
        if k==0:
            return head
        steps=leng-k-1
        temp=head
        while steps:
            steps-=1
            temp=temp.next
        newHead=temp.next
        temp.next=None
        temp=newHead
        while temp and temp.next:
            temp=temp.next
        temp.next=head
        return newHead

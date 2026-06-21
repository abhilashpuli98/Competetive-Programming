# Last Updated: 6/21/2026, 7:06:58 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1=None
        head2=None
        cn1=None
        cn2=None
        cn=head
        tracker=0
        while cn:
            if tracker%2==0:
                if not head1:
                    head1=cn
                    cn1=cn
                else:
                    cn1.next=cn
                    cn1=cn
            else:
                if not head2:
                    head2=cn
                    cn2=cn
                else:
                    cn2.next=cn
                    cn2=cn
            cn=cn.next
            tracker+=1
        if cn2:
            cn2.next=None
        if cn1:
            cn1.next=head2
        return head1

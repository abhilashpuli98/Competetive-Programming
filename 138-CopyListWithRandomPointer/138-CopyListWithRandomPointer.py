# Last Updated: 6/22/2026, 12:43:31 AM
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':    
        
        curr=head
        
        while curr:
            node=Node(curr.val)
            node.next=curr.next
            curr.next=node
            curr=curr.next.next
        curr=head
        while curr:
            if not curr.random:
                curr.next.random=None
            else:
                curr.next.random=curr.random.next
            curr=curr.next.next
        temp=head
        dummy=Node(-1)
        curr=dummy
        while temp:
            curr.next=temp.next
            temp.next=temp.next.next
            temp=temp.next
            curr=curr.next
        return dummy.next
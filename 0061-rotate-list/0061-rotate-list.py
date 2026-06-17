# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        while not head or not head.next:
            return head
        n=0
        curr=head
        while curr:
            curr=curr.next
            n+=1
        k=k%n
        c=0
        while c<k:
            curr=head
            while curr.next.next:
                curr=curr.next
            temp=curr.next
            curr.next=None
            temp.next=head
            head=temp
            c+=1
        return head
        

        
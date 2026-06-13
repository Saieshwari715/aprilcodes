# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        res=dummy
        sum=0
        c=0
        while l1 or l2 or c:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            t=val1+val2+c
            c=t//10
            d=t%10
            dummy.next=ListNode(d)
            dummy=dummy.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return res.next

            
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''dummy=ListNode()
        num1=""
        num2=""
        
        while l1!=None and l2!=None:
            num1+=str(l1.val)
            num2+=str(l2.val)
            l1=l1.next
            l2=l2.next
        while l1!=None:
            num1+=str(l1.val)
            l1=l1.next
        while l2!=None:
            num2+=str(l2.val)
            l2=l2.next
        num1=int(num1[::-1])
        num2=int(num2[::-1])
        res=num1+num2
        res=str(res)[::-1]
        head=dummy
        for ele in res:
            head.next=ListNode(int(ele))
            head=head.next
        return dummy.next
'''

        


        
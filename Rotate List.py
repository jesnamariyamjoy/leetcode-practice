# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Edge cases: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the list and locate the tail node
        current = head
        n = 1
        while current.next:
            current = current.next
            n += 1
            
        # Step 2: Make the linked list circular by connecting tail to head
        current.next = head
        
        # Step 3: Find the effective rotations needed (since k can be larger than n)
        k %= n
        if k == 0:
            current.next = None  # Break the circle if no rotation actually happens
            return head
            
        # Step 4: Find the new tail (n - k steps from the start)
        steps_to_new_tail = n - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        # Step 5: Break the circle and set the new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
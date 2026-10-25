# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the k-th node of this group (or stop if fewer than k remain)
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # Reverse the group: nodes from group_prev.next up to kth
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Reconnect: group_prev -> (new head of group), and advance
            old_group_head = group_prev.next  # this is now the tail of the reversed group
            group_prev.next = kth
            group_prev = old_group_head
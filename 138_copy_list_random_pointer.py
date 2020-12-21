"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        id_hash = {}
        temp = head
        head_id = None
        flag = True
        _next, _rand = None, None
        
        if not head:
            return head
        
        while temp:
            if flag:
                head_id = id(temp)
                flag = False
                
            if temp.next:
                _next = id(temp.next)
            else:
                _next = None
            
            if temp.random:
                _rand = id(temp.random)
            else:
                _rand = None
                
            id_hash[id(temp)] = Node(temp.val, _next, _rand)
            temp = temp.next
        
        temp = id_hash[head_id] 
        
        while temp:
            if temp.next:
                temp.next = id_hash[temp.next]
            else:
                temp.next = None
            
            if temp.random:
                temp.random = id_hash[temp.random]
            else:
                temp.random = None
                
            temp = temp.next
            
        return id_hash[head_id]
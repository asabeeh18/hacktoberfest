#https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        class Node:
            def __init__(self,node,x,y):
                self.x=x
                self.y=y
                self.n=node
        
        d={}
        root=Node(root,0,0)
        q=deque()
        q.append(root)
        
        while q:
            x=q.popleft()
            
            if (x.x,x.y) not in d:
                d[(x.x,x.y)]=[x.n.val]
            else:
                d[(x.x,x.y)].append(x.n.val)
            
            if x.n.left:
                f=Node(x.n.left,x.x-1,x.y+1)
                q.append(f)
            if x.n.right:
                f=Node(x.n.right,x.x+1,x.y+1)
                q.append(f)
                
        res=[]
        print(d)
        py=float('-inf')
        for i in sorted(d):
            if py==i[0]:
                res[-1]+=sorted(d[i])
            else:
                res.append(sorted(d[i]))
            py=i[0]
        return res
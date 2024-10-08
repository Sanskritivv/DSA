class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        result = []
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val) 
        result.extend(self.inorderTraversal(root.right))
        return result

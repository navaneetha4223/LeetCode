class Solution:
    def bstFromPreorder(self, preorder):
        self.i = 0

        def build(bound):
            if self.i == len(preorder) or preorder[self.i] > bound:
                return None

            rootV = preorder[self.i]
            self.i += 1

            root = TreeNode(rootV)
            root.left = build(rootV)
            root.right = build(bound)

            return root

        return build(float('inf'))
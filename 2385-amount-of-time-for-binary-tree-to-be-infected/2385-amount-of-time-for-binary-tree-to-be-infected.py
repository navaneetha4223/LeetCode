from collections import deque

class Solution:
    def amountOfTime(self, root, start):

        # Step 1: Build parent mapping
        def getParent(root):
            parent = {}
            q = deque([root])

            while q:
                node = q.popleft()

                if node.left:
                    parent[node.left] = node
                    q.append(node.left)

                if node.right:
                    parent[node.right] = node
                    q.append(node.right)

            return parent

        # Step 2: Find start node
        def getStartNode(root, start):
            q = deque([root])

            while q:
                node = q.popleft()

                if node.val == start:
                    return node

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        parent = getParent(root)
        startNode = getStartNode(root, start)

        # Step 3: BFS to calculate time
        q = deque([startNode])
        visited = set([startNode])
        time = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                # left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)

                # right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)

                # parent
                if node in parent and parent[node] not in visited:
                    visited.add(parent[node])
                    q.append(parent[node])

            time += 1

        return time - 1
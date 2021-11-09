def bfs(self):
     traversal = []
      Q = ArrayQueue()
       if self.root == None:
            return traversal
        else:
            Q.enqueue(self.root)
        while not Q.isEmpty():
            visit = Q.dequeue()
            traversal.append(visit.data)
            if visit.left:
                Q.enqueue(visit.left)
            if visit.right:
                Q.enqueue(visit.right)
        return traversal

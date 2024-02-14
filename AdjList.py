class AdjNode:
    def __init__(self, value):
        self.data = value
        self.next = None


class AdjList:

    def __init__(self, num):

        self.V = num
        self.adjList = [None] * self.V
    
    def addEdge(self, src, dest):
    
        newNode = AdjNode(dest)
        
        if self.adjList[src] == None:
            self.adjList[src] = newNode
        else:

            last = self.adjList[src]

            while last.next != None:
            
                last = last.next
            

            last.next = newNode
    
    def printGraph(self):

        for i in range(self.V):
        
            temp = self.adjList[i]

            print("adjList["+str(i)+"]", end="->")

            while temp != None:
            
                print(temp.data, end="->")
                temp = temp.next
            
            print("None")

    def addEdgeopt(sielf, src, dest):

       newNode = AdjNode(dest)

       newNode.next = self.adjList[src]
       self.adjList[src] = newNode

    def hasEdge(self, src, dest):

       temp = self.adjList[src]

       while temp != None:
           
           if temp.data == dest:
               return 1
           temp = temp.next

       return 0

    def removeEdge(self, src, dest):

       if self.adjList[src] == None:
           return

       if self.adjList[src].data == dest:
           self.adjList[src] = self.adjList[src].next
       else:
           current = AdjNode(self.adjList[src])

           while current.next != None:

               if current.next.data == dest:
                   temp = AdjNode(current.next)
                   temp.next = current.next
                   break
               else:
                   current = current.next
        
    
if __name__ == '__main__':    

        obj = AdjList(5)

        print("Adding Edge From 0 to 1")
        obj.addEdge(0,1)
        print("Adding Edge From 0 to 2")
        obj.addEdge(0,2)
        print("Adding Edge From 0 to 3")
        obj.addEdge(0,3)
        print("Adding Edge From 1 to 3")
        obj.addEdge(1,3)
        print("Adding Edge From 1 to 4")
        obj.addEdge(1,4)
        print("Adding Edge From 2 to 3")
        obj.addEdge(2,3)
        print("Adding Edge From 3 to 4")
        obj.addEdge(3,4)

        print("Adjacency List Representation of the Graph")
        obj.printGraph()
        
        if obj.hasEdge(0, 3):
            print("hasEdge")
        else:
            print("doesn't hasEdge")

        if obj.hasEdge(1, 2):
            print("hasEdge")
        else:
            print("doesn't hasEdge")

        obj.removeEdge(1, 3)
        obj.removeEdge(0, 2)
        obj.printGraph()
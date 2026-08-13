class AdjMatrix:
    def __init__(self,size):
        self.arr=[]
        for _ in range(size):
            self.arr.append( [0 for i in range(size)])

    def display_matrix(self):
        for row in self.arr:
                print(row)
        print("\n")        

    def add_edge(self,src,dest):
        self.arr[src][dest]  = 1       
        self.arr[dest][src]  = 1  

    def remove_edge(self,src,dest):
        self.arr[src][dest]  = 0
        self.arr[dest][src]  = 0

    def has_edge(self,src,dest):
        if self.arr[src][dest] == 1:
            return 1
        else:
            return 0    


mat=AdjMatrix(3)
mat.display_matrix()
mat.add_edge(0,1) 
mat.add_edge(1,2) 
mat.add_edge(0,2) 
mat.display_matrix()
mat.remove_edge(1,2)
mat.display_matrix()
print(mat.has_edge(0,1))
print(mat.has_edge(1,2))
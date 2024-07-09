class HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size
        for i in range(self.size):
            self.table[i] = -1
            i+=1

    def insert(self,num):
        key = num % self.size
        index=key

        while(self.table[key] != -1):
            key = (key+1) % self.size

            if index == key:
                print("Hash Table full")
        self.table[key] = num

    def delete(self,num):
        key = num % self.size
        index=key

        while(self.table[key] != num):
            key = (key+1) % self.size

            if key == index:
                return 0
        self.table[key]= -1
        return 1

    def search(self,num):
        key = num % self.size
        index=key

        while(self.table[key] != num ):
            key = (key+1) % self.size

            if index == key:
                return 0
        return 1    
HT=HashTable(5)


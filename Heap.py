import math

class Heap:
    def __init__(self):
        self.tree = []

    def getFather(self, index):
        return math.floor((index - 1) / 2)

    def getLChild(self, index):
        return index * 2 + 1

    def getRChild(self, index):
        return index * 2 + 2

    def addnSort(self, element):
        index = len(self.tree)
        father = self.getFather(index)
        self.tree.append(element)
        if father < 0:
            return
        while(father >= 0):
            if element[1] > self.tree[father][1]:
                self.tree[index], self.tree[father] = self.tree[father], self.tree[index]
                index = father
                father =self.getFather(index)
            else:
                break

    def getMax(self):
        if len(self.tree) == 1:
            return self.tree[0]
        m = self.tree[0]
        sub = self.tree[-1]
        del(self.tree[-1])
        self.tree[0] = sub
        self.bubbleDown()
        return m

    def replaceChild(self, index):
        if(self.haveLChild(index) and self.haveRChild(index)):
            if self.tree[self.getLChild(index)][1] >= self.tree[self.getRChild(index)][1]:
                if self.tree[index][1] < self.tree[self.getLChild(index)][1]:
                    self.tree[index], self.tree[self.getLChild(index)] = self.tree[self.getLChild(index)], self.tree[index]
                    return self.getLChild(index)
            else:
                if self.tree[index][1] < self.tree[self.getRChild(index)][1]:
                    self.tree[index], self.tree[self.getRChild(index)] = self.tree[self.getRChild(index)], self.tree[index]
                    return self.getRChild(index)
        else:
            if self.tree[index][1] < self.tree[self.getLChild(index)][1]:
                self.tree[index], self.tree[self.getLChild(index)] = self.tree[self.getLChild(index)], self.tree[index]
                return self.getLChild(index)
        return -1


    def bubbleDown(self):
        index = 0
        while(self.haveLChild(index) or self.haveLChild(index)):
            index = self.replaceChild(index)
            if index == -1: break


    def haveLChild(self, index):
        return self.getLChild(index) < len(self.tree)
        
    def haveRChild(self, index):
        return self.getRChild(index) < len(self.tree)
    


    def getFirstK(self, k):
        result = []
        k = min(k, len(self.tree))
        for i in range(k):
            print(i)
            result.append(self.getMax())
        return result

    def getSize(self):
        return len(self.tree)
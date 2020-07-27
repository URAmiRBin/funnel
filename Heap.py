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
        # print("ADDING ", element)
        # print("CURRENT ", self.tree)
        index = len(self.tree)
        father = self.getFather(index)
        self.tree.append(element)
        if father < 0:
            # print("NEW ", self.tree)
            return
        while(father >= 0):
            if element[1] > self.tree[father][1]:
                self.tree[index], self.tree[father] = self.tree[father], self.tree[index]
                index = father
                father =self.getFather(index)
            else:
                break
        # print("NEW ", self.tree)
        # print("===============")

    def getMax(self):
        m = self.tree[0]
        sub = self.tree[-1]
        del(self.tree[-1])
        self.tree[0] = sub
        # print("STARTING BUBBLE DOWN WITH ", self.tree)
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
        # print("BUBBLED DOWN ", self.tree[index])
        # print("NEW ", self.tree)

    def haveLChild(self, index):
        return self.getLChild(index) < len(self.tree)
        
    def haveRChild(self, index):
        return self.getRChild(index) < len(self.tree)
    


    def getFirstK(self, k):
        # print("============================================")
        result = []
        for i in range(k):
            result.append(self.getMax())
            # print("Added ", result[i])
        return result

    def getSize(self):
        return len(self.tree)
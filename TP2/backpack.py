from typing import Tuple
import math

class Elem:
    def __init__(self, benefit, weight):
        self.benefit = benefit
        self.weight = weight

class Backpack:
    def __init__(self, max_capacity, max_weight, elems = []):
        self.max_capacity = max_capacity
        self.max_weight = max_weight
        self.elems = elems
    
    def getCapacity(self):
        return self.max_capacity

    def getMaxWeight(self):
        return self.max_weight

    def getWeight(self, chrom):
        totWeight = 0
        for c,e in zip(chrom, self.elems):
            if c:
                totWeight += e.weight
        return totWeight
    
    def getElemWeight(self, index):
        return self.elems[index].weight
    
    def getBenefit(self, chrom):
        totBenefit = 0 
        for c, e in zip(chrom, self.elems):
            if c:
                totBenefit += e.benefit
        return totBenefit

    def getFitness(self, chrom):
        benefit = self.getBenefit(chrom)
        weight = self.getWeight(chrom)
        if weight > self.getMaxWeight():
           weight *= (weight - self.getMaxWeight())
           return benefit/weight
        return benefit
        # d = self.getBenefit(chrom) - self.getWeight(chrom) 
        # if( d > 700):
        #     d = 700
        # if( d < 0):
        #     ans = -1/d
        # else:
        #     prev = math.pow(math.e, d)
        #     ans = math.pow(prev, 0.5)
        # return ans

    def getPopuFitness(self, popu):
        maxFit =0
        for i in popu:
            actualFit = self.getFitness(i)
            if(maxFit < actualFit):
                maxFit = actualFit
        return maxFit
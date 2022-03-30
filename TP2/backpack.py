from typing import Tuple

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
    
    def getBenefit(self, chrom):
        totBenefit = 0 
        for c, e in zip(chrom, self.elems):
            if c:
                totBenefit = e.benefit
        return totBenefit

    def getFitness(self, chrom):
        if self.getWeight(chrom) > self.max_weight:
            return 0
        return self.getBenefit(chrom)
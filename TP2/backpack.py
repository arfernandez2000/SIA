from typing import Tuple


class Elem:
    def __init__(self, benefit, weight):
        self.benefit = benefit
        self.weight = weight


Chromosome = Tuple[bool, ...]


class Backpack:
    def __init__(self, max_capacity, max_weight, elems = []):
        self.max_capacity = max_capacity
        self.max_weight = max_weight
        self.elems = elems
    
    def getWeight(self, chrom: Chromosome):
        totWeight = 0
        for c,e in zip(chrom, self.elems):
            if c:
                totWeight += e.weight
        return totWeight
    
    def getBenefit(self, chrom: Chromosome):
        totBenefit = 0 
        for c, e in zip(chrom, self.elems):
            if c:
                totBenefit = e.benefit
        return totBenefit

    def getFitness(self, chrom: Chromosome):
        if self.getWeight(chrom) > self.max_capacity:
            return 0
        return self.getBenefit(chrom)

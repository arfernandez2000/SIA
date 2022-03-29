import random

def crossbreed(one, two, n):
    if n==0:
        for i in range (0, len(one)):
            prob = random.random()
            if prob > 0.5:
                one[i], two[i] = two[i], one[i]
        
    else:
        points = set()
        points.add(0)
        points.add(len(one))
        while n>0:
            l = len(points)
            points.add(random.randint(0, len(one)))
            if len(points) == l:
                n-=1
        points = sorted(points)

        final_one = []
        final_two = []

        for i in range(0, len(points) -1):
            
            p1 = points[i]
            p2 = points [i+1]

            n1 = one if i%2 == 0 else two
            n2 = two if i%2 == 0 else one

            if i==0:
                final_one += n1[0:p1]
                final_two += n2[0:p1]
    
            final_one += n1[p1:p2]
            final_two += n2[p1:p2]
            
        return final_one, final_two
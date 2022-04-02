import random
from config_loader import crossover_points

def crossbreed(one, two, backpack):
    n = crossover_points
    if n == 0:
        onet = list(one)
        twot = list(two)
        for i in range (0, len(one)):
            prob = random.uniform(0, 1)
            if prob > 0.5:
                onet[i], twot[i] = twot[i], onet[i]
        return tuple(onet), tuple(twot)
        
    else:
        points = set()
        points.add(0)
        points.add(len(one))
        while n > 0:
            l = len(points)
            points.add(random.randint(0, len(one)))
            if len(points) == l:
                n-=1
        points = sorted(points)
        print(type(points))
        final_one = []
        final_two = []

        for i in range(1, len(points)):
            p1 = points[i - 1]
            p2 = points [i]

            n1 = one if i%2 == 0 else two
            n2 = two if i%2 == 0 else one

            if i==0:
                final_one += n1[0:p1]
                final_two += n2[0:p1]
            else:
                final_one += n1[p1:p2]
                final_two += n2[p1:p2]
        return final_one, final_two
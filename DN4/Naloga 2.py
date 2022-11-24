import math

stevila = [-2,-1,0,1,2]
od_avg = []

def matematika(seznam):
    najvecja = max(seznam)
    najmanjsa = min(seznam)

    avg = math.fsum(seznam)/len(seznam)
    
    for i in range(len(seznam)):

        if seznam[i] >= 0: 
            od_avg1 = abs(seznam[i] - avg)
            od_avg.append(od_avg1)

        elif seznam[i] <= 0:
            od_avg1 = abs(seznam[i] - avg)
            od_avg.append(od_avg1)
        
    stevilka = od_avg.index(min(od_avg))
    basic = seznam[stevilka]

    print(najvecja, najmanjsa, avg, basic)

matematika(stevila)
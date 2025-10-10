def gasstation(gas,cost):
    if sum(gas)<sum(cost):
        return -1

    start =0
    diff = 0

    for i in range(len(gas)):
        diff += (gas[i]-cost[i])

        if diff<0:
            diff = 0
            start = i+1

    return start

gas = list(map(int,input().split()))
cost = list(map(int,input().split()))
print(gasstation(gas,cost))
def isPossible(weights,D,capacity):
    days = 1
    curr =0
    for i in range(len(weights)):
        if curr + weights[i] > capacity:
            days += 1
            curr = weights[i]
        else:
            curr += weights[i]
    return days <= D

def shipWithinDays(weights,D):
    low = max(weights)
    high = sum(weights)
    while low<=high:
        mid  = (low+high)//2
        if isPossible(weights,D,mid):
            high = mid-1
        else:
            low = mid+1
    return low

weights = [5,4,5,2,3,4,5,6]
D = 5
print(shipWithinDays(weights, D))

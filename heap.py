import heapq
#smallest numbers Min Heap
def func(arr,k):
    heap = []

    for num in arr:
        if len(heap)<k:
            heapq.heappush(heap,-num)
        else:
            if -num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,-num)
    res = [-x for x in heap]
    return sorted(res)

def func1(arr,k):
    heap = []

    for num in arr:
        if len(heap)<k:
            heapq.heappush(heap,num)
        else:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)
    res = [x for x in heap]
    return sorted(res)



arr = list(map(int, input().split()))
k = int(input())

print(func1(arr,k))

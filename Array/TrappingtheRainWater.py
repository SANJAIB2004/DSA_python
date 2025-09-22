def trap(height,n):
    left = [0]*n
    right = [0]*n

    left[0] = height[0]
    for i in range(1,n):
        left[i] = max(left[i-1],height[i])

    right[n-1] =height[n-1]
    for i in range(n-2,-1,-1):
        right[i] = max(right[i+1],height[i])

    watermax =0
    for i in range(n):
        watermax += min(left[i],right[i]) - height[i]

    return watermax


height =[0,1,0,2,1,0,1,3,2,1,2,1]
n = len(height)
print(trap(height,n))
def numberOfSubarrays(nums,k):
    if k < 0:
        return 0
    n = len(nums)
    l = r = sums = cnt = 0
    while r < n:
        sums += (nums[r] % 2)
        while sums > k:
            sums -= (nums[l] % 2)
            l += 1
        cnt = cnt + (r - l + 1)
    return cnt

nums = [1,1,2,1,1]
k =3
print(numberOfSubarrays(nums,k))
# User function Template for python3
class Item:
    def __init__(self, values, weight):
        self.values = values
        self.weight = weight


class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        item = [Item(v, w) for v, w in zip(val, wt)]
        item.sort(key=lambda x: x.values / x.weight, reverse=True)
        curweg = 0
        finalval = 0.0

        for i in item:
            if curweg + i.weight <= capacity:
                curweg += i.weight
                finalval += i.values

            else:
                rem = capacity - curweg
                finalval += i.values * (rem / i.weight)
                break
        return finalval


# {
# Driver Code Starts
# Position this line where user code will be pasted.

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # Read values array
        values = list(map(int, input().strip().split()))

        # Read weights array
        weights = list(map(int, input().strip().split()))

        # Read the knapsack capacity
        W = int(input().strip())

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(values, weights, W))
        print("~")

# } Driver Code Ends
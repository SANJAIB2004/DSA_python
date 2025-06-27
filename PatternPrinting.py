n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *


  # --------------------------------------------------------------------------------#
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

# --------------------------------------------------------------------------------#

# for i in range(1,n+1):
#     for k in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# --------------------------------------------------------------------------------#

# for i in range(n,0,-1):
#     for k in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# Output:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# --------------------------------------------------------------------------------#

# for i in range(1,n+1):
#     for k in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print('*',end=" ")
#     print()

# Output:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# --------------------------------------------------------------------------------#

# for i in range(n,0,-1):
#     for k in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print('*',end=" ")
#     print()

# Output:
# * * * * * * * * *
#   * * * * * *
#     * * * *
#      * * *
#        *

# --------------------------------------------------------------------------------#

# for i in range(1,2*n):
#     for j in range(1,2*n):
#         if  i == n or j == n or i+j == n+1 or i-j == n-1 or j-i == n-1 or i+j == 3*n-1:
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()

# Output:
#         *
#       * * *
#     *   *   *
#   *     *     *
# * * * * * * * * *
#   *     *     *
#     *   *   *
#       * * *
#         *

# --------------------------------------------------------------------------------#

# for i in range(1,2*n):
#     i = i if i<=n else 2*n-i
#     for j in range(1,i+1):
#         print('*', end=" ")
#     print()

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# --------------------------------------------------------------------------------#

# for i in range(1,2*n): # outer loop
#     i = i if i<=n else 2*n-i
#     for _ in range(1,n-i+1): # space loop
#         print(" ",end=" ")
#     for j in range(1,i+1): # inner loop
#         print('*', end=" ")
#     print()

# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# --------------------------------------------------------------------------------#

# for i in range(1,2*n): # outer loop
#     i = i if i<=n else 2*n-i
#     for k in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print('*', end=" ")
#     print()
#
# Output:

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# --------------------------------------------------------------------------------#

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or j == 1 or i == n or j == n:
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()
#
# Output:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# --------------------------------------------------------------------------------#

# ascii = 97
#
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ", end=" ")
#     for j in range(1,2*i):
#         print(chr(ascii), end=" ")
#         ascii += 1
#     print()

# Output:
#         a
#       b c d
#     e f g h i
#   j k l m n o p
# q r s t u v w x y

# --------------------------------------------------------------------------------#


# arr = [[0,1,2],
#        [3,4,5],
#        [6,7,8]]
# n = len(arr)
# t1,t2 = 0, 0
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             t1 += arr[i][j]
#         if i+j == n-1:
#             t2 += arr[i][j]
# if t1 == t2:
#     print(f"Diagonal sum is equal: {t1} {t2}")

# output:
# Diagonal sum is equal: 12 12

 #--------------------------------------------------#
# n = 5
# mat = [[0 for _ in range(n)] for _ in range(n)]
#
# # Top row and first column
# for i in range(n):
#     for j in range(n):
#         if i == 0:
#             mat[i][j] = j + 1
#         if j == 0:
#             mat[i][j] = i + 1
#
# # Bottom row and last column
# for i in range(n - 1, -1, -1):
#     for j in range(n - 1, -1, -1):
#         if j == n - 1:
#             mat[i][j] = n - i
#         if i == n - 1:
#             mat[i][j] = n - j
#
# # Diagonal elements
# mid = n // 2
# arr = []
#
# for i in range(n):
#     for j in range(n):
#         if i == j and i <= mid:
#             mat[i][j] = i + 1
#             arr.append(mat[i][j])
#         if i > mid and i < n - 1 and i == j:
#             mat[i][j] = arr[n - 1 - i]
#
# # Print the matrix
# for row in mat:
#     for val in row:
#         print(f"{val if val != 0 else ' '}", end=" ")
#     print()

# output:
    # 1 2 3 4 5
    # 2 2     4
    # 3   3   3
    # 4     2 2
    # 5 4 3 2 1






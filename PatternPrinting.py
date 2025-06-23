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

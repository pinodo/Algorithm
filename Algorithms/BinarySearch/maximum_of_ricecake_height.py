# The number and the required length of rice cakes as N and M are given in the first line.
# The individual heights are given in the second line.
# The sum of all rice cake length is more than M.
# The customer can bring the leftover after rice cakes are cut in a certain height of the machine.
# Write a code to print the maximum length of the cutting machine for customer to bring at least the amound of M.

# Example 1
# Input
# 4 6
# 19 15 10 17
# Output
# 15

# Constraints
# 1 <= N <= 1000000
# 1 <= M <= 2000000000

def max_height(n, m, arr):
    if 1 <= n <= 1000000:
        if 1 <= m <= 2000000000:
            result = 0
            start = 0
            end = max(arr)
            while start <= end:
                total = 0
                mid = (start + end) // 2
                for x in arr:
                    if x > mid:
                        total += x - mid
                if total < m:
                    end = mid - 1
                else:
                    result = mid
                    start = mid + 1
        else:
            raise ValueError('Invalid Length')
    else:
        raise ValueError('Invalid Length')
    return result


n, m = list(map(int, input('The number of rice cakes, Length of rice cake: ').split()))
arr = list(map(int, input('Elements: ').split()))
print(max_height(n, m, arr))

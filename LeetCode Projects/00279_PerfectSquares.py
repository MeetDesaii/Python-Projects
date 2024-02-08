"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Constraints:

1 <= n <= 104
"""


def num_squares(n):
    # Initialize the dp array with infinity for all indices except 0
    dp = [float('inf')] * (n + 1)
    # There are 0 ways to sum to 0
    dp[0] = 0

    for i in range(1, n + 1):
        # Check all square numbers less than or equal to i
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]


print(num_squares(12))
print(num_squares(13))
print(num_squares(9))


"""
EXPLANATION:

Initializes a list dp of size n+1 where each element is set to positive infinity (float('inf')). This list is used to store the minimum number of perfect squares needed to sum up to each index i (ranging from 0 to n). We use positive infinity as an initial value because we want to minimize this number, and any actual number of squares will be less than infinity.

Sets the first element of the list dp[0] to 0. This is because 0 perfect square numbers sum to 0. It's the base case for our dynamic programming approach.

This loop iterates through each number from 1 to n. For each number i, we will calculate the minimum number of perfect square numbers that sum to i.

Inside the loop for each i, another loop starts with j starting from 1. This inner loop continues as long as the square of j (j*j) is less than or equal to i. The reason is we are looking for all perfect square numbers (j*j) that can contribute to sum i.

This line updates dp[i] with the minimum of its current value and dp[i - j * j] + 1. Here, dp[i - j * j] represents the least number of perfect squares that sum to the number i - j*j, and adding 1 accounts for the square number j*j we are currently considering. This ensures that dp[i] will hold the minimum number of squares needed to sum to i.

Increments j to check the next square number in the next iteration of the while loop.

Finally, the function returns dp[n], which contains the minimum number of perfect square numbers that sum to n.



- Logic and Alternatives:
The logic behind this approach is to use dynamic programming to build up the solution to n by using the solutions to smaller problems. This method is efficient because it avoids recalculating the minimum number of perfect squares for numbers less than n, which would significantly increase the computational complexity.


- Alternative Approaches:

Recursive Solution: A straightforward recursive solution could also solve this problem by trying every combination of perfect squares less than n. However, this approach would be significantly less efficient due to repeated calculations for the same sub-problems.
Breadth-First Search (BFS): This problem can also be solved using a graph-based approach where each node represents a number, and edges connect numbers to their sum with a perfect square. BFS can then be used to find the shortest path from 0 to n, which corresponds to the least number of perfect squares. This approach is more intuitive from a graph perspective but might not be as straightforward to implement as dynamic programming.
"""
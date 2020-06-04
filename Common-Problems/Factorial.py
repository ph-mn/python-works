'''Finding factorial for a given number using recursion
Time Complexity - O(N)
Space Complexity - O(1)
Spacy Complexity with recursion - O(N)
'''
def factorial(n):
    result = n
    while(n > 1):
        n -= 1
        result = result * n
    return result

def factorialWithRecursion(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(6))
print(factorialWithRecursion(5))

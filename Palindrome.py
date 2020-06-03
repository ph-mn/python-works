'''Program to find the string is palindrome or not
Time Complexity - O(N)
Space Comlexity - O(1)'''

def isPalindrome(str):
    start = 0
    end = len(str) -1
    if end < 0:
        return False
    isPal = True
    while(start < end):
        if str[start] != str[end]:
            isPal = False
            break
        start += 1
        end -= 1
    return isPal
    
print(isPalindrome("ABA"))




        

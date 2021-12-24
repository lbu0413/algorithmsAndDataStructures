def isPalindrome(str):
    left = 0
    right = len(str) - 1

    while left < right:
        if not str[left].isalnum():
            left += 1
        elif not str[right].isalnum():
            right -= 1
        elif str[left].lower() != str[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


str = "A man, a plan, a canal: Panama"
print(isPalindrome(str))

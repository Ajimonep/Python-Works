def is_palindrome(word):
    
    slice_str=word[::-1]

    return True if slice_str==word else False

    
print(is_palindrome("malayalam"))

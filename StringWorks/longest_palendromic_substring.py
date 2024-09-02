text="RACECAR "

longest_palendrome=""

length=len(text)

for i in range (0,length):

    left=i
    
    right=i

    while left>=0 and right<length and text[left]==text[right]:

        current_palindrome=text[left:right+1]

        if len(current_palindrome) >len(longest_palendrome):

            longest_palendrome=current_palindrome

        left=left-1

        right=right+1

print(longest_palendrome)

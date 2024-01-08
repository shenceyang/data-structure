
# Two Pointers: it has two pointers that both move along an iterable

"""
                        Type 1. Start at the edges and move towards till they meet

-Overall structure:
    def func(arr):
        left=0
        right=len(arr)-1
        while left<right:
            #do something depends on problem 
            #decide when to move left and right(eg left+=1, right-=1, both move)


- O(n) runtime and O(1) space

-strength: we will never have more than O(n) iterations

-Usage: 
    1.check palindrome

    2.check for target sum of a sorted array:
        Given a SORTED!!! array of unique integers and a target integer, return true if there exists 
        a PAIR!! of numbers that sum to target, false otherwise. 
    
    

"""

def check_palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True


def check_target_sum(arr,target):
    # [1,2,4,6,8,9], target=7 -> True
    # [1,2,9], target=12 -> False
    left=0
    right=len(arr)-1
    while left < right:
        if arr[left]+arr[right]==target:
            return True
        elif arr[left]+arr[right]<target:
            left+=1
        else:
            right-=1
    return False



"""     
                    Type 2. Move both pointers at the same direction till all elements are visited

-Overall structure:
    def func(arr1, arr2):
        i=0
        j=0
        while i<len(arr1) AND j<len(arr2):
            #do something depends on problem 
            #decide when to move left and right(eg i+=1, j+=1, both move)
        
        while i<len(arr1):
            # do something to the rest of arr1
            i+=1

        while j<len(arr2):
            # do something to the rest of arr2
            j+=1



- O(n+m) runtime, O(1) space

-Uasge:
    1. merge two SORTED array

    2. is_subsequence:
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
        A subsequence of a string is a new string that is formed from the original string by deleting 
        some (can be none) of the characters without disturbing the relative positions of the remaining 
        characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

def merge_two_sorted_arr(arr1, arr2):
    i=0
    j=0
    res=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while i<len(arr1):
        res.append(arr1[i])
        i+=1
    while j<len(arr2):
        res.append(arr2[j])
        j+=1
    return res


def is_subsequence(s,t):
    # s="abc", t="ahbgdc" -> True
    i=0
    j=0
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            i+=1
        j+=1
    return i==len(s)





#------------------------------------ Exercise------------------------------------
"""
 Reverse string: input s=["h","e","l","l","o"], output s=["o","l","l","e","h"]
"""
def reverse_string(s):
    # do not return anything, modify s in-place instead.
    left=0
    right=len(s)-1
    while left<right:
        #swap
        temp = s[left]
        s[left]=s[right]
        s[right]=temp  

        left+=1
        right-=1


"""
 Squares of a Sorted Array: Given an integer array nums sorted in non-decreasing order, 
                            return an array of the squares of each number sorted in non-decreasing order.

                            Input: nums = [-4,-1,0,3,10]
                            Output: [0,1,9,16,100]
"""
def sortedSquares(nums):
    res=[]
    left=0
    right=len(nums)-1
    while left<=right:
        if abs(nums[left])>abs(nums[right]):    #put the larger one in the front and reverse later
            res.append(nums[left]**2)
            left+=1
        else:
            res.append(nums[right]**2)
            right-=1
    res.reverse()
    return res

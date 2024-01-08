
""" 
                            What is Subarray?
All the elements must be adjacent to each other in the original array and in their original order.
For example, with the array [1, 2, 3, 4], the subarrays (grouped by length) are:

[1], [2], [3], [4]
[1, 2], [2, 3], [3, 4]
[1, 2, 3], [2, 3, 4]
[1, 2, 3, 4]

A subarray can be defined by two indices, the start and end. 
For example, with [1, 2, 3, 4], the subarray [2, 3] has a starting index of 1 and an ending index of 2. 
Let's call the starting index the left bound and the ending index the right bound. 

Another name for subarray in this context is "window".

-number of subarrays = n*(n+1)/2
    For any array, how many subarrays are there? If the array has a length of n, there are n subarrays of length 1.
    Then there are n - 1 subarrays of length 2, n - 2 subarrays of length 3 and so on until there is only 1 subarray
    of length n.
    
    !!so total_subarray_number = sum (k=1 to n) k 
                               = n*(n+1)/2
             

"""

#------------------------------------------------------------------------------------------------

"""
                            Sliding windows
-idea: add elements until the constraint is violated, then remove elements until the constraint is satisfied again.
       add elements from the right, remove elements from the left

-When to use sliding window?
  for problems that ask you to find valid subarrays in someway
        eg. Find the longest subarray with a sum less than or equal to k
            Find the longest substring that has at most one "0"
            Find the number of subarrays that have a product less than k


-Overall structure:
    def func(arr):
        left = 0
        set up other var to use (curr, res ...)

        for (right=0; right<len(arr); right++):
            add arr[right] to the window
            while constraint is violated:
                do some logic to remove arr[left] from the window
                left+=1

            logic to update the result 

- O(n) runtime:
    A sliding window guarantees a maximum of 2n window iterations - the right pointer can move n times and 
    the left pointer can move n times.

- Uasge:
    1. Find the longest len of subarray with a sum less than or equal to k

    2. Find the longest len of substring that contains only "1":
        You are given a binary string s. You may choose up to one "0" and flip it to a "1". 
        What is the length of the longest substring achievable that contains only "1"?
        eg: given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.

    3. number of array fit some condition:
        3.1: number of subarray porduct less than k:
            eg: input nums = [10, 5, 2, 6], k = 100, the answer is 8. 
            The subarrays with products less than k are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
"""

def longest_len_subarray_with_sum_less_than_or_equal_to_k(nums, k):
    #nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] and k = 8 -> 4 ([4, 2, 1, 1])
    left = 0
    curr = 0
    res = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        res = max(res, right - left + 1)
    return res



def longest_len_one_after_flip(s):
    #given s = "1101100111", -> 5
    left = 0
    curr = 0
    res = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1: 
            # if window broke, (kick out the leftmost 0 to refresh and continue) OR (calculate length immediately)
            if s[left] == "0":
                curr -= 1
            left += 1
        res = max(res, right - left + 1)
    return res



def number_of_subarray_product_less_than_k(nums, k):
    #input nums = [10, 5, 2, 6], k = 100 -> 8
    left = 0
    curr = 1
    res = 0
    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr /= nums[left]
            left += 1
        
        #inside of for loop to update res 
            """ [10, 5, 2, 6] -> valid window:  10     ->[10]
                                                10 5   -> [10, 5], [5]
                                                5 2    ->[5, 2], [2]
                                                5 2 6  -> [2, 6], [6]

                new non-duplicated subarray created each time window changes= right - left + 1

             """
        res = res+ right - left + 1 
        print(res)




"""
                                 Fixed window size

-sometiimes some problem will specify a fixed length k .


-Overall structure:
    def func(arr):
        curr = some data to track the window 
        
        for (i= 0 ; i<k ;i++):
            do something with curr or other vars to build first window 
        
        consider what is res equals to 
        for (i=k; i<len(arr); i++):
            add arr[i] to the window
            remove arr[i-k] from the window
            update res

        return res

-Usage:
   1.largest_sum_subarray:
        Given an integer array nums and an integer k, find the sum of the subarray with the largest sum 
        whose length is k.

    2. Maximum average subarray I:
        Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum
        average value. And you need to output the maximum average value.

        Input: nums = [1,12,-5,-6,50,3], k = 4
        Output: 12.75000
        Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

"""

def largest_sum_subarray(nums, k):
    curr = 0

    for i in range(k):
        curr += nums[i]
    
    res = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        res = max(res, curr)

    return res





def maximum_average_subarray_I(nums, k):
    curr = 0

    for i in range(k):
        curr += nums[i]
    
    res = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        res = max(res, curr)
    return float(res)/ float(k)



#---------------------------------Exercise---------------------------------------------------------------

"""
                                    Most consecutive ones

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array 
if you can flip at most k 0's.
"""

def most_consecutive_ones(nums, k):
    left = 0
    curr = 0
    res = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        res = max(res, right - left + 1)
    return res
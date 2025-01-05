def arithmeticTriplets(nums, diff):
    num_set = set(nums)  
    count = 0
    
    for j in range(1, len(nums) - 1):
      
        if (nums[j] - diff) in num_set and (nums[j] + diff) in num_set:
            count += 1
    
    return count 

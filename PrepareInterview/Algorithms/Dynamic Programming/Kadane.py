#subarray maxium 
def maximum_subarray(array): 
    n = len(array)
    local_max = 0 
    global_max = float('-inf')

    for i in range(n): 
        local_max = max(array[i], array[i] + local_max)
        if local_max > global_max: 
            global_max = local_max
    
    return global_max

# For negative number in the group
def maxSubArray(self, nums) -> int:
    if len(nums) == 1: 
        return nums[0]
    local_max = nums[0]
    global_max = nums[0]
    
    for i in range(1, len(nums)): 
        local_max = max(nums[i], local_max+nums[i]) 
        global_max = max(local_max, global_max)
    return global_max
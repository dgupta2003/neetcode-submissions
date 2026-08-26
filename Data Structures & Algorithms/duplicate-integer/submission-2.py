class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # WITH .SORT()
        # nums.sort()
        # print(f'here is the sorted nums:', nums)

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        
        # return False

        # WITH HASHSET
        hashmap = set()
        for i in nums:
            if i in hashmap:
                return True
            hashmap.add(i)
        return False
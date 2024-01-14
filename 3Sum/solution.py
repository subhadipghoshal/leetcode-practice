from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = set()

        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [nums]
            else:
                return []
        
        num_range_dict = {}
        processed_nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in num_range_dict:
                num_range_dict[nums[i]] = [i, i]
            else:
                num_range_dict[nums[i]][1] = i
            
        for i in range(len(nums) - 2):
            if i not in processed_nums_dict:
                processed_nums_dict[nums[i]] = i

                if i > 0 and nums[i] == nums[i-1]:
                    continue

                # Use two pointers to find the remaining two numbers
                left, right = i + 1, len(nums) - 1

                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total == 0:
                        results.add(tuple([nums[i], nums[left], nums[right]]))
                        left = num_range_dict[nums[left]][1] + 1
                        right = num_range_dict[nums[right]][0] - 1
                    elif total < 0:
                        left += 1
                    else:
                        right -= 1

        return results
    


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([0, 0, 0, 0]))
print(solution.threeSum([0, 0, 0]))
print(solution.threeSum([0,1,1]))
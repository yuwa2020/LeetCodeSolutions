"""
LeetCode Problem #1: Two Sum

Problem:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Approach:
Use a hash map to store the numbers we've seen so far and their indices.
For each number, check if (target - number) exists in the hash map.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash map stores at most n elements
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in array that sum to target.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing indices of the two numbers
        """
        # Dictionary to store number -> index mapping
        num_map = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if complement exists in our map
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store current number and its index
            num_map[num] = i
        
        # Should never reach here given problem constraints
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("Test case 1 passed: [2,7,11,15], target=9 -> [0,1]")
    
    # Test case 2
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    print("Test case 2 passed: [3,2,4], target=6 -> [1,2]")
    
    # Test case 3
    assert solution.twoSum([3, 3], 6) == [0, 1]
    print("Test case 3 passed: [3,3], target=6 -> [0,1]")
    
    print("\nAll test cases passed!")

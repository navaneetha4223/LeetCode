class Solution(object):

    def searchRange(self, nums, target):

        # Find first occurrence
        def first_position():

            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:

                mid = (left + right) // 2

                # Target found
                if nums[mid] == target:

                    ans = mid
                    right = mid - 1

                # Search right side
                elif nums[mid] < target:
                    left = mid + 1

                # Search left side
                else:
                    right = mid - 1

            return ans

        # Find last occurrence
        def last_position():

            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:

                mid = (left + right) // 2

                # Target found
                if nums[mid] == target:

                    ans = mid
                    left = mid + 1

                # Search right side
                elif nums[mid] < target:
                    left = mid + 1

                # Search left side
                else:
                    right = mid - 1

            return ans

        return [first_position(), last_position()]
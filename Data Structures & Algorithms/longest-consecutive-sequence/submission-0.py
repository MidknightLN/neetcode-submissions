class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## Sort array
        # max_count = 0
        # nums = sorted(list(set(nums)))
        # print(nums)
        # temp_count = 1
        # for idx, val in enumerate(nums):
        #     if val-1 == nums[idx-1]:
        #         temp_count += 1
        #     else:
        #         max_count = max(max_count, temp_count)
        #         temp_count = 1
        # return max(max_count, temp_count)

        ## Hash set
        num_set = set(nums)
        max_count = 0

        for num in num_set:
            # 如果他前面有數字 代表他不是開頭
            if (num -1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                max_count = max(length, max_count)
        return max_count


        
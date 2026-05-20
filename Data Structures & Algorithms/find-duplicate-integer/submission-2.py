class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #龜兔賽跑演算法步驟
        #我們可以使用雙指標：烏龜（慢指標，一次走一步） 與 兔子（快指標，一次走兩步）。
        #階段一：尋找相遇點（確認有環）

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if fast == slow:
                return fast

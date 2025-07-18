class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k - 1
        mxAverage = 0
        summer = 0
        for i in range(0, k):
            summer += nums[i]
        mxAverage = summer/k

        divider = 0
        for i in range(k, len(nums)):
            summer += nums[i]
            summer -= nums[divider]
            mxAverage = max(mxAverage, summer/k)
            divider += 1
        return mxAverage

        

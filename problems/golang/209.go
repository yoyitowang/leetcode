func minSubArrayLen(target int, nums []int) int {
    left := 0
    right := 0
    n := len(nums)
    res := n + 1
    sum := 0

    for ;right < n; right++ {
        sum += nums[right]
        for ;sum >= target; left++ {
            res = min(res, right-left+1)
            sum -= nums[left]
        }
    }

    if res > n {
        return 0
    }

    return res
}
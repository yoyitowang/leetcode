func threeSum(nums []int) [][]int {
    var res [][]int
    sort.Ints(nums)
    for idx:=0; idx<len(nums); idx++ {
        if idx > 0 && nums[idx-1]==nums[idx] {
            continue
        }
        left := idx + 1
        right := len(nums)-1
        for left < right {
            _sum := nums[idx] + nums[left] + nums[right]
            if _sum == 0 {
                res = append(res, []int{nums[idx], nums[left], nums[right]})
                for left < right && nums[left] == nums[left+1] {left++}
                for left < right && nums[right] == nums[right-1] {right--}
                left++
                right--
            } else if _sum < 0 {
                left++
            } else {
                right--
            }
        }
    }

    return res
}
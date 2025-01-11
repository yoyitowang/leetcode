func removeDuplicates(nums []int) int {
    left, right := 0, 0
    for right < len(nums) {
        if left == 0 || nums[left-1] != nums[right] {
            nums[left] = nums[right]
            left += 1
        }
        right += 1
    }
    return left
}
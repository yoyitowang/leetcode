func sortedSquares(nums []int) []int {
	left := 0
	right := len(nums) - 1
	// 初始化一個固定大小的切片，長度為 nums 的長度
	res := make([]int, len(nums))
	// 用於填充結果的索引，從最後一位開始
	index := len(nums) - 1

	for left <= right {
		// 計算左右指針對應數字的平方
		leftSquare := nums[left] * nums[left]
		rightSquare := nums[right] * nums[right]

		// 比較平方值，將較大的值放入結果切片的尾部
		if leftSquare > rightSquare {
			res[index] = leftSquare
			left++
		} else {
			res[index] = rightSquare
			right--
		}
		index-- // 填充索引向前移動
	}

	return res
}
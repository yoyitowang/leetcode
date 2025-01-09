package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	// 讀取數組長度 n
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	// 構建前綴和數組
	prefixSum := make([]int, n+1)
	for i := 0; i < n; i++ {
		scanner.Scan()
		num, _ := strconv.Atoi(scanner.Text())
		prefixSum[i+1] = prefixSum[i] + num
	}

	// 處理查詢並輸出結果
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	for scanner.Scan() {
		// 讀取查詢區間
		line := scanner.Text()
		parts := strings.Split(line, " ")
		if len(parts) != 2 {
			fmt.Fprintln(writer, "Invalid query format")
			continue
		}

		start, err1 := strconv.Atoi(parts[0])
		end, err2 := strconv.Atoi(parts[1])

		// 檢查輸入是否合法
		if err1 != nil || err2 != nil || start < 0 || end >= n || start > end {
			fmt.Fprintln(writer, "Invalid query range")
			continue
		}

		// 計算區間和
		result := prefixSum[end+1] - prefixSum[start]
		fmt.Fprintln(writer, result)
	}
}
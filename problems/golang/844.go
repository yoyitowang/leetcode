func backspaceCompare(s string, t string) bool {
    sList := []rune(s)
    tList := []rune(t)
    left, right := 0, 0
    for ; right < len(s); right++ {
        if string(sList[right]) == "#" {
            if left > 0 {left -= 1}
        } else {
            sList[left] = sList[right]
            left += 1
        }
    }
    newS := string(sList[:left])
    left, right = 0, 0
    for ; right < len(t); right++ {
        if string(tList[right]) == "#" {
            if left > 0 {left -= 1}
        } else {
            tList[left] = tList[right]
            left += 1
        }
    }
    newT := string(tList[:left])
    return newS == newT
}
func removeDuplicates(s string) string {
    st := []rune{}
    for _, char := range s {
        if len(st) > 0 && char == st[len(st)-1] {
            st = st[:len(st)-1]
        } else {
            st = append(st, char)
        }
    }
    return string(st)
}
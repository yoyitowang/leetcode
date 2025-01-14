def main():
    s = list(input())
    n = len(s)
    cnt = 0
    for char in s:
        if char.isdigit():
            cnt += 1
    res = []
    for char in s:
        if char.isdigit():
            for i in "number":
                res.append(i)
        else:
            res.append(char)
        
    print( ''.join(res))
    
main()
def main():
    n = int(input())
    s = input()
    s = reverse(s)
    print(reverse(s[:n])+reverse(s[n:]))
    
    
def reverse(s: str):
    s = list(s)
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        
    return ''.join(s)
    
main()
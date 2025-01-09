import sys
input = sys.stdin.read

def main():
    data = input().split()
    index = 0
    n = int(data[index])
    
    ht = [0]*n
    _sum = 0
    for idx, num in enumerate(range(1, n+1)):
        _sum += int(data[num])
        ht[idx] = _sum
    
    q = data[n+1:]
    for i in range(0, len(q), 2):
        start, end = int(q[i]), int(q[i+1])
        if start == 0:
            print(ht[end])
        else:
            print(ht[end]-ht[start-1])
        
if __name__ == "__main__":
    main()
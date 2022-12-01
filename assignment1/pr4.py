# problem 4 find second maximum number in a list
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(set(arr))
    a=sorted(l)
    print(a[-2])
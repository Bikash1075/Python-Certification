# problem 3
n= int(input())
s1=set(map(int,input().split()))
n=int(input())
s2=set(map(int,input().split()))
s3=s1.intersection(s2)
l=len(s3)
print(l)
# problem 11 leap year
def is_leap(year):
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    return False
year = int(input())
print(is_leap(year))

# 2nd approach
def is_leap(year):
    return(year%400==0) or ((year%100!=0) and (year%4==0))
year = int(input())
print(is_leap(year))


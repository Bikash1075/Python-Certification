# problem 1 finding percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    k=[]
    if query_name in student_marks.keys():
        k=student_marks[query_name]
        s=sum(k);l=len(k)
        a=s/l
    print("{:.2f}".format(a))
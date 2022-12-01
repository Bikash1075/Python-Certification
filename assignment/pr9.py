# problem 9 nested list Second minimum score
if __name__ == '__main__':
    l=([])
    l1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
      
    for i in range (len(l)):
        if l[i][1] not in l1:
            l1.append(l[i][1])
    for i in range(len(l)):
        sl = sorted(l)
        if sorted(l1)[1]==sl[i][1]:
            print(sl[i][0])
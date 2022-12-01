l=sorted ([['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['Harsh',39]])
# l=sorted([])
l1=[]
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     l.append([name,score])
      
for i in range (len(l)):
    if l[i][1] not in l1:
        l1.append(l[i][1])
print(l1)
for i in range(len(l)):
    if sorted(l1)[1]==l[i][1]:
        print(l[i][0])
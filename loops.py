'''
# part 1 
# 1
i= 0
while i <=5:
    print(i)
    i+=1
# 2
i=10
while i >=0:
    print(i)
    i=i-1
# 3
total=0
while total<10:
    total+=1
print(total)
# 4
items = [2, 4, 6, 8]
i=0
while i < len(items)-1:
    print(items[i])
    i+=1
    if items[i]>5:
        break
# 5

i=0
while i<=10:
    if i%2==0:
        print(i)
    i=i+1
# 6

agents = ['Alpha', 'Bravo', 'Charlie']
i=0
while i<len(agents):
    print(agents[i])
    i+=1

# 8
i=1
while i*2<100:
   i=i*2
print(i)
# 9

data = [3, 7, 2, -1, 5]
i=0
sum=0
while i <len(data):
    if data[i]==-1:
        break
   
    sum=sum+data[i]
    i=i+1
print(sum)

#10
#1
items = ['a', 'x', 'b', 'x', 'x']
i=0
while i < len(items):
    items.remove("x")
    i+=1
print(items)
# 2

matrix = [[1, 2], [3, 4], [5, 6]]
i=0

while i<len(matrix):
   
    x=0
    while x<len(matrix[i]):
        print(matrix[i][x])
        x+=1
    i+=1
# 3 

num=[1,2,3,4,5]
i=len(num)-1
while i >=0:
    print(num[i])
    i=i-1
# 4
'''
data = [10, 30, 55, 20, 80]
i=0
while i < len(data):
    if data[i]>=50:
        print(i)
    i+=1
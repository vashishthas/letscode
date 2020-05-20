lst = [] 
nelst=[]
  
n = int(input("Enter number of elements : ")) 
  
for i in range(n): 
    ele = int(input()) 
    lst.append(ele) 

for i in range(n):
    if lst[i]>0:
        nelst.append(lst[i])
print(nelst)

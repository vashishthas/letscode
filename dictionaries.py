s=input("enter a string ")
s=s.lower()
z=len(s)
freq={}
for x in s:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1

a = sorted(freq.items(), key=lambda x: x[1], reverse=True)    
print(a)

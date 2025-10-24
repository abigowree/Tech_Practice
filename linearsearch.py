num=[10,2,3,2,4]
n=int(input("number:"))
for i in range(len(num)):
    if n==num[i]:
        print(i)
        break
else:
    print(-1)   
    
arr=[10,2,4,10,5]
max=arr[0]
count=0
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]        
for i in arr:
    if i==max:
        count+=1
print(count)    
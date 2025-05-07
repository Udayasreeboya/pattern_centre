rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==rows or i==1 or j==rows or j==1 or j==mid and i==mid:
            res+="*"+" "
        else:
            res+=" "+ " "
    print(res)
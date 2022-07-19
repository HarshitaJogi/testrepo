list = [2, 1, 5, 3]
target = 4
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]+list[j]==target:
            print(i,j)









#for i in list:
    #for j in list:
        #if i + j == 4:
           # print(i, j)
        #else:
            #i=i+1
            #j=j+1
names="yahya ali saied nourhan faisal nour "
count=[]
cnt=1
names1=names.split()
# counting the numbers of letters in names1
for i in names1 :  
    for j in i :        
        count.append(cnt)
        cnt +=1

#turning it to string                 
count_string=[str(counts) for counts in count]

count_string1=[]
for i in names1  :   
    count_string1.append(count_string[0:len(i)]) #Slicing every count_string with 
    # each matching name and append it to a new list

x=len(count_string1)
for i in range(x):
    print(f"{names1[i]} is {''.join(count_string1[i])}")





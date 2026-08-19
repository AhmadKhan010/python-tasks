# an empty list to store the numbers
result=[]

# iterate through the range given to find the numbers
for i in range(2000,3601):
    if i%7 == 0 and i%5 != 0:
        result.append(i)

# print the list of numbers separated by comma
for i in range(len(result)):
    if i == (len(result)-1):    # just to avoid the trailing comma
        print(result[i])
    else:
        print(result[i], end=',')
        
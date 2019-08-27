# Python-beginners-tasks
file = input("filename:")
index=0
for x in range(len(file)):
    if file[x]== '.':
            index= x
print(file[index+1:])

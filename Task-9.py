# Python-beginners-tasks
numbers  = (1,2,3,4,5,6,7,8,9)
odd_numbers = 0
even_numbers = 0
for x in numbers:
    if x % 2==0:
            even_numbers+=1
    else:
            odd_numbers+=1
print("Number of even numbers :",even_numbers)
print("Number of odd numbers :",odd_numbers)

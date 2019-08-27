# Python-beginners-tasks
ab= int(input("Enter the size of a side of the triangle : "))
bc= int(input("Enter the size of a side of the triangle : "))
ca= int(input("Enter the size of a side of the triangle : "))
if ab==bc==ca :
   print("Equilateral Triangle")
elif ab==bc or bc==ca or ca==ab :
   print("Isosceles Triangle")
else :
   print("Scalene Triangle")

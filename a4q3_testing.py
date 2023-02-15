from a4q3 import Statistics
#creating Statistics object called m
m = Statistics()
#adding element
m.add(1)
#adding element
m.add(7)
#adding element
m.add(4)
#adding element
m.add(9)
#adding element
m.add(7)
#adding element
m.add(2)

#calling mean and printing the return value
print("The mean is:",m.mean())
#calling mode and printing the return value
print("The mode is:",m.mode())
#calling range and printing the return value
print("The range is:",m.range())
#calling min and printing the return value
print("The minimum element is:",m.min())
#calling max and printing the return value
print("The maximum element is:",m.max())
#calling count and printing the return value
print("The count is:",m.count())

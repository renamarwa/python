names=input("Enter first names(space seperated):").split()
count_a=sum(name.lower().count('a')for name in names)
print("Total number of'a' in the list:", count_a)
      

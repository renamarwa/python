ints = input("Enter the list of integers seperared by spaces")
parts= ints.split()
n=[]
for p in parts:
    n.append(int(p))
print("Before modyfying :")
print(n)
result = []
for num in n:
    if num>100:
        result.append("over")
    else:
        result.append(num)
print("\n Modified List :")
print(result)

n==start=int(input("Enter the starting number of the range:"))
end=int(input("Enter the ending number of the range:"))
print("Four-digit numbers with all even digits and perfect squares are:")
for num in range(start, end+1):
    if 1000<= num<=999:
        digits=str(num)
        if all(int(d)%2==0 for d in digits):
            root=int(num**0.5)
            if root*root==num:
                print(num)

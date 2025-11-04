string=input("Enter a string:")
if len(string)>=3:
    if string.endswith("ing"):
        string=string+"ly"
    else:
        string=string+"ing"
else:
      string=string
print("Modified string:",string)






















  

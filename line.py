line=input("Enter a line of text:")
words=line.split()
word_count={word: words.count(word)for word in words}
print("Word occurences:")
for word, count in word_count.items():
    print(f"{word}: {count}")
            

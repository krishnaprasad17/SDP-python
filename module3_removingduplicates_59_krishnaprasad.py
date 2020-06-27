#REMOVE ALL DUPLICATES
word=input("enter your string :")
NewWord = " "
index = 0
for char in word:
    if char != NewWord[index]:
            NewWord += char
            index += 1
     
print(NewWord.strip())

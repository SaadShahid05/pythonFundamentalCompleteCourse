print("This program will count total number of vowels from user defined sentence")
string = input("enter your string here: ")
vowels = 0
for i in string: 
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        print("the vowel is:", i)
        vowels += 1
print("the number of vowels are: ")
print(vowels)

print("Hello World")

char = input("Enter a char: ").split()
new_char = [len(i) for i in char]
print(new_char)
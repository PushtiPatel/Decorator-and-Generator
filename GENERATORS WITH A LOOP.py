#Reverse a string
def reverse_str(test_str):
    length = len(test_str)
    for i in range(length - 1, -1, -1):
        yield test_str[i]
for char in reverse_str("Python"):
    print(char,end =" ")
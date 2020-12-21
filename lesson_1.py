# task 1
# Use the built-in function `print` in it several times.
# Try to pass “sep”, “end” params and pass several parameters separated by commas.
if __name__ == '__main__':
    print(1, 3, 5, 7, 11, sep='#')  # Ex. 1#3#5#7#11
    print(1, 3, 5, 7, 11, sep='#', end='\t')
    print(1, 3, 5, 7, 11, end='!')  # Ex. 1#3#5#7#11	1 3 5 7 11!
# task 2
# Write a program, which has two print statements to print the following text
# (capital letters “O” and “H”, made from “#” symbols).
# Pay attention that usage of spaces is forbidden,
# as well as creating the whole result text string using “”” ”””, use ‘\n’ and ‘\t’ symbols instead.
    print('#########')
    print('#', end='\t\t')
    print('#')
    print('#', end='\t\t')
    print('#')
    print('#', end='\t\t')
    print('#')
    print('#########', end='\n\n')
    print('#', end='\t\t')
    print('#')
    print('#', end='\t\t')
    print('#')
    print('#########')
    print('#', end='\t\t')
    print('#')
    print('#', end='\t\t')
    print('#')

s = input()
numbers = s.split('+')
numbers.sort()  # This works since '1' < '2' < '3' as strings
print('+'.join(numbers))


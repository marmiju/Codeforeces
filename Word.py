word = input()

lowercase_count = sum(1 for c in word if c.islower())
uper_count = len(word) - lowercase_count
if uper_count > lowercase_count : 
    print(word.upper())
else :
    print(word.lower())


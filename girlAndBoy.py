def girlsBoy(s:str):
    unique_text = set(s)
    N = len(unique_text)

    if N % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')

s = input()
girlsBoy(s)
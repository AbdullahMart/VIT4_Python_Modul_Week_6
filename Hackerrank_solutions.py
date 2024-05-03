#Question 1: Swap Case
def swap_case(s):
    res = ''
    for ch in s:
        if ch.isupper():
            res += ch.lower()
        else:
            res += ch.upper()
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#Question 2:
def split_and_join(line):
    # write your code here
    return '-'.join(line.split())
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)




#Question 3: (Mutations)

def mutate_string(string, position, character):
    Mutated = string[:position] + character + string[position+1:]
    return Mutated


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)



#Question 4:
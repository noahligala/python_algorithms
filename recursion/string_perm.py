def permute(string):
    if len(string) == 0:
        return [""]
    
    permutations = []

    for i in range(len(string)):
        letter = string[i]
        rest = string[:i] + string[i+1:]
        sub_permutations = permute(rest)
        
        for sub_permutation in sub_permutations:
            permutations.append(letter + sub_permutation)

    return permutations

result = permute("HELLO")
for perm in result:
    print(perm)

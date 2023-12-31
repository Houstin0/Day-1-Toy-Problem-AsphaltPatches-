def solution(S):
    N = len(S)
    patches = 0
    i = 0

    while i < N:
        if S[i] == 'X':
            patches += 1
            i += 3
        else:
            i += 1
    return patches

print(solution(".X..X"))  
print(solution("X.XXXXX.X."))
print(solution("XX.XXX.."))  
print(solution("XXXX"))  
print(solution('.X...XX')) 
print(solution('...XX.X')) 
print(solution('...XX.X.........X..X.......X.')) 


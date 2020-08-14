def solution(s):
    salutes = 0
    for x in range(0,len(s)):
        pos = s[x]
        left_space = s[:x]
        right_space = s[x+1:]
        if pos == '>':
            opp = right_space.count('<')
            salutes += opp
        elif pos == '<':
            opp2 = left_space.count('>')
            salutes += opp2
    return(salutes)

string = '--->-><-><-->-'
s2 = ">----<"
print(solution(string))
print(solution(s2))
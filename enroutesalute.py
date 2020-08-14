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
print(solution(string))


#Se me ocurre que puede ser, para x contar la cantidad de opuestos que vienen de frente y sumarlo para el string completo.
#Lo otro que se me ocurre es en vez de ir uno por uno, contarlo una vez para las combinaciones del string completo.
#Los < se tienen que contar al reves, de derecha a izq.
#podría guardarlos todos que no sean "-"
import ply.lex as lex
import ply.yacc as yacc

tokens = ['SYMBOL', 'COUNT']

t_ignore = ' \t'
t_SYMBOL = r'A[cglmrstu]|B[aehikr]?|C[adeflmnorsu]?|D[bsy]|E[rsu]|F[elmr]?|G[ade]|H[efgos]?|I[nr]?|Kr?|L[airuv]|M[cdgnot]|N[abdehiop]?|O[gs]?|P[abdmortu]?|R[abefghnu]|S[bcegimnr]?|T[abcehilms]|U|V|W|Xe|Yb?|Z[nr]'

def t_COUNT(t):
     r'\d+'
     t.value = int(t.value)
     return t

def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

error = False

def t_error(t):
    global error
    error = True
    t.lexer.skip(1)

lexer = lex.lex()

line = ""
data = ""
count = 0
symbol = ""

while True:
    line = input("")
    if line == "#":
        break
    if data == "":
        data = line
    else:
        data += '\n' + line

def p_formula_group_formula(p):
    '''formula : group formula'''
    p[0] = ('FORMULA', p[1], p[2])

def p_formula_group(p):
    '''formula : group'''
    p[0] = p[1]
 
def p_group_symbol_count(p):
    'group : SYMBOL COUNT'
    p[0] = ('GROUP', p[1], p[2])
    global count, symbol, error
    count += p[2]
    if symbol == p[1]:
        error = True
    symbol = p[1]

def p_group_symbol(p):
    'group : SYMBOL'
    p[0] = ('GROUP', p[1])
    if p[0] != "":
        global count, symbol, error
        count += 1
        if symbol == p[1]:
            error = True
        symbol = p[1]

def p_error(p):
    global error
    error = True


parser = yacc.yacc(errorlog=yacc.NullLogger())

for formula in data.splitlines():
    result = parser.parse(formula, debug=False)
    if error:
        print("Error in formula")
    else:
        print(count)
    
    count = 0
    error = False


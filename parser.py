import ply.yacc as yacc
import lexer
tokens = lexer.tokens
literals = lexer.literals

vars = {}

def p_program(p):
    '''program : statement program
               | statement'''

    if len(p) == 2 and p[1]:
         p[0] = {}
         line, statement = p[1]
         p[0][line] = statement
    elif len(p) == 3:
         p[0] = p[1]
         if not p[0]:
            p[0] = {}
         if p[2]:
            line, statement = p[2]
            p[0][line] = statement

def p_statement_assign(p):
    '''statement : NAME '=' expression'''
    vars[p[1]] = p[3]

def p_expression_plus(p):
    '''expression : expression '+' term'''
    p[0] = p[1] + p[3]
 
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_name(p):
    'factor : NAME'
    try:
        p[0] = vars[p[1]]
    except LookupError:
        print("Error in input")
        exit()

def p_factor_expression(p):
    '''factor : '(' expression ')' '''
    p[0] = p[2]

def p_error(p):
    print("Error in input")
    exit()

parser = yacc.yacc(errorlog=yacc.NullLogger())
result = parser.parse(lexer.data, debug=False)
print("Accepted")
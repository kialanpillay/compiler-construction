import ply.lex as lex

tokens = ['NAME', 'NUMBER']
literals = [ '+','=', '(', ')']

t_ignore = ' \t'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
     r'\d+'
     t.value = int(t.value)
     return t

def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

def t_error(t):
     if __name__ == "__main__":
        print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

lexer = lex.lex()

line = ""
data = ""

while True:
    line = input("")
    if line == "#":
        break
    if data == "":
        data = line
    else:
        data += '\n' + line

lexer.input(data)

while True:
     tok = lexer.token()
     if not tok: 
         break
     if __name__ == "__main__":
        print(('{}'.format(tok.type), tok.value, tok.lineno, tok.lexpos))
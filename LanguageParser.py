import ply.yacc as yacc

from lexer import *

# fmt: off

def p_program(p):
    '''program : func_declaration
               | func_declaration program'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_func_declaration(p):
    '''func_declaration : signature block'''
    p[0] = sa.FuncDeclConcrete(p[1], p[2])
    











f = open("teste_parser.txt", "r")
parser = yacc.yacc()
result = parser.parse(input=f.read(), debug=True)

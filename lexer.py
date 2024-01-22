import ply.lex as lex

tokens = []

keyword_list = [
    'bool', 'break', 'case', 'catch', 'char', 'class', 'const', 'continue', 'decimal',
    'default', 'do', 'double', 'else', 'enum', 'false', 'finally', 'float', 'for',
    'foreach', 'goto', 'if', 'in', 'int', 'interface', 'is', 'long', 'namespace', 'new',
    'null', 'out', 'override', 'params', 'private', 'protected', 'public', 'readonly',
    'ref', 'return', 'short', 'sizeof', 'static', 'string', 'struct', 'switch', 'this',
    'throw', 'true', 'try', 'typeof', 'uint', 'ulong', 'ushort', 'void', 'while'
]

reserved_words = {}
for keyword in keyword_list:
    name = keyword.upper()
    reserved_words[keyword] = name
    tokens.append(name)

tokens += [
    'PLUSPLUS', 'MINUSMINUS', 'PLUS', 'MINUS', 'STAR', 'SLASH', 'PERCENT',
    'BANG', 'AMPER', 'CIRCUMFLEX', 'PIPE', 'AMPERAMPER', 'PIPEPIPE',
    'TILDE', 'LSHIFT', 'RSHIFT',
    'EQEQUAL', 'NOTEQUAL', 'LT', 'GT', 'LEQ', 'GEQ',
    
    'EQUAL', 'PLUSEQUAL', 'MINUSEQUAL', 'STAREQUAL', 'SLASHEQUAL', 'PERCENTEQUAL',
    'AMPEREQUAL', 'PIPEEQUAL', 'CIRCUMEQUAL',
    'LSHIFTEQUAL', 'RSHIFTEQUAL', 'URSHIFTEQUAL',
    'HOOKHOOK', 'HOOKHOOKEQUAL',
    
    'COLON', 'COMMA', 'SEMI', 'DOT',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LSB', 'RSB',
    
    'INTNUM', 'FLOATNUM', 'DOUBLENUM', 'DECIMALNUM',
    'BINARYNUM', 'OCTALNUM', 'HEXADECIMALNUM',
    'CHARLITERAL',
    'STRINGLITERAL',
]
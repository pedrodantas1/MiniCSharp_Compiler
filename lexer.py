import ply.lex as lex

# fmt: off
tokens = []

keyword_list = [
    'bool', 'break', 'case', 'char', 'class', 'const', 'continue', 'decimal',
    'default', 'do', 'double', 'else', 'false', 'float', 'for', 'foreach',
    'if', 'in', 'int', 'is', 'long', 'new', 'object', 'null', 'private',
    'protected', 'public', 'return', 'static', 'string', 'switch', 'this',
    'true', 'void', 'while'
]

reserved = {}
for keyword in keyword_list:
    name = keyword.upper()
    reserved[keyword] = name
    tokens.append(name)

tokens += [
    'PLUSPLUS', 'MINUSMINUS', 'PLUS', 'MINUS', 'STAR', 'SLASH', 'PERCENT',
    'BANG', 'AMPER', 'CIRCUMFLEX', 'PIPE', 'AMPERAMPER', 'PIPEPIPE',
    'LSHIFT', 'RSHIFT',
    'EQEQUAL', 'NOTEQUAL', 'LT', 'GT', 'LEQ', 'GEQ',
    
    'EQUAL',
    
    'HOOK', 'COLON', 'COMMA', 'SEMI', 'DOT',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LSB', 'RSB',
    
    'INTNUM', 'FLOATNUM', 'DOUBLENUM', 'DECIMALNUM',
    'BINARYNUM', 'HEXADECIMALNUM',
    'CHARLITERAL',
    'STRINGLITERAL',
    'ID'
]

t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_PERCENT = r'%'

t_BANG = r'!'
t_AMPER = r'&'
t_CIRCUMFLEX = r'\^'
t_PIPE = r'\|'
t_AMPERAMPER = r'&&'
t_PIPEPIPE = r'\|\|'

t_LSHIFT = r'<<'
t_RSHIFT = r'>>'

t_EQEQUAL = r'=='
t_NOTEQUAL = r'!='
t_LT = r'<'
t_GT = r'>'
t_LEQ = r'<='
t_GEQ = r'>='

t_EQUAL = r'='

t_HOOK = r'\?'
t_COLON = r':'
t_COMMA = r','
t_SEMI = r';'
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LSB = r'\['
t_RSB = r'\]'


def t_HEXADECIMALNUM(t):
    r'0[xX]([0-9a-fA-F]+)'
    return t


def t_BINARYNUM(t):
    r'0[bB]([0-1]+)'
    return t


def t_FLOATNUM(t):
    r'[+-]?(([0-9]+[.][0-9]+)|([.][0-9]+))[fF]'
    return t


def t_DECIMALNUM(t):
    r'[+-]?(([0-9]+[.][0-9]+)|([.][0-9]+))[mM]'
    return t


def t_DOUBLENUM(t):
    r'[+-]?(([0-9]+[.][0-9]+)|([.][0-9]+))[dD]?'
    return t


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CHARLITERAL(t):
    r'\'([^\'\\\u000D\u000A]|\\\'|\\\\|\\"|\\0|\\a|\\b|\\f|\\n|\\r|\\t|\\v)\''
    return t


def t_STRINGLITERAL(t):
    r'\"([^\"\\\u000D\u000A]|(\\.))*?\"'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_comment(t):
#   r'(\/\/.*)|(\/\*(.|\n)*?\*\/)'
#   r'(\/\/)(.*?)(?=[\n\r])|(\/\*(.|\n)*?\*\/)'
    r'(\/\/)(.*?)([\n\r])|(\/\/.*)|(\/\*(.|[\n\r])*?\*\/[\n\r]?)'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    msg = "\n# ERROR: Illegal character '%s' at line %d\n" % (t.value[0], t.lineno)
    print(msg)
    t.lexer.skip(1)


t_ignore = ' \t'

if __name__ == "__main__":
    f = open("teste_lexer.txt", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    t = lexer.token()
    while t:
        print(t)
        t = lexer.token()
    # print('{:10s}{:10s}{:10s}{:10s}'.format("Token", "Lexema", "Linha", "Coluna"))
    # for tok in lexer:
    #     print('{:10s}{:10s}{:10s}{:10s}'.format(tok.type, tok.value, str(tok.lineno), str(tok.lexpos)))

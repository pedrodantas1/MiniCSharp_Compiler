import ply.yacc as yacc

import SintaxeAbstrata as sa
from lexer import *

# fmt: off

def p_type_name(p):
    '''type_name : ID
                 | type_name DOT ID'''
    if (len(p) == 2):
        p[0] = sa.SingleTypeName(p[1])
    else:
        p[0] = sa.CompoundTypeName(p[1], p[3])

def p_type_class(p):
    '''type : class_type
            | interface_type
            | value_type'''
    if (isinstance(p[1], sa.ClassType)):
        p[0] = sa.TypeClass(p[1])
    elif (isinstance(p[1], sa.InterfaceType)):
        p[0] = sa.TypeInterface(p[1])
    elif (isinstance(p[1], sa.ValueType)):
        p[0] = sa.TypeValue(p[1])

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
    
def p_signature(p):
    '''signature : type ID LPAREN param_list RPAREN
                 | type ID LPAREN RPAREN'''
    if (isinstance(p[4], sa.ParamList)):
        p[0] = sa.SignatureConcrete(p[1], p[2], p[4])
    else:
        p[0] = sa.SignatureConcrete(p[1], p[2], None)

def p_param_list(p):
    '''param_list : type ID
                  | type ID COMMA param_list'''
    if (len(p) == 3):
        p[0] = sa.SingleParamList(p[1], p[2])
    else:
        p[0] = sa.CompoundParamList(p[1], p[2], p[4])

def p_statement_list(p):
    '''statement_list : statement
                      | statement statement_list'''
    if (len(p) == 2):
        p[0] = sa.SingleStatementList(p[1])
    else:
        p[0] = sa.CompoundStatementList(p[1], p[2])

def p_statement(p):
    '''statement : declaration_statement
                 | embedded_statement'''
    if (isinstance(p[1], sa.DeclarationStatement)):
        p[0] = sa.StatementDeclaration(p[1])
    elif (isinstance(p[1], sa.EmbeddedStatement)):
        p[0] = sa.StatementEmbedded(p[1])

def p_declaration_stmt(p):
    '''declaration_statement : const_declaration SEMI
                             | var_declaration SEMI'''
    if (isinstance(p[1], sa.ConstDeclaration)):
        p[0] = sa.DeclarationStmtConst(p[1])
    elif (isinstance(p[1], sa.VarDeclaration)):
        p[0] = sa.DeclarationStmtVar(p[1])

def p_const_declaration(p):
    '''const_declaration : CONST type const_declarators'''
    p[0] = sa.ConstDeclarationConcrete(p[2], p[3])

def p_const_declarators(p):
    '''const_declarators : const_declarator
                         | const_declarator COMMA const_declarators'''
    if (len(p) == 2):
        p[0] = sa.SingleConstDeclarators(p[1])
    else:
        p[0] = sa.CompoundConstDeclarators(p[1], p[3])

def p_const_declarator(p):
    '''const_declarator : ID EQUAL exp'''
    p[0] = sa.ConstDeclaratorConcrete(p[1], p[3])

def p_var_declaration(p):
    '''var_declaration : type var_declarators'''
    p[0] = sa.VarDeclarationConcrete(p[1], p[2])

def p_var_declarators(p):
    '''var_declarators : var_declarator
                       | var_declarator COMMA var_declarators'''
    if (len(p) == 2):
        p[0] = sa.SingleVarDeclarators(p[1])
    else:
        p[0] = sa.CompoundVarDeclarators(p[1], p[3])

def p_var_declarator(p):
    '''var_declarator : ID
                      | ID EQUAL exp'''
    if (len(p) == 1):
        p[0] = sa.VarDeclaratorId(p[1])
    else:
        p[0] = sa.VarDeclaratorIdExp(p[1], p[3])

def p_embedded_stmt(p):
    '''embedded_statement : block
                          | empty_statement
                          | exp_statement
                          | selection_statement
                          | iteration_statement
                          | jump_statement'''
    if (isinstance(p[1], sa.BlockStmt)):
        p[0] = sa.EmbeddedStmtBlock(p[1])
    elif (isinstance(p[1], sa.EmptyStmt)):
        p[0] = sa.EmbeddedStmtEmpty(p[1])
    elif (isinstance(p[1], sa.ExpStmt)):
        p[0] = sa.EmbeddedStmtExp(p[1])
    elif (isinstance(p[1], sa.SelectionStmt)):
        p[0] = sa.EmbeddedStmtSelection(p[1])
    elif (isinstance(p[1], sa.SelectionStmt)):
        p[0] = sa.EmbeddedStmtIteration(p[1])
    elif (isinstance(p[1], sa.JumpStmt)):
        p[0] = sa.EmbeddedStmtJump(p[1])

def p_block(p):
    '''block : LBRACE statement_list RBRACE
             | LBRACE RBRACE'''
    if (len(p) == 4):
        p[0] = sa.BlockStmtConcrete(p[2])
    else:
        p[0] = sa.BlockStmtConcrete(None)
        
def p_empty_stmt(p):
    '''empty_statement : SEMI'''        
    p[0] = sa.EmptyStmtConcrete()

def p_exp_statement(p):
    '''exp_statement : statement_exp SEMI'''
    if (isinstance(p[1], sa.InvocationExp)):
        p[0] = sa.ExpStmtInvocation(p[1])
    elif (isinstance(p[1], sa.ObjectCreationExp)):
        p[0] = sa.ExpStmtObjectCreation(p[1])
    elif (isinstance(p[1], sa.AssignExp)):
        p[0] = sa.ExpStmtAssignment(p[1])
    elif (isinstance(p[1], sa.PostIncrementExp)):
        p[0] = sa.ExpStmtPostIncrement(p[1])
    elif (isinstance(p[1], sa.PostDecrementExp)):
        p[0] = sa.ExpStmtPostDecrement(p[1])
    elif (isinstance(p[1], sa.PreIncrementExp)):
        p[0] = sa.ExpStmtPreIncrement(p[1])
    elif (isinstance(p[1], sa.PreDecrementExp)):
        p[0] = sa.ExpStmtPreDecrement(p[1])

def p_object_creation(p):
    '''object_creation_exp : NEW type LPAREN RPAREN
                           | NEW type LPAREN RPAREN object_initializer
                           | NEW type LPAREN arg_list RPAREN
                           | NEW type LPAREN arg_list RPAREN object_initializer'''
    if (isinstance(len(p) == 5)):
        p[0] = sa.NoArgsObjectCreation(p[2])
    elif (len(p) == 6):
        if (isinstance(p[5], sa.ObjectInitializer)):
            p[0] = sa.NoArgsWithInitializerObjectCreation(p[2], p[5])
        elif (isinstance(p[4], sa.ArgList)):
            p[0] = sa.ObjectCreation(p[2], p[4])
    elif (len(p) == 7):
        p[0] = sa.WithInitializerObjectCreation(p[2], p[4], p[6])

def p_object_initializer(p):
    '''object_initializer : LBRACE RBRACE
                          | LBRACE member_initializer_list RBRACE'''
    if (len(p) == 3):
        p[0] = sa.ObjectInitializerConcrete(None)
    else:
        p[0] = sa.ObjectInitializerConcrete(p[2])

def p_member_initializer_list(p):
    '''member_initializer_list : member_initializer
                               | member_initializer COMMA member_initializer_list'''
    if (len(p) == 2):
        p[0] = sa.SingleMemberInitializerList(p[1])
    else:
        p[0] = sa.CompoundMemberInitializerList(p[1], p[3])

def p_member_initializer(p):
    '''member_initializer : ID EQUAL exp'''
    p[0] = sa.MemberInitializerConcrete(p[1], p[3])

def p_post_increment_exp(p):
    '''post_increment_exp : primary_exp PLUSPLUS'''
    p[0] = sa.PostIncrementExpConcrete(p[1])

def p_post_decrement_exp(p):
    '''post_decrement_exp : primary_exp MINUSMINUS'''
    p[0] = sa.PostDecrementExpConcrete(p[1])

def p_pre_increment_exp(p):
    '''pre_increment_exp : PLUSPLUS unary_exp'''
    p[0] = sa.PreIncrementExpConcrete(p[2])

def p_pre_decrement_exp(p):
    '''pre_decrement_exp : MINUSMINUS unary_exp'''
    p[0] = sa.PreDecrementExpConcrete(p[2])

def p_selection_statement(p):
    '''selection_statement : if_statement
                           | switch_statement'''
    if (isinstance(p[1], sa.IfStmt)):
        p[0] = sa.SelectionStmtIf(p[1])
    else:
        p[0] = sa.SelectionStmtSwitch(p[1])






















def p_error(p):
    print("Syntax error in input!")

f = open("teste_parser.txt", "r")
parser = yacc.yacc()
result = parser.parse(input=f.read(), debug=True)

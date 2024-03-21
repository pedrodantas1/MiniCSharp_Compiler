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

def p_type(p):
    '''type : class_type
            | interface_type
            | value_type'''
    if (isinstance(p[1], sa.ClassType)):
        p[0] = sa.TypeClass(p[1])
    elif (isinstance(p[1], sa.InterfaceType)):
        p[0] = sa.TypeInterface(p[1])
    elif (isinstance(p[1], sa.ValueType)):
        p[0] = sa.TypeValue(p[1])

def p_class_type(p):
    '''class_type : type_name
                  | OBJECT
                  | STRING'''
    if (isinstance(p[1], sa.TypeName)):
        p[0] = sa.GenericClassType(p[1])
    elif(p[1] == 'object'):
        p[0] = sa.ObjectClassType(p[1])
    elif(p[1] == 'string'):
        p[0] = sa.StringClassType(p[1])

def p_interface_type(p):
    '''interface_type : type_name'''
    p[0] = sa.InterfaceType(p[1])

def p_value_type(p):
    '''value_type : integral_type
                  | floating_point_type
                  | BOOL'''
    if (isinstance(p[1], sa.IntegralType)):
        p[0] = sa.IntegralTypeRef(p[1])
    elif (isinstance(p[1], sa.FloatingPointType)):
        p[0] = sa.FloatingPointTypeRef(p[1])
    elif (p[1] == 'bool'):
        p[0] = sa.BoolType(p[1])

def p_integral_type_int(p):
    '''integral_type : INT'''
    p[0] = sa.IntType(p[1])

def p_integral_type_long(p):
    '''integral_type : LONG'''
    p[0] = sa.LongType(p[1])

def p_integral_type_char(p):
    '''integral_type : CHAR'''
    p[0] = sa.CharType(p[1])

def p_integral_type_float(p):
    '''floating_point_type : FLOAT'''
    p[0] = sa.FloatType(p[1])

def p_integral_type_double(p):
    '''floating_point_type : DOUBLE'''
    p[0] = sa.DoubleType(p[1])

def p_integral_type_decimal(p):
    '''floating_point_type : DECIMAL'''
    p[0] = sa.DecimalType(p[1])

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

def p_if_statement(p):
    '''if_statement : IF LPAREN exp RPAREN embedded_statement
                    | IF LPAREN exp RPAREN embedded_statement ELSE embedded_statement'''
    if (len(p) == 6):
        p[0] = sa.SimpleIfStmt(p[3], p[5])
    else:
        p[0] = sa.IfElseStmt(p[3], p[5], p[7])

def p_switch_statement(p):
    '''switch_statement : SWITCH LPAREN exp RPAREN LBRACE switch_body RBRACE'''
    p[0] = sa.SwitchStmtConcrete(p[3], p[6])

def p_switch_body(p):
    '''switch_body : switch_section
                   | switch_section switch_body'''
    if (len(p) == 2):
        p[0] = sa.SimpleSwitchBody(p[1])
    else:
        p[0] = sa.CompoundSwitchBody(p[1], p[2])

def p_switch_section_simple(p):
    '''switch_section : switch_label statement_list'''
    p[0] = sa.SimpleSwitchSection(p[1], p[2])

def p_switch_section_compound(p):
    '''switch_section : switch_label switch_section'''
    p[0] = sa.CompoundSwitchSection(p[1], p[2])

def p_switch_label(p):
    '''switch_label : CASE pattern COLON
                    | DEFAULT COLON'''
    if (len(p) == 4):
        p[0] = sa.SwitchLabelCase(p[2])
    else:
        p[0] = sa.SwitchLabelDefault()

def p_pattern(p):
    '''pattern : exp'''
    p[0] = sa.PatternConcrete(p[1])

def p_iteration_statement(p):
    '''iteration_statement : while_statement
                           | do_statement
                           | for_statement
                           | foreach_statement'''
    if (isinstance(p[1], sa.WhileStmt)):
        p[0] = sa.IterationStmtWhile(p[1])
    elif (isinstance(p[1], sa.DoStmt)):
        p[0] = sa.IterationStmtDo(p[1])
    elif (isinstance(p[1], sa.ForStmt)):
        p[0] = sa.IterationStmtFor(p[1])
    elif (isinstance(p[1], sa.ForeachStmt)):
        p[0] = sa.IterationStmtForeach(p[1])

def p_while_statement(p):
    '''while_statement : WHILE LPAREN exp RPAREN embedded_statement'''
    p[0] = sa.WhileStmtConcrete(p[3], p[5])

def p_do_statement(p):
    '''do_statement : DO embedded_statement WHILE LPAREN exp RPAREN SEMI'''
    p[0] = sa.DoStmtConcrete(p[2], p[5])

def p_for_statement_full(p):
    '''FOR LPAREN for_initializer SEMI for_condition SEMI for_iterator RPAREN embedded_statement'''
    p[0] = sa.ForStmtConcrete(p[2], p[4], p[6], p[8])

def p_for_statement_12(p):
    '''FOR LPAREN for_initializer SEMI for_condition SEMI RPAREN embedded_statement'''
    p[0] = sa.ForStmtConcrete(p[2], p[4], None, p[7])

def p_for_statement_13(p):
    '''FOR LPAREN for_initializer SEMI SEMI for_iterator RPAREN embedded_statement'''
    p[0] = sa.ForStmtConcrete(p[2], None, p[5], p[7])

def p_for_statement_1(p):
    '''FOR LPAREN for_initializer SEMI SEMI RPAREN embedded_statement'''
    p[0] = sa.ForStmtConcrete(p[2], None, None, p[6])

def p_for_statement_23(p):
    '''FOR LPAREN SEMI for_condition SEMI for_iterator RPAREN embedded_statement'''
    p[0] = sa.ForStmtConcrete(None, p[3], p[5], p[7])

def p_for_statement_2(p):
    '''FOR LPAREN SEMI for_condition SEMI RPAREN embedded_statement'''
    p[0] = sa.ForStmtConcrete(None, p[3], None, p[6])

def p_for_statement_3(p):
    '''FOR LPAREN SEMI SEMI for_iterator RPAREN embedded_statement'''
    p[0] = sa.ForStmtConcrete(None, None, p[4], p[6])

def p_for_statement_empty(p):
    '''FOR LPAREN SEMI SEMI RPAREN embedded_statement'''
    p[0] = sa.ForStmtConcrete(None, None, None, p[5])

def p_for_initializer(p):
    '''for_initializer : var_declaration
                       | var_declaration COMMA for_initializer'''
    if (len(p) == 2):
        p[0] = sa.SimpleForInitializer(p[1])
    else:
        p[0] = sa.CompoundForInitializer(p[1], p[3])

def p_for_condition(p):
    '''for_condition : exp'''
    p[0] = sa.ForConditionConcrete(p[1])

def p_for_iterator(p):
    '''for_iterator : statement_exp_list'''
    p[0] = sa.ForIteratorConcrete(p[1])

def p_statement_exp_list(p):
    '''statement_exp_list : statement_exp
                          | statement_exp COMMA statement_exp_list'''
    if (len(p) == 2):
        p[0] = sa.SimpleStmtExpList(p[1])
    else:
        p[0] = sa.CompoundStmtExpList(p[1], p[3])

def p_foreach_statement(p):
    '''foreach_statement : FOREACH LPAREN type ID IN exp RPAREN embedded_statement'''
    p[0] = sa.ForeachStmtConcrete(p[3], p[4], p[6], p[8])

def p_jump_statement(p):
    '''jump_statement : break_statement
                      | continue_statement
                      | return_statement'''
    if (isinstance(p[1], sa.BreakStmt)):
        p[0] = sa.JumpStmtBreak(p[1])
    elif (isinstance(p[1], sa.ContinueStmt)):
        p[0] = sa.JumpStmtContinue(p[1])
    elif (isinstance(p[1], sa.ReturnStmt)):
        p[0] = sa.JumpStmtReturn(p[1])

def p_break_statement(p):
    '''break_statement : BREAK SEMI'''
    p[0] = sa.BreakStmtConcrete()

def p_continue_statement(p):
    '''continue_statement : CONTINUE SEMI'''
    p[0] = sa.ContinueStmtConcrete()

def p_return_statement(p):
    '''return_statement : RETURN SEMI
                        | RETURN exp SEMI'''
    if (len(p) == 3):
        p[0] = sa.ReturnStmtConcrete(None)
    else:
        p[0] = sa.ReturnStmtConcrete(p[2])




    





















def p_error(p):
    print("Syntax error in input!")

f = open("teste_parser.txt", "r")
parser = yacc.yacc()
result = parser.parse(input=f.read(), debug=True)

import ply.yacc as yacc

import SintaxeAbstrata as sa
from lexer import *

# fmt: off

def p_program(p):
    '''program : class_declaration
               | class_declaration program'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_type(p):
    '''type : class_type
            | value_type'''
    if (isinstance(p[1], sa.ClassType)):
        p[0] = sa.TypeClass(p[1])
    elif (isinstance(p[1], sa.ValueType)):
        p[0] = sa.TypeValue(p[1])

def p_class_type(p):
    '''class_type : OBJECT
                  | STRING'''
    if(p[1] == 'object'):
        p[0] = sa.ObjectClassType(p[1])
    elif(p[1] == 'string'):
        p[0] = sa.StringClassType(p[1])

def p_value_type(p):
    '''value_type : integral_type
                  | floating_point_type
                  | BOOL
                  | VOID'''
    if (isinstance(p[1], sa.IntegralType)):
        p[0] = sa.IntegralTypeRef(p[1])
    elif (isinstance(p[1], sa.FloatingPointType)):
        p[0] = sa.FloatingPointTypeRef(p[1])
    elif (p[1] == 'bool'):
        p[0] = sa.BoolType(p[1])
    elif (p[1] == 'void'):
        p[0] = sa.VoidType(p[1])

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

# def p_func_declaration(p):
#     '''func_declaration : signature block'''
#     p[0] = sa.FuncDeclConcrete(p[1], p[2])
    
# def p_signature(p):
#     '''signature : type ID LPAREN param_list RPAREN
#                  | type ID LPAREN RPAREN'''
#     if (isinstance(p[4], sa.ParamList)):
#         p[0] = sa.SignatureConcrete(p[1], p[2], p[4])
#     else:
#         p[0] = sa.SignatureConcrete(p[1], p[2], None)

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
    '''declaration_statement : local_const_declaration SEMI
                             | local_var_declaration SEMI'''
    if (isinstance(p[1], sa.LocalConstDeclaration)):
        p[0] = sa.DeclarationStmtConst(p[1])
    elif (isinstance(p[1], sa.LocalVarDeclaration)):
        p[0] = sa.DeclarationStmtVar(p[1])

def p_local_const_declaration(p):
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

def p_local_var_declaration(p):
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
    if (len(p) == 2):
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
    elif (isinstance(p[1], sa.IterationStmt)):
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
    p[0] = sa.ExpStmtConcrete(p[1])

def p_statement_exp(p):
    '''statement_exp : invocation_exp
                     | object_creation_exp
                     | assignment
                     | post_increment_exp
                     | post_decrement_exp
                     | pre_increment_exp
                     | pre_decrement_exp'''
    if (isinstance(p[1], sa.InvocationExp)):
        p[0] = sa.StmtExpInvocation(p[1])
    elif (isinstance(p[1], sa.ObjectCreationExp)):
        p[0] = sa.StmtExpObjectCreation(p[1])
    elif (isinstance(p[1], sa.AssignExp)):
        p[0] = sa.StmtExpAssignment(p[1])
    elif (isinstance(p[1], sa.PostIncrementExp)):
        p[0] = sa.StmtExpPostIncrement(p[1])
    elif (isinstance(p[1], sa.PostDecrementExp)):
        p[0] = sa.StmtExpPostDecrement(p[1])
    elif (isinstance(p[1], sa.PreIncrementExp)):
        p[0] = sa.StmtExpPreIncrement(p[1])
    elif (isinstance(p[1], sa.PreDecrementExp)):
        p[0] = sa.StmtExpPreDecrement(p[1])

def p_object_creation(p):
    '''object_creation_exp : NEW type LPAREN RPAREN
                           | NEW type LPAREN RPAREN object_initializer
                           | NEW type LPAREN arg_list RPAREN
                           | NEW type LPAREN arg_list RPAREN object_initializer'''
    if (len(p) == 5):
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
    '''if_statement : IF LPAREN exp RPAREN block
                    | IF LPAREN exp RPAREN block ELSE block'''
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
    '''pattern : relational_pattern
               | constant_pattern'''
    if (isinstance(p[1], sa.RelationalPattern)):
        p[0] = sa.PatternRelational(p[1])
    elif (isinstance(p[1], sa.ConstantPattern)):
        p[0] = sa.PatternConstant(p[1])

def p_relational_pattern(p):
    '''relational_pattern : relational_operator constant_exp'''
    p[0] = sa.RelationalPatternConcrete(p[1], p[2])

def p_relational_operator(p):
    '''relational_operator : LT
                           | GT
                           | LEQ
                           | GEQ'''
    p[0] = sa.RelationalOperatorConcrete(p[1])

def p_constant_exp(p):
    '''constant_exp : INTNUM
                    | FLOATNUM
                    | CHARLITERAL'''
    p[0] = sa.ConstantExpConcrete(p[1])

def p_constant_pattern(p):
    '''constant_pattern : INTNUM
                        | FLOATNUM
                        | CHARLITERAL
                        | STRINGLITERAL
                        | TRUE
                        | FALSE
                        | NULL'''
    p[0] = sa.ConstantPatternConcrete(p[1])

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
    '''while_statement : WHILE LPAREN exp RPAREN block'''
    p[0] = sa.WhileStmtConcrete(p[3], p[5])

def p_do_statement(p):
    '''do_statement : DO block WHILE LPAREN exp RPAREN SEMI'''
    p[0] = sa.DoStmtConcrete(p[2], p[5])

def p_for_statement_full(p):
    '''for_statement : FOR LPAREN for_initializer SEMI for_condition SEMI for_iterator RPAREN block'''
    p[0] = sa.ForStmtConcrete(p[3], p[5], p[7], p[9])

def p_for_statement_12(p):
    '''for_statement : FOR LPAREN for_initializer SEMI for_condition SEMI RPAREN block'''
    p[0] = sa.ForStmtConcrete(p[3], p[5], None, p[8])

def p_for_statement_13(p):
    '''for_statement : FOR LPAREN for_initializer SEMI SEMI for_iterator RPAREN block'''
    p[0] = sa.ForStmtConcrete(p[3], None, p[6], p[8])

def p_for_statement_1(p):
    '''for_statement : FOR LPAREN for_initializer SEMI SEMI RPAREN block'''
    p[0] = sa.ForStmtConcrete(p[3], None, None, p[7])

def p_for_statement_23(p):
    '''for_statement : FOR LPAREN SEMI for_condition SEMI for_iterator RPAREN block'''
    p[0] = sa.ForStmtConcrete(None, p[4], p[6], p[8])

def p_for_statement_2(p):
    '''for_statement : FOR LPAREN SEMI for_condition SEMI RPAREN block'''
    p[0] = sa.ForStmtConcrete(None, p[4], None, p[7])

def p_for_statement_3(p):
    '''for_statement : FOR LPAREN SEMI SEMI for_iterator RPAREN block'''
    p[0] = sa.ForStmtConcrete(None, None, p[5], p[7])

def p_for_statement_empty(p):
    '''for_statement : FOR LPAREN SEMI SEMI RPAREN block'''
    p[0] = sa.ForStmtConcrete(None, None, None, p[6])

def p_for_initializer(p):
    '''for_initializer : local_var_declaration'''
    p[0] = sa.SimpleForInitializer(p[1])

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
    '''foreach_statement : FOREACH LPAREN type ID IN exp RPAREN block'''
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

def p_arg_list(p):
    '''arg_list : exp
                | exp COMMA arg_list'''
    if (len(p) == 2):
        p[0] = sa.SimpleArgList(p[1])
    else:
        p[0] = sa.CompoundArgList(p[1], p[3])

def p_primary_exp(p):
    '''primary_exp : primary_no_array_creation_exp'''
    p[0] = sa.PrimaryExpNoArrayCreation(p[1])

def p_boolean_exp(p):
    '''primary_no_array_creation_exp : TRUE
                                     | FALSE'''
    p[0] = sa.BooleanExp(p[1])

def p_null_exp(p):
    '''primary_no_array_creation_exp : NULL'''
    p[0] = sa.NullExp(p[1])

def p_intnum_exp(p):
    '''primary_no_array_creation_exp : INTNUM'''
    p[0] = sa.IntNumExp(p[1])

def p_hexnum_exp(p):
    '''primary_no_array_creation_exp : HEXADECIMALNUM'''
    p[0] = sa.HexNumExp(p[1])

def p_binnum_exp(p):
    '''primary_no_array_creation_exp : BINARYNUM'''
    p[0] = sa.BinNumExp(p[1])

def p_floatnum_exp(p):
    '''primary_no_array_creation_exp : FLOATNUM'''
    p[0] = sa.FloatNumExp(p[1])

def p_doublenum_exp(p):
    '''primary_no_array_creation_exp : DOUBLENUM'''
    p[0] = sa.DoubleNumExp(p[1])

def p_decimalnum_exp(p):
    '''primary_no_array_creation_exp : DECIMALNUM'''
    p[0] = sa.DecimalNumExp(p[1])

def p_charliteral_exp(p):
    '''primary_no_array_creation_exp : CHARLITERAL'''
    p[0] = sa.CharExp(p[1])

def p_stringliteral_exp(p):
    '''primary_no_array_creation_exp : STRINGLITERAL'''
    p[0] = sa.StringExp(p[1])

def p_id_exp(p):
    '''primary_no_array_creation_exp : ID'''
    p[0] = sa.IdExp(p[1])

def p_primary_parenthesized_exp(p):
    '''primary_no_array_creation_exp : parenthesized_exp'''
    p[0] = sa.PrimaryParenthesizedExp(p[1])

def p_parenthesized_exp(p):
    '''parenthesized_exp : LPAREN exp RPAREN'''
    p[0] = sa.ParenthesizedExpConcrete(p[2])

def p_primary_member_access_exp(p):
    '''primary_no_array_creation_exp : member_access'''
    p[0] = sa.PrimaryMemberAccessExp(p[1])

def p_member_access_exp(p):
    '''member_access : primary_exp DOT ID'''
    p[0] = sa.MemberAccessExpConcrete(p[1], p[3])

def p_primary_invocation_exp(p):
    '''primary_no_array_creation_exp : invocation_exp'''
    p[0] = sa.PrimaryInvocationExp(p[1])

def p_invocation_exp(p):
    '''invocation_exp : primary_exp LPAREN RPAREN
                      | primary_exp LPAREN arg_list RPAREN'''
    if (len(p) == 4):
        p[0] = sa.InvocationExpConcrete(p[1], None)
    else:
        p[0] = sa.InvocationExpConcrete(p[1], p[3])

def p_primary_element_access_exp(p):
    '''primary_no_array_creation_exp : element_access'''
    p[0] = sa.PrimaryElementAccessExp(p[1])

def p_element_access_exp(p):
    '''element_access : primary_no_array_creation_exp LSB exp RSB'''
    p[0] = sa.ElementAccessExpConcrete(p[1], p[3])

def p_this_exp(p):
    '''primary_no_array_creation_exp : THIS'''
    p[0] = sa.ThisExp(p[1])

# @
def p_primary_post_increment_exp(p):
    '''primary_no_array_creation_exp : post_increment_exp'''
    p[0] = sa.PrimaryPostIncrementExp(p[1])

# @
def p_primary_post_decrement_exp(p):
    '''primary_no_array_creation_exp : post_decrement_exp'''
    p[0] = sa.PrimaryPostDecrementExp(p[1])

# @
def p_primary_object_creation_exp(p):
    '''primary_no_array_creation_exp : object_creation_exp'''
    p[0] = sa.PrimaryObjectCreationExp(p[1])

# def p_exp_list(p):
#     '''exp_list : exp
#                 | exp_list COMMA exp'''
#     if (len(p) == 2):
#         p[0] = sa.SingleExpList(p[1])
#     else:
#         p[0] = sa.CompoundExpList(p[1], p[3])

def p_unary_primary_exp(p):
    '''unary_exp : primary_exp'''
    p[0] = sa.UnaryPrimaryExp(p[1])

def p_unary_pre_increment_exp(p):
    '''unary_exp : pre_increment_exp'''
    p[0] = sa.UnaryPreIncrementExp(p[1])

def p_unary_pre_decrement_exp(p):
    '''unary_exp : pre_decrement_exp'''
    p[0] = sa.UnaryPreDecrementExp(p[1])
    
def p_unary_cast_exp(p):
    '''unary_exp : cast_exp'''
    p[0] = sa.UnaryCastExp(p[1])

def p_cast_exp(p):
    '''cast_exp : LPAREN type RPAREN unary_exp'''
    p[0] = sa.CastExpConcrete(p[2], p[4])

def p_unary_minus_exp(p):
    '''unary_exp : minus_exp'''
    p[0] = sa.UnaryMinusExp(p[1])

def p_minus_exp(p):
    '''minus_exp : MINUS unary_exp'''
    p[0] = sa.MinusExpConcrete(p[2])

def p_unary_plus_exp(p):
    '''unary_exp : plus_exp'''
    p[0] = sa.UnaryPlusExp(p[1])

def p_plus_exp(p):
    '''plus_exp : PLUS unary_exp'''
    p[0] = sa.PlusExpConcrete(p[2])

def p_exp_non_assignment_exp(p):
    '''exp : non_assignment_exp'''
    p[0] = sa.ExpNonAssignment(p[1])

def p_exp_assignment_exp(p):
    '''exp : assignment'''
    p[0] = sa.ExpAssignment(p[1])

def p_non_assignment_conditional_exp(p):
    '''non_assignment_exp : conditional_exp'''
    p[0] = sa.NonAssignmentConditionalExp(p[1])

def p_conditional_exp(p):
    '''conditional_exp : conditional_or_exp HOOK exp COLON exp
                       | conditional_or_exp'''
    if (len(p) == 2):
        p[0] = sa.ConditionalExpNext(p[1])
    else:
        p[0] = sa.TernaryExp(p[1], p[3], p[5])

def p_conditional_or_exp(p):
    '''conditional_or_exp : conditional_or_exp PIPEPIPE conditional_and_exp
                          | conditional_and_exp'''
    if (len(p) == 2):
        p[0] = sa.ConditionalOrExpNext(p[1])
    else:
        p[0] = sa.ConditionalOrExpConcrete(p[1], p[3])

def p_conditional_and_exp(p):
    '''conditional_and_exp : conditional_and_exp AMPERAMPER inclusive_or_exp
                           | inclusive_or_exp'''
    if (len(p) == 2):
        p[0] = sa.ConditionalAndExpNext(p[1])
    else:
        p[0] = sa.ConditionalAndExpConcrete(p[1], p[3])

def p_inclusive_or_exp(p):
    '''inclusive_or_exp : inclusive_or_exp PIPE exclusive_or_exp
                        | exclusive_or_exp'''
    if (len(p) == 2):
        p[0] = sa.InclusiveOrExpNext(p[1])
    else:
        p[0] = sa.InclusiveOrExpConcrete(p[1], p[3])

def p_exclusive_or_exp(p):
    '''exclusive_or_exp : exclusive_or_exp CIRCUMFLEX and_exp
                        | and_exp'''
    if (len(p) == 2):
        p[0] = sa.ExclusiveOrExpNext(p[1])
    else:
        p[0] = sa.ExclusiveOrExpConcrete(p[1], p[3])

def p_and_exp(p):
    '''and_exp : and_exp AMPER equality_exp
               | equality_exp'''
    if (len(p) == 2):
        p[0] = sa.AndExpNext(p[1])
    else:
        p[0] = sa.AndExpConcrete(p[1], p[3])

def p_equality_exp(p):
    '''equality_exp : equality_exp EQEQUAL relational_exp
                    | equality_exp NOTEQUAL relational_exp
                    | relational_exp'''
    if (len(p) == 2):
        p[0] = sa.EqualityExpNext(p[1])
    elif (p[2] == '=='):
        p[0] = sa.EqualExp(p[1], p[3])
    elif (p[2] == '!='):
        p[0] = sa.NotEqualExp(p[1], p[3])

def p_relational_exp(p):
    '''relational_exp : relational_exp LT shift_exp
                      | relational_exp GT shift_exp
                      | relational_exp LEQ shift_exp
                      | relational_exp GEQ shift_exp
                      | relational_exp IS type
                      | shift_exp'''
    if (len(p) == 2):
        p[0] = sa.RelationalExpNext(p[1])
    elif (p[2] == '<'):
        p[0] = sa.LessExp(p[1], p[3])
    elif (p[2] == '>'):
        p[0] = sa.GreaterExp(p[1], p[3])
    elif (p[2] == '<='):
        p[0] = sa.LessEqualExp(p[1], p[3])
    elif (p[2] == '>='):
        p[0] = sa.GreaterEqualExp(p[1], p[3])
    elif (p[2] == 'is'):
        p[0] = sa.IsTypeExp(p[1], p[3])

def p_shift_exp(p):
    '''shift_exp : shift_exp LSHIFT additive_exp
                 | shift_exp RSHIFT additive_exp
                 | additive_exp'''
    if (len(p) == 2):
        p[0] = sa.ShiftExpNext(p[1])
    elif (p[2] == '<<'):
        p[0] = sa.LeftShiftExp(p[1], p[3])
    elif (p[2] == '>>'):
        p[0] = sa.RightShiftExp(p[1], p[3])

def p_additive_exp(p):
    '''additive_exp : additive_exp PLUS multiplicative_exp
                    | additive_exp MINUS multiplicative_exp
                    | multiplicative_exp'''
    if (len(p) == 2):
        p[0] = sa.AdditiveExpNext(p[1])
    elif (p[2] == '+'):
        p[0] = sa.SumExp(p[1], p[3])
    elif (p[2] == '-'):
        p[0] = sa.SubExp(p[1], p[3])

def p_multiplicative_exp(p):
    '''multiplicative_exp : multiplicative_exp STAR unary_exp
                          | multiplicative_exp SLASH unary_exp
                          | multiplicative_exp PERCENT unary_exp
                          | unary_exp'''
    if (len(p) == 2):
        p[0] = sa.MultiplicativeExpNext(p[1])
    elif (p[2] == '*'):
        p[0] = sa.MultExp(p[1], p[3])
    elif (p[2] == '/'):
        p[0] = sa.DivExp(p[1], p[3])
    elif (p[2] == '%'):
        p[0] = sa.ModExp(p[1], p[3])

def p_assignment_simple(p):
    '''assignment : unary_exp EQUAL exp'''
    p[0] = sa.AssignExp(p[1], p[3])

def p_class_declaration(p):
    '''class_declaration : class_modifier CLASS ID class_body |
                         | CLASS ID class_body'''
    if (len(p) == 5):
        p[0] = sa.ClassDeclWithMod(p[1], p[3], p[4])
    else:
        p[0] = sa.ClassDeclSimple(p[2], p[3])
        


def p_error(p):
    print("Syntax error in input!")

f = open("teste_parser.cs", "r")
lexer = lex.lex()
lexer.input(f.read())
parser = yacc.yacc()
result = parser.parse(debug=True)

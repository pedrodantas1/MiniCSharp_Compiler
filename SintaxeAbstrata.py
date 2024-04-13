from abc import ABC, abstractmethod


# Herdado por mais de uma classe (talvez mudar)
class NoArrayCreationExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class UnaryExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Type(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class TypeClass(Type):
    def __init__(self, class_type):
        self.class_type = class_type

    def accept(self, visitor):
        return visitor.visitTypeClass(self)


class TypeValue(Type):
    def __init__(self, value_type):
        self.value_type = value_type

    def accept(self, visitor):
        return visitor.visitTypeValue(self)


class ClassType(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ObjectClassType(ClassType):
    def __init__(self, type_object):
        self.type_object = type_object

    def accept(self, visitor):
        return visitor.visitObjectClassType(self)


class StringClassType(ClassType):
    def __init__(self, type_string):
        self.type_string = type_string

    def accept(self, visitor):
        return visitor.visitStringClassType(self)


class ValueType(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class IntegralTypeRef(ValueType):
    def __init__(self, integral_type):
        self.integral_type = integral_type

    def accept(self, visitor):
        return visitor.visitIntegralTypeRef(self)


class FloatingPointTypeRef(ValueType):
    def __init__(self, floating_point_type):
        self.floating_point_type = floating_point_type

    def accept(self, visitor):
        return visitor.visitFloatingPointTypeRef(self)


class BoolType(ValueType):
    def __init__(self, bool_type):
        self.bool_type = bool_type

    def accept(self, visitor):
        return visitor.visitBoolType(self)


class VoidType(ValueType):
    def __init__(self, void_type):
        self.void_type = void_type

    def accept(self, visitor):
        return visitor.visitVoidType(self)


class IntegralType(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class IntType(IntegralType):
    def __init__(self, int_type):
        self.int_type = int_type

    def accept(self, visitor):
        return visitor.visitIntType(self)


class LongType(IntegralType):
    def __init__(self, long_type):
        self.long_type = long_type

    def accept(self, visitor):
        return visitor.visitLongType(self)


class CharType(IntegralType):
    def __init__(self, char_type):
        self.char_type = char_type

    def accept(self, visitor):
        return visitor.visitCharType(self)


class FloatingPointType(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class FloatType(FloatingPointType):
    def __init__(self, float_type):
        self.float_type = float_type

    def accept(self, visitor):
        return visitor.visitFloatType(self)


class DoubleType(FloatingPointType):
    def __init__(self, double_type):
        self.double_type = double_type

    def accept(self, visitor):
        return visitor.visitDoubleType(self)


class DecimalType(FloatingPointType):
    def __init__(self, decimal_type):
        self.decimal_type = decimal_type

    def accept(self, visitor):
        return visitor.visitDecimalType(self)


# class FuncDecl(ABC):
#     @abstractmethod
#     def accept(self, visitor):
#         pass


# class FuncDeclConcrete(FuncDecl):
#     def __init__(self, signature, block):
#         self.signature = signature
#         self.block = block

#     def accept(self, visitor):
#         return visitor.visitFuncDeclConcrete(self)


# class Signature(ABC):
#     @abstractmethod
#     def accept(self, visitor):
#         pass


# class SignatureConcrete(Signature):
#     def __init__(self, type, id, param_list):
#         self.type = type
#         self.id = id
#         self.param_list = param_list  # Pode ser None

#     def accept(self, visitor):
#         return visitor.visitSignatureConcrete(self)


class ParamList(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SingleParamList(ParamList):
    def __init__(self, type, id):
        self.type = type
        self.id = id

    def accept(self, visitor):
        visitor.visitSingleParamList(self)


class CompoundParamList(ParamList):
    def __init__(self, type, id, param_list):
        self.type = type
        self.id = id
        self.param_list = param_list

    def accept(self, visitor):
        visitor.visitCompoundParamList(self)


class StatementList(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SingleStatementList(StatementList):
    def __init__(self, stmt):
        self.stmt = stmt

    def accept(self, visitor):
        visitor.visitSingleStatementList(self)


class CompoundStatementList(StatementList):
    def __init__(self, stmt, stmt_list):
        self.stmt = stmt
        self.stmt_list = stmt_list

    def accept(self, visitor):
        visitor.visitCompoundStatementList(self)


# Comandos
class Statement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class StatementDeclaration(Statement):
    def __init__(self, declaration_stmt):
        self.declaration_stmt = declaration_stmt

    def accept(self, visitor):
        visitor.visitStatementDeclaration(self)


class StatementEmbedded(Statement):
    def __init__(self, embedded_stmt):
        self.embedded_stmt = embedded_stmt

    def accept(self, visitor):
        visitor.visitStatementEmbedded(self)


# Comandos de declaracao (constante e variavel)
class DeclarationStatement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class DeclarationStmtConst(DeclarationStatement):
    def __init__(self, const_declaration):
        self.const_declaration = const_declaration

    def accept(self, visitor):
        visitor.visitDeclarationStmtConst(self)


class DeclarationStmtVar(DeclarationStatement):
    def __init__(self, var_declaration):
        self.var_declaration = var_declaration

    def accept(self, visitor):
        visitor.visitDeclarationStmtVar(self)


class LocalConstDeclaration(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class LocalConstDeclarationConcrete(LocalConstDeclaration):
    def __init__(self, type, const_declarators):
        self.type = type
        self.const_declarators = const_declarators

    def accept(self, visitor):
        visitor.visitLocalConstDeclarationConcrete(self)


class ConstDeclarators(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SingleConstDeclarators(ConstDeclarators):
    def __init__(self, const_declarator):
        self.const_declarator = const_declarator

    def accept(self, visitor):
        visitor.visitSingleConstDeclarators(self)


class CompoundConstDeclarators(ConstDeclarators):
    def __init__(self, const_declarator, const_declarators):
        self.const_declarator = const_declarator
        self.const_declarators = const_declarators

    def accept(self, visitor):
        visitor.visitCompoundConstDeclarators(self)


class ConstDeclarator(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConstDeclaratorConcrete(ConstDeclarator):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        visitor.visitConstDeclaratorConcrete(self)


class LocalVarDeclaration(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class LocalVarDeclarationConcrete(LocalVarDeclaration):
    def __init__(self, type, var_declarators):
        self.type = type
        self.var_declarators = var_declarators

    def accept(self, visitor):
        visitor.visitLocalVarDeclarationConcrete(self)


class VarDeclarators(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SingleVarDeclarators(VarDeclarators):
    def __init__(self, var_declarator):
        self.var_declarator = var_declarator

    def accept(self, visitor):
        visitor.visitSingleVarDeclarators(self)


class CompoundVarDeclarators(VarDeclarators):
    def __init__(self, var_declarator, var_declarators):
        self.var_declarator = var_declarator
        self.var_declarators = var_declarators

    def accept(self, visitor):
        visitor.visitCompoundVarDeclarators(self)


class VarDeclarator(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class VarDeclaratorId(VarDeclarator):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.visitVarDeclaratorId(self)


class VarDeclaratorIdExp(VarDeclarator):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        visitor.visitVarDeclaratorIdExp(self)


# class VarDeclaratorIdArray(VarDeclarator):
#     def __init__(self, id, array_initializer):
#         self.id = id
#         self.array_initializer = array_initializer

#     def accept(self, visitor):
#         visitor.visitVarDeclaratorIdArray(self)


# Comandos integrados
# (comandos exp, if, switch, while, do while, for, foreach,
# break, continue, return)
class EmbeddedStatement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class EmbeddedStmtBlock(EmbeddedStatement):
    def __init__(self, block):
        self.block = block

    def accept(self, visitor):
        visitor.visitEmbeddedStmtBlock(self)


class EmbeddedStmtEmpty(EmbeddedStatement):
    def __init__(self, empty_statement):
        self.empty_statement = empty_statement

    def accept(self, visitor):
        visitor.visitEmbeddedStmtEmpty(self)


class EmbeddedStmtExp(EmbeddedStatement):
    def __init__(self, exp_statement):
        self.exp_statement = exp_statement

    def accept(self, visitor):
        visitor.visitEmbeddedStmtExp(self)


class EmbeddedStmtSelection(EmbeddedStatement):
    def __init__(self, selection_statement):
        self.selection_statement = selection_statement

    def accept(self, visitor):
        visitor.visitEmbeddedStmtSelection(self)


class EmbeddedStmtIteration(EmbeddedStatement):
    def __init__(self, iteration_statement):
        self.iteration_statement = iteration_statement

    def accept(self, visitor):
        visitor.visitEmbeddedStmtIteration(self)


class EmbeddedStmtJump(EmbeddedStatement):
    def __init__(self, jump_statement):
        self.jump_statement = jump_statement

    def accept(self, visitor):
        visitor.visitEmbeddedStmtJump(self)


# Bloco de comando
class BlockStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class BlockStmtConcrete(BlockStmt):
    def __init__(self, stmt_list):
        self.stmt_list = stmt_list  # Pode ser None

    def accept(self, visitor):
        visitor.visitBlockStmtConcrete(self)


# Comando vazio
class EmptyStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class EmptyStmtConcrete(EmptyStmt):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitEmptyStmtConcrete(self)


class ExpStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ExpStmtConcrete(ExpStmt):
    def __init__(self, statement_exp):
        self.statement_exp = statement_exp

    def accept(self, visitor):
        visitor.visitExpStmtConcrete(self)


class StmtExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class StmtExpInvocation(StmtExp):
    def __init__(self, invocation_exp):
        self.invocation_exp = invocation_exp

    def accept(self, visitor):
        visitor.visitStmtExpInvocation(self)


class StmtExpObjectCreation(StmtExp):
    def __init__(self, object_creation_exp):
        self.object_creation_exp = object_creation_exp

    def accept(self, visitor):
        visitor.visitStmtExpObjectCreation(self)


class StmtExpAssignment(StmtExp):
    def __init__(self, assignment):
        self.assignment = assignment

    def accept(self, visitor):
        visitor.visitStmtExpAssignment(self)


class StmtExpPostIncrement(StmtExp):
    def __init__(self, post_increment_exp):
        self.post_increment_exp = post_increment_exp

    def accept(self, visitor):
        visitor.visitStmtExpPostIncrement(self)


class StmtExpPostDecrement(StmtExp):
    def __init__(self, post_decrement_exp):
        self.post_decrement_exp = post_decrement_exp

    def accept(self, visitor):
        visitor.visitStmtExpPostDecrement(self)


class StmtExpPreIncrement(StmtExp):
    def __init__(self, pre_increment_exp):
        self.pre_increment_exp = pre_increment_exp

    def accept(self, visitor):
        visitor.visitStmtExpPreIncrement(self)


class StmtExpPreDecrement(StmtExp):
    def __init__(self, pre_decrement_exp):
        self.pre_decrement_exp = pre_decrement_exp

    def accept(self, visitor):
        visitor.visitStmtExpPreDecrement(self)


# Comando para criacao de objetos
class ObjectCreationExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class NoArgsObjectCreation(ObjectCreationExp):
    def __init__(self, type):
        self.type = type

    def accept(self, visitor):
        visitor.visitNoArgsObjectCreation(self)


class NoArgsWithInitializerObjectCreation(ObjectCreationExp):
    def __init__(self, type, object_initializer):
        self.type = type
        self.object_initializer = object_initializer

    def accept(self, visitor):
        visitor.visitNoArgsWithInitializerObjectCreation(self)


class ObjectCreation(ObjectCreationExp):
    def __init__(self, type, arg_list):
        self.type = type
        self.arg_list = arg_list

    def accept(self, visitor):
        visitor.visitObjectCreation(self)


class WithInitializerObjectCreation(ObjectCreationExp):
    def __init__(self, type, arg_list, object_initializer):
        self.type = type
        self.arg_list = arg_list
        self.object_initializer = object_initializer

    def accept(self, visitor):
        visitor.visitWithInitializerObjectCreation(self)


class ObjectInitializer(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ObjectInitializerConcrete(ObjectInitializer):
    def __init__(self, member_initializer_list):
        self.member_initializer_list = member_initializer_list

    def accept(self, visitor):
        visitor.visitObjectInitializerConcrete(self)


class MemberInitializerList(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SingleMemberInitializerList(MemberInitializerList):
    def __init__(self, member_initializer):
        self.member_initializer = member_initializer

    def accept(self, visitor):
        visitor.visitSingleMemberInitializerList(self)


class CompoundMemberInitializerList(MemberInitializerList):
    def __init__(self, member_initializer, member_initializer_list):
        self.member_initializer = member_initializer
        self.member_initializer_list = member_initializer_list

    def accept(self, visitor):
        visitor.visitCompoundMemberInitializerList(self)


class MemberInitializer(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class MemberInitializerConcrete(MemberInitializer):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        visitor.visitMemberInitializerConcrete(self)


class PostIncrementExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class PostIncrementExpConcrete(PostIncrementExp):
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp

    def accept(self, visitor):
        visitor.visitPostIncrementExpConcrete(self)


class PostDecrementExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class PostDecrementExpConcrete(PostDecrementExp):
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp

    def accept(self, visitor):
        visitor.visitPostDecrementExpConcrete(self)


class PreIncrementExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class PreIncrementExpConcrete(PreIncrementExp):
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp

    def accept(self, visitor):
        visitor.visitPreIncrementExpConcrete(self)


class PreDecrementExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class PreDecrementExpConcrete(PreDecrementExp):
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp

    def accept(self, visitor):
        visitor.visitPreDecrementExpConcrete(self)


class SelectionStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SelectionStmtIf(SelectionStmt):
    def __init__(self, if_statement):
        self.if_statement = if_statement

    def accept(self, visitor):
        visitor.visitSelectionStmtIf(self)


class SelectionStmtSwitch(SelectionStmt):
    def __init__(self, switch_statement):
        self.switch_statement = switch_statement

    def accept(self, visitor):
        visitor.visitSelectionStmtSwitch(self)


class IfStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SimpleIfStmt(IfStmt):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block

    def accept(self, visitor):
        visitor.visitSimpleIfStmt(self)


class IfElseStmt(IfStmt):
    def __init__(self, exp, block1, block2):
        self.exp = exp
        self.block1 = block1
        self.block2 = block2

    def accept(self, visitor):
        visitor.visitIfElseStmt(self)


class SwitchStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SwitchStmtConcrete(SwitchStmt):
    def __init__(self, exp, switch_body):
        self.exp = exp
        self.switch_body = switch_body

    def accept(self, visitor):
        visitor.visitSwitchStmtConcrete(self)


class SwitchBody(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SimpleSwitchBody(SwitchBody):
    def __init__(self, switch_section):
        self.switch_section = switch_section

    def accept(self, visitor):
        visitor.visitSimpleSwitchBody(self)


class CompoundSwitchBody(SwitchBody):
    def __init__(self, switch_section, switch_body):
        self.switch_section = switch_section
        self.switch_body = switch_body

    def accept(self, visitor):
        visitor.visitCompoundSwitchBody(self)


class SwitchSection(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SimpleSwitchSection(SwitchSection):
    def __init__(self, switch_label, stmt_list):
        self.switch_label = switch_label
        self.stmt_list = stmt_list

    def accept(self, visitor):
        visitor.visitSimpleSwitchSection(self)


class CompoundSwitchSection(SwitchSection):
    def __init__(self, switch_label, switch_section):
        self.switch_label = switch_label
        self.switch_section = switch_section

    def accept(self, visitor):
        visitor.visitCompoundSwitchSection(self)


class SwitchLabel(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SwitchLabelCase(SwitchLabel):
    def __init__(self, pattern):
        self.pattern = pattern

    def accept(self, visitor):
        visitor.visitSwitchLabelCase(self)


class SwitchLabelDefault(SwitchLabel):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitSwitchLabelDefault(self)


class Pattern(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class PatternRelational(Pattern):
    def __init__(self, relational_pattern):
        self.relational_pattern = relational_pattern

    def accept(self, visitor):
        visitor.visitPatternRelational(self)


class PatternConstant(Pattern):
    def __init__(self, constant_pattern):
        self.constant_pattern = constant_pattern

    def accept(self, visitor):
        visitor.visitPatternConstant(self)


class RelationalPattern(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class RelationalPatternConcrete(RelationalPattern):
    def __init__(self, relational_operator, constant_exp):
        self.relational_operator = relational_operator
        self.constant_exp = constant_exp

    def accept(self, visitor):
        visitor.visitRelationalPatternConcrete(self)


class RelationalOperator(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class RelationalOperatorConcrete(RelationalOperator):
    def __init__(self, operator):
        self.operator = operator

    def accept(self, visitor):
        visitor.visitRelationalOperatorConcrete(self)


class ConstantExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConstantExpConcrete(ConstantExp):
    def __init__(self, constant_exp):
        self.constant_exp = constant_exp

    def accept(self, visitor):
        visitor.visitConstantExpConcrete(self)


class ConstantPattern(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConstantPatternConcrete(ConstantPattern):
    def __init__(self, constant_exp):
        self.constant_exp = constant_exp

    def accept(self, visitor):
        visitor.visitConstantPatternConcrete(self)


class IterationStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class IterationStmtWhile(IterationStmt):
    def __init__(self, while_statement):
        self.while_statement = while_statement

    def accept(self, visitor):
        visitor.visitIterationStmtWhile(self)


class IterationStmtDo(IterationStmt):
    def __init__(self, do_statement):
        self.do_statement = do_statement

    def accept(self, visitor):
        visitor.visitIterationStmtDo(self)


class IterationStmtFor(IterationStmt):
    def __init__(self, for_statement):
        self.for_statement = for_statement

    def accept(self, visitor):
        visitor.visitIterationStmtFor(self)


class IterationStmtForeach(IterationStmt):
    def __init__(self, foreach_statement):
        self.foreach_statement = foreach_statement

    def accept(self, visitor):
        visitor.visitIterationStmtForeach(self)


class WhileStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class WhileStmtConcrete(WhileStmt):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block

    def accept(self, visitor):
        visitor.visitWhileStmtConcrete(self)


class DoStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class DoStmtConcrete(DoStmt):
    def __init__(self, block, exp):
        self.block = block
        self.exp = exp

    def accept(self, visitor):
        visitor.visitDoStmtConcrete(self)


class ForStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ForStmtConcrete(ForStmt):
    def __init__(self, for_initializer, for_condition, for_iterator, block):
        self.for_initializer = for_initializer  # Pode ser None
        self.for_condition = for_condition  # Pode ser None
        self.for_iterator = for_iterator  # Pode ser None
        self.block = block

    def accept(self, visitor):
        visitor.visitForStmtConcrete(self)


class ForInitializer(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SimpleForInitializer(ForInitializer):
    def __init__(self, local_var_declaration):
        self.local_var_declaration = local_var_declaration

    def accept(self, visitor):
        visitor.visitSimpleForInitializer(self)


class ForCondition(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ForConditionConcrete(ForCondition):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        visitor.visitForConditionConcrete(self)


class ForIterator(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ForIteratorConcrete(ForIterator):
    def __init__(self, stmt_exp_list):
        self.stmt_exp_list = stmt_exp_list

    def accept(self, visitor):
        visitor.visitForIteratorConcrete(self)


class StmtExpList(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SimpleStmtExpList(StmtExpList):
    def __init__(self, exp_stmt):
        self.exp_stmt = exp_stmt

    def accept(self, visitor):
        visitor.visitSimpleStmtExpList(self)


class CompoundStmtExpList(StmtExpList):
    def __init__(self, exp_stmt, stmt_exp_list):
        self.exp_stmt = exp_stmt
        self.stmt_exp_list = stmt_exp_list

    def accept(self, visitor):
        visitor.visitCompoundStmtExpList(self)


class ForeachStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ForeachStmtConcrete(ForeachStmt):
    def __init__(self, type, id, exp, block):
        self.type = type
        self.id = id
        self.exp = exp
        self.block = block

    def accept(self, visitor):
        visitor.visitForeachStmtConcrete(self)


class JumpStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class JumpStmtBreak(JumpStmt):
    def __init__(self, break_stmt):
        self.break_stmt = break_stmt

    def accept(self, visitor):
        visitor.visitJumpStmtBreak(self)


class JumpStmtContinue(JumpStmt):
    def __init__(self, continue_stmt):
        self.continue_stmt = continue_stmt

    def accept(self, visitor):
        visitor.visitJumpStmtContinue(self)


class JumpStmtReturn(JumpStmt):
    def __init__(self, return_stmt):
        self.return_stmt = return_stmt

    def accept(self, visitor):
        visitor.visitJumpStmtReturn(self)


class BreakStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class BreakStmtConcrete(BreakStmt):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitBreakStmtConcrete(self)


class ContinueStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ContinueStmtConcrete(ContinueStmt):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitContinueStmtConcrete(self)


class ReturnStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ReturnStmtConcrete(ReturnStmt):
    def __init__(self, exp):
        self.exp = exp  # Pode ser None

    def accept(self, visitor):
        visitor.visitReturnStmtConcrete(self)


# Lista de argumentos
class ArgList(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SimpleArgList(ArgList):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        visitor.visitSimpleArgList(self)


class CompoundArgList(ArgList):
    def __init__(self, exp, arg_list):
        self.exp = exp
        self.arg_list = arg_list

    def accept(self, visitor):
        visitor.visitCompoundArgList(self)


# Expressoes primarias
class PrimaryExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class PrimaryExpNoArrayCreation(PrimaryExp):
    def __init__(self, no_array_creation_exp):
        self.no_array_creation_exp = no_array_creation_exp

    def accept(self, visitor):
        visitor.visitPrimaryExpNoArrayCreation(self)


# class PrimaryExpArrayCreation(PrimaryExp):
#     def __init__(self, array_creation_exp):
#         self.array_creation_exp = array_creation_exp

#     def accept(self, visitor):
#         visitor.visitPrimaryExpArrayCreation(self)


# class NoArrayCreationExp(ABC):
#     @abstractmethod
#     def accept(self, visitor):
#         pass


class BooleanExp(NoArrayCreationExp):
    def __init__(self, bool_value):
        self.bool_value = bool_value

    def accept(self, visitor):
        visitor.visitBooleanExp(self)


class NullExp(NoArrayCreationExp):
    def __init__(self, null_value):
        self.null_value = null_value

    def accept(self, visitor):
        visitor.visitNullExp(self)


class IntNumExp(NoArrayCreationExp):
    def __init__(self, int_value):
        self.int_value = int_value

    def accept(self, visitor):
        visitor.visitIntNumExp(self)


class HexNumExp(NoArrayCreationExp):
    def __init__(self, hex_value):
        self.hex_value = hex_value

    def accept(self, visitor):
        visitor.visitHexNumExp(self)


class BinNumExp(NoArrayCreationExp):
    def __init__(self, bin_value):
        self.bin_value = bin_value

    def accept(self, visitor):
        visitor.visitBinNumExp(self)


class FloatNumExp(NoArrayCreationExp):
    def __init__(self, float_value):
        self.float_value = float_value

    def accept(self, visitor):
        visitor.visitFloatNumExp(self)


class DoubleNumExp(NoArrayCreationExp):
    def __init__(self, double_value):
        self.double_value = double_value

    def accept(self, visitor):
        visitor.visitDoubleNumExp(self)


class DecimalNumExp(NoArrayCreationExp):
    def __init__(self, decimal_value):
        self.decimal_value = decimal_value

    def accept(self, visitor):
        visitor.visitDecimalNumExp(self)


class CharExp(NoArrayCreationExp):
    def __init__(self, char_literal):
        self.char_literal = char_literal

    def accept(self, visitor):
        visitor.visitCharExp(self)


class StringExp(NoArrayCreationExp):
    def __init__(self, string_literal):
        self.string_literal = string_literal

    def accept(self, visitor):
        visitor.visitStringExp(self)


class IdExp(NoArrayCreationExp):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.visitIdExp(self)


class PrimaryParenthesizedExp(NoArrayCreationExp):
    def __init__(self, parenthesized_exp):
        self.parenthesized_exp = parenthesized_exp

    def accept(self, visitor):
        visitor.visitPrimaryParenthesizedExp(self)


class ParenthesizedExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ParenthesizedExpConcrete(ParenthesizedExp):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        visitor.visitParenthesizedExpConcrete(self)


class PrimaryMemberAccessExp(NoArrayCreationExp):
    def __init__(self, member_access):
        self.member_access = member_access

    def accept(self, visitor):
        visitor.visitPrimaryMemberAccessExp(self)


class MemberAccessExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class MemberAccessExpConcrete(MemberAccessExp):
    def __init__(self, primary_exp, id):
        self.primary_exp = primary_exp
        self.id = id

    def accept(self, visitor):
        visitor.visitMemberAccessExpConcrete(self)


class PrimaryInvocationExp(NoArrayCreationExp):
    def __init__(self, invocation_exp):
        self.invocation_exp = invocation_exp

    def accept(self, visitor):
        visitor.visitPrimaryInvocationExp(self)


class InvocationExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class InvocationExpConcrete(InvocationExp):
    def __init__(self, primary_exp, arg_list):
        self.primary_exp = primary_exp
        self.arg_list = arg_list  # Pode ser None

    def accept(self, visitor):
        visitor.visitInvocationExpConcrete(self)


class PrimaryElementAccessExp(NoArrayCreationExp):
    def __init__(self, element_access):
        self.element_access = element_access

    def accept(self, visitor):
        visitor.visitPrimaryElementAccessExp(self)


class ElementAccessExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ElementAccessExpConcrete(ElementAccessExp):
    def __init__(self, no_array_creation_exp, exp):
        self.no_array_creation_exp = no_array_creation_exp
        self.exp = exp

    def accept(self, visitor):
        visitor.visitElementAccessExpConcrete(self)


class ThisExp(NoArrayCreationExp):
    def __init__(self, this_value):
        self.this_value = this_value

    def accept(self, visitor):
        visitor.visitThisExp(self)


class PrimaryPostIncrementExp(NoArrayCreationExp):
    def __init__(self, post_increment_exp):
        self.post_increment_exp = post_increment_exp

    def accept(self, visitor):
        visitor.visitPrimaryPostIncrementExp(self)


class PrimaryPostDecrementExp(NoArrayCreationExp):
    def __init__(self, post_decrement_exp):
        self.post_decrement_exp = post_decrement_exp

    def accept(self, visitor):
        visitor.visitPrimaryPostDecrementExp(self)


class PrimaryObjectCreationExp(NoArrayCreationExp):
    def __init__(self, object_creation_exp):
        self.object_creation_exp = object_creation_exp

    def accept(self, visitor):
        visitor.visitPrimaryObjectCreationExp(self)


class PrimaryDefaultExp(NoArrayCreationExp):
    def __init__(self, default_exp):
        self.default_exp = default_exp

    def accept(self, visitor):
        visitor.visitPrimaryDefaultExp(self)


class ExpList(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SingleExpList(ExpList):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        visitor.visitSingleExpList(self)


class CompoundExpList(ExpList):
    def __init__(self, exp_list, exp):
        self.exp_list = exp_list
        self.exp = exp

    def accept(self, visitor):
        visitor.visitCompoundExpList(self)


# class ArrayCreationExp(ABC):
#     @abstractmethod
#     def accept(self, visitor):
#         pass


# class ArrayCreationExp(ArrayCreationExp):
#     def __init__(self, exp):
#         self.exp = exp

#     def accept(self, visitor):
#         visitor.visitArrayCreationExp(self)


class UnaryPrimaryExp(UnaryExp):
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp

    def accept(self, visitor):
        visitor.visitUnaryPrimaryExp(self)


class UnaryPreIncrementExp(UnaryExp):
    def __init__(self, pre_increment_exp):
        self.pre_increment_exp = pre_increment_exp

    def accept(self, visitor):
        visitor.visitUnaryPreIncrementExp(self)


class UnaryPreDecrementExp(UnaryExp):
    def __init__(self, pre_decrement_exp):
        self.pre_decrement_exp = pre_decrement_exp

    def accept(self, visitor):
        visitor.visitUnaryPreDecrementExp(self)


class UnaryCastExp(UnaryExp):
    def __init__(self, cast_exp):
        self.cast_exp = cast_exp

    def accept(self, visitor):
        visitor.visitUnaryCastExp(self)


class CastExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class CastExpConcrete(CastExp):
    def __init__(self, type, unary_exp):
        self.type = type
        self.unary_exp = unary_exp

    def accept(self, visitor):
        visitor.visitCastExpConcrete(self)


class UnaryMinusExp(UnaryExp):
    def __init__(self, minus_exp):
        self.minus_exp = minus_exp

    def accept(self, visitor):
        visitor.visitUnaryMinusExp(self)


class MinusExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class MinusExpConcrete(MinusExp):
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp

    def accept(self, visitor):
        visitor.visitMinusExpConcrete(self)


class UnaryPlusExp(UnaryExp):
    def __init__(self, plus_exp):
        self.plus_exp = plus_exp

    def accept(self, visitor):
        visitor.visitUnaryPlusExp(self)


class PlusExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class PlusExpConcrete(PlusExp):
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp

    def accept(self, visitor):
        visitor.visitPlusExpConcrete(self)


class Exp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ExpNonAssignment(Exp):
    def __init__(self, non_assignment_exp):
        self.non_assignment_exp = non_assignment_exp

    def accept(self, visitor):
        visitor.visitExpNonAssignment(self)


class ExpAssignment(Exp):
    def __init__(self, assignment):
        self.assignment = assignment

    def accept(self, visitor):
        visitor.visitExpAssignment(self)


class NonAssignmentExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class NonAssignmentConditionalExp(NonAssignmentExp):
    def __init__(self, conditional_exp):
        self.conditional_exp = conditional_exp

    def accept(self, visitor):
        visitor.visitNonAssignmentConditionalExp(self)


class ConditionalExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class TernaryExp(ConditionalExp):
    def __init__(self, conditional_or_exp, exp1, exp2):
        self.conditional_or_exp = conditional_or_exp
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitTernaryExp(self)


class ConditionalExpNext(ConditionalExp):
    def __init__(self, conditional_or_exp):
        self.conditional_or_exp = conditional_or_exp

    def accept(self, visitor):
        visitor.visitConditionalExpNext(self)


class ConditionalOrExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConditionalOrExpConcrete(ConditionalOrExp):
    def __init__(self, conditional_or_exp, conditional_and_exp):
        self.conditional_or_exp = conditional_or_exp
        self.conditional_and_exp = conditional_and_exp

    def accept(self, visitor):
        visitor.visitConditionalOrExpConcrete(self)


class ConditionalOrExpNext(ConditionalOrExp):
    def __init__(self, conditional_and_exp):
        self.conditional_and_exp = conditional_and_exp

    def accept(self, visitor):
        visitor.visitConditionalOrExpNext(self)


class ConditionalAndExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConditionalAndExpConcrete(ConditionalAndExp):
    def __init__(self, conditional_and_exp, inclusive_or_exp):
        self.conditional_and_exp = conditional_and_exp
        self.inclusive_or_exp = inclusive_or_exp

    def accept(self, visitor):
        visitor.visitConditionalAndExpConcrete(self)


class ConditionalAndExpNext(ConditionalAndExp):
    def __init__(self, inclusive_or_exp):
        self.inclusive_or_exp = inclusive_or_exp

    def accept(self, visitor):
        visitor.visitConditionalAndExpNext(self)


class InclusiveOrExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class InclusiveOrExpConcrete(InclusiveOrExp):
    def __init__(self, inclusive_or_exp, exclusive_or_exp):
        self.inclusive_or_exp = inclusive_or_exp
        self.exclusive_or_exp = exclusive_or_exp

    def accept(self, visitor):
        visitor.visitInclusiveOrExpConcrete(self)


class InclusiveOrExpNext(InclusiveOrExp):
    def __init__(self, exclusive_or_exp):
        self.exclusive_or_exp = exclusive_or_exp

    def accept(self, visitor):
        visitor.visitInclusiveOrExpNext(self)


class ExclusiveOrExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ExclusiveOrExpConcrete(ExclusiveOrExp):
    def __init__(self, exclusive_or_exp, and_exp):
        self.exclusive_or_exp = exclusive_or_exp
        self.and_exp = and_exp

    def accept(self, visitor):
        visitor.visitExclusiveOrExpConcrete(self)


class ExclusiveOrExpNext(ExclusiveOrExp):
    def __init__(self, and_exp):
        self.and_exp = and_exp

    def accept(self, visitor):
        visitor.visitExclusiveOrExpNext(self)


class AndExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class AndExpConcrete(AndExp):
    def __init__(self, and_exp, equality_exp):
        self.and_exp = and_exp
        self.equality_exp = equality_exp

    def accept(self, visitor):
        visitor.visitAndExpConcrete(self)


class AndExpNext(AndExp):
    def __init__(self, equality_exp):
        self.equality_exp = equality_exp

    def accept(self, visitor):
        visitor.visitAndExpNext(self)


class EqualityExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class EqualExp(EqualityExp):
    def __init__(self, equality_exp, relational_exp):
        self.equality_exp = equality_exp
        self.relational_exp = relational_exp

    def accept(self, visitor):
        visitor.visitEqualExp(self)


class NotEqualExp(EqualityExp):
    def __init__(self, equality_exp, relational_exp):
        self.equality_exp = equality_exp
        self.relational_exp = relational_exp

    def accept(self, visitor):
        visitor.visitNotEqualExp(self)


class EqualityExpNext(EqualityExp):
    def __init__(self, relational_exp):
        self.relational_exp = relational_exp

    def accept(self, visitor):
        visitor.visitEqualityExpNext(self)


class RelationalExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class LessExp(RelationalExp):
    def __init__(self, relational_exp, shift_exp):
        self.relational_exp = relational_exp
        self.shift_exp = shift_exp

    def accept(self, visitor):
        visitor.visitLessExp(self)


class GreaterExp(RelationalExp):
    def __init__(self, relational_exp, shift_exp):
        self.relational_exp = relational_exp
        self.shift_exp = shift_exp

    def accept(self, visitor):
        visitor.visitGreaterExp(self)


class LessEqualExp(RelationalExp):
    def __init__(self, relational_exp, shift_exp):
        self.relational_exp = relational_exp
        self.shift_exp = shift_exp

    def accept(self, visitor):
        visitor.visitLessEqualExp(self)


class GreaterEqualExp(RelationalExp):
    def __init__(self, relational_exp, shift_exp):
        self.relational_exp = relational_exp
        self.shift_exp = shift_exp

    def accept(self, visitor):
        visitor.visitGreaterEqualExp(self)


class IsTypeExp(RelationalExp):
    def __init__(self, relational_exp, type):
        self.relational_exp = relational_exp
        self.type = type

    def accept(self, visitor):
        visitor.visitIsTypeExp(self)


class RelationalExpNext(RelationalExp):
    def __init__(self, shift_exp):
        self.shift_exp = shift_exp

    def accept(self, visitor):
        visitor.visitRelationalExpNext(self)


class ShiftExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class LeftShiftExp(ShiftExp):
    def __init__(self, shift_exp, additive_exp):
        self.shift_exp = shift_exp
        self.additive_exp = additive_exp

    def accept(self, visitor):
        visitor.visitLeftShiftExp(self)


class RightShiftExp(ShiftExp):
    def __init__(self, shift_exp, additive_exp):
        self.shift_exp = shift_exp
        self.additive_exp = additive_exp

    def accept(self, visitor):
        visitor.visitRightShiftExp(self)


class ShiftExpNext(ShiftExp):
    def __init__(self, additive_exp):
        self.additive_exp = additive_exp

    def accept(self, visitor):
        visitor.visitShiftExpNext(self)


class AdditiveExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SumExp(AdditiveExp):
    def __init__(self, additive_exp, multiplicative_exp):
        self.additive_exp = additive_exp
        self.multiplicative_exp = multiplicative_exp

    def accept(self, visitor):
        visitor.visitSumExp(self)


class SubExp(AdditiveExp):
    def __init__(self, additive_exp, multiplicative_exp):
        self.additive_exp = additive_exp
        self.multiplicative_exp = multiplicative_exp

    def accept(self, visitor):
        visitor.visitSubExp(self)


class AdditiveExpNext(AdditiveExp):
    def __init__(self, multiplicative_exp):
        self.multiplicative_exp = multiplicative_exp

    def accept(self, visitor):
        visitor.visitAdditiveExpNext(self)


class MultiplicativeExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class MultExp(MultiplicativeExp):
    def __init__(self, multiplicative_exp, unary_exp):
        self.multiplicative_exp = multiplicative_exp
        self.unary_exp = unary_exp

    def accept(self, visitor):
        visitor.visitMultExp(self)


class DivExp(MultiplicativeExp):
    def __init__(self, multiplicative_exp, unary_exp):
        self.multiplicative_exp = multiplicative_exp
        self.unary_exp = unary_exp

    def accept(self, visitor):
        visitor.visitDivExp(self)


class ModExp(MultiplicativeExp):
    def __init__(self, multiplicative_exp, unary_exp):
        self.multiplicative_exp = multiplicative_exp
        self.unary_exp = unary_exp

    def accept(self, visitor):
        visitor.visitModExp(self)


class MultiplicativeExpNext(MultiplicativeExp):
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp

    def accept(self, visitor):
        visitor.visitMultiplicativeExpNext(self)


class AssignExp(Exp):
    def __init__(self, unary_exp, exp):
        self.unary_exp = unary_exp
        self.exp = exp

    def accept(self, visitor):
        visitor.visitAssignExp(self)


class ClassDeclaration(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ClassDeclWithMod(ClassDeclaration):
    def __init__(self, class_modifier, id, class_body):
        self.class_modifier = class_modifier
        self.id = id
        self.class_body = class_body

    def accept(self, visitor):
        visitor.visitClassDeclWithMod(self)


class ClassDeclSimple(ClassDeclaration):
    def __init__(self, id, class_body):
        self.id = id
        self.class_body = class_body

    def accept(self, visitor):
        visitor.visitClassDeclSimple(self)


class ClassMod(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ClassModPublic(ClassMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitClassModPublic(self)


class ClassModProtected(ClassMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitClassModProtected(self)


class ClassModPrivate(ClassMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitClassModPrivate(self)


class ClassModStatic(ClassMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitClassModStatic(self)


class ClassBody(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ClassBodyConcrete(ClassBody):
    def __init__(self, class_member_decl):
        self.class_member_decl = class_member_decl

    def accept(self, visitor):
        visitor.visitClassBodyConcrete(self)


class ClassMemberDeclaration(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ClassMemberConstant(ClassMemberDeclaration):
    def __init__(self, constant_declaration):
        self.constant_declaration = constant_declaration

    def accept(self, visitor):
        visitor.visitClassMemberConstant(self)


class ClassMemberField(ClassMemberDeclaration):
    def __init__(self, field_declaration):
        self.field_declaration = field_declaration

    def accept(self, visitor):
        visitor.visitClassMemberField(self)


class ClassMemberMethod(ClassMemberDeclaration):
    def __init__(self, method_declaration):
        self.method_declaration = method_declaration

    def accept(self, visitor):
        visitor.visitClassMemberMethod(self)


class ClassMemberConstructor(ClassMemberDeclaration):
    def __init__(self, constructor_declaration):
        self.constructor_declaration = constructor_declaration

    def accept(self, visitor):
        visitor.visitClassMemberConstructor(self)


class ConstantDeclaration(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConstDeclWithMod(ConstantDeclaration):
    def __init__(self, const_modifier, type, const_declarators):
        self.const_modifier = const_modifier
        self.type = type
        self.const_declarators = const_declarators

    def accept(self, visitor):
        visitor.visitConstDeclWithMod(self)


class ConstDeclSimple(ConstantDeclaration):
    def __init__(self, type, const_declarators):
        self.type = type
        self.const_declarators = const_declarators

    def accept(self, visitor):
        visitor.visitConstDeclSimple(self)


class ConstMod(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConstModPublic(ConstMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitConstModPublic(self)


class ConstModProtected(ConstMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitConstModProtected(self)


class ConstModPrivate(ConstMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitConstModPrivate(self)


class FieldDeclaration(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class FieldDeclWithMod(FieldDeclaration):
    def __init__(self, field_modifiers, type, var_declarators):
        self.field_modifiers = field_modifiers
        self.type = type
        self.var_declarators = var_declarators

    def accept(self, visitor):
        visitor.visitFieldDeclWithMod(self)


class FieldDeclSimple(FieldDeclaration):
    def __init__(self, type, var_declarators):
        self.type = type
        self.var_declarators = var_declarators

    def accept(self, visitor):
        visitor.visitFieldDeclSimple(self)


class FieldModifiers(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SingleFieldModifier(FieldModifiers):
    def __init__(self, field_modifier):
        self.field_modifier = field_modifier

    def accept(self, visitor):
        visitor.visitSingleFieldModifier(self)


class CompoundFieldModifier(FieldModifiers):
    def __init__(self, field_modifier, field_modifiers):
        self.field_modifier = field_modifier
        self.field_modifiers = field_modifiers

    def accept(self, visitor):
        visitor.visitCompoundFieldModifier(self)


class FieldMod(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class FieldModNew(FieldMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitFieldModNew(self)


class FieldModPublic(FieldMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitFieldModPublic(self)


class FieldModProtected(FieldMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitFieldModProtected(self)


class FieldModPrivate(FieldMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitFieldModPrivate(self)


class FieldModStatic(FieldMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitFieldModStatic(self)


class MethodDeclaration(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class MethodDeclWithMod(MethodDeclaration):
    def __init__(self, method_modifiers, type, method_head, block):
        self.method_modifiers = method_modifiers
        self.type = type
        self.method_head = method_head
        self.block = block

    def accept(self, visitor):
        visitor.visitMethodDeclWithMod(self)


class MethodDeclSimple(MethodDeclaration):
    def __init__(self, type, method_head, block):
        self.type = type
        self.method_head = method_head
        self.block = block

    def accept(self, visitor):
        visitor.visitMethodDeclSimple(self)


class MethodModifiers(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SingleMethodModifier(MethodModifiers):
    def __init__(self, method_modifier):
        self.method_modifier = method_modifier

    def accept(self, visitor):
        visitor.visitSingleMethodModifier(self)


class CompoundMethodModifier(MethodModifiers):
    def __init__(self, method_modifier, method_modifiers):
        self.method_modifier = method_modifier
        self.method_modifiers = method_modifiers

    def accept(self, visitor):
        visitor.visitCompoundMethodModifier(self)


class MethodMod(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class MethodModPublic(MethodMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitMethodModPublic(self)


class MethodModProtected(MethodMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitMethodModProtected(self)


class MethodModPrivate(MethodMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitMethodModPrivate(self)


class MethodModStatic(MethodMod):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitMethodModStatic(self)


class MethodHead(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class MethodHeadConcrete(MethodHead):
    def __init__(self, id, param_list):
        self.id = id
        self.param_list = param_list

    def accept(self, visitor):
        visitor.visitMethodHeadConcrete(self)
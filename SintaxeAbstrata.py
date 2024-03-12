from abc import ABC, abstractmethod


# Herdado por mais de uma classe (talvez mudar)
class NoArrayCreationExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class FuncDecl(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class FuncDeclConcrete(FuncDecl):
    def __init__(self, signature, block):
        self.signature = signature
        self.block = block

    def accept(self, visitor):
        return visitor.visitFuncDeclConcrete(self)


class Signature(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SignatureConcrete(Signature):
    def __init__(self, type, id, param_list):
        self.type = type
        self.id = id
        self.param_list = param_list  # Pode ser None

    def accept(self, visitor):
        return visitor.visitSignatureConcrete(self)


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
        visitor.visitDeclarationVar(self)


class ConstDeclaration(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConstDeclarationConcrete(ConstDeclaration):
    def __init__(self, type, const_declarators):
        self.type = type
        self.const_declarators = const_declarators

    def accept(self, visitor):
        visitor.visitConstDeclarationConcrete(self)


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


class VarDeclaration(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class VarDeclarationConcrete(VarDeclaration):
    def __init__(self, type, var_declarators):
        self.type = type
        self.var_declarators = var_declarators

    def accept(self, visitor):
        visitor.visitVarDeclarationConcrete(self)


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


class VarDeclaratorIdArray(VarDeclarator):
    def __init__(self, id, array_initializer):
        self.id = id
        self.array_initializer = array_initializer

    def accept(self, visitor):
        visitor.visitVarDeclaratorIdArray(self)


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


# Comando de expressao
class ExpStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ExpStmtInvocation(ExpStmt):
    def __init__(self, invocation_exp):
        self.invocation_exp = invocation_exp

    def accept(self, visitor):
        visitor.visitExpStmtInvocation(self)


class ExpStmtObjectCreation(ExpStmt):
    def __init__(self, object_creation_exp):
        self.object_creation_exp = object_creation_exp

    def accept(self, visitor):
        visitor.visitExpStmtObjectCreation(self)


class ExpStmtAssignment(ExpStmt):
    def __init__(self, assignment):
        self.assignment = assignment

    def accept(self, visitor):
        visitor.visitExpStmtAssignment(self)


class ExpStmtPostIncrement(ExpStmt):
    def __init__(self, post_increment_exp):
        self.post_increment_exp = post_increment_exp

    def accept(self, visitor):
        visitor.visitExpStmtPostIncrement(self)


class ExpStmtPostDecrement(ExpStmt):
    def __init__(self, post_decrement_exp):
        self.post_decrement_exp = post_decrement_exp

    def accept(self, visitor):
        visitor.visitExpStmtPostDecrement(self)


class ExpStmtPreIncrement(ExpStmt):
    def __init__(self, pre_increment_exp):
        self.pre_increment_exp = pre_increment_exp

    def accept(self, visitor):
        visitor.visitExpStmtPreIncrement(self)


class ExpStmtPreDecrement(ExpStmt):
    def __init__(self, pre_decrement_exp):
        self.pre_decrement_exp = pre_decrement_exp

    def accept(self, visitor):
        visitor.visitExpStmtPreDecrement(self)


# Comando para criacao de objetos
class ObjectCreationExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class NoArgsObjectCreation(ObjectCreationExp, NoArrayCreationExp):
    def __init__(self, type):
        self.type = type

    def accept(self, visitor):
        visitor.visitNoArgsObjectCreation(self)


class NoArgsWithInitializerObjectCreation(ObjectCreationExp, NoArrayCreationExp):
    def __init__(self, type, member_initializer_list):
        self.type = type
        self.member_initializer_list = member_initializer_list

    def accept(self, visitor):
        visitor.visitNoArgsWithInitializerObjectCreation(self)


class ObjectCreation(ObjectCreationExp, NoArrayCreationExp):
    def __init__(self, type, arg_list):
        self.type = type
        self.arg_list = arg_list

    def accept(self, visitor):
        visitor.visitObjectCreation(self)


class WithInitializerObjectCreation(ObjectCreationExp, NoArrayCreationExp):
    def __init__(self, type, arg_list, member_initializer_list):
        self.type = type
        self.arg_list = arg_list
        self.member_initializer_list = member_initializer_list

    def accept(self, visitor):
        visitor.visitWithInitializerObjectCreation(self)


# class ObjectInitializer(ABC):
#     @abstractmethod
#     def accept(self, visitor):
#         pass


# class ObjectInitializerConcrete(ObjectInitializer):
#     def __init__(self, member_initializer_list):
#         self.member_initializer_list = member_initializer_list

#     def accept(self, visitor):
#         visitor.visitObjectInitializerConcrete(self)


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


class PostIncrementExpConcrete(PostIncrementExp, NoArrayCreationExp):
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp

    def accept(self, visitor):
        visitor.visitPostIncrementExpConcrete(self)


class PostDecrementExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class PostDecrementExpConcrete(PostDecrementExp, NoArrayCreationExp):
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
    def __init__(self, exp, embedded_stmt):
        self.exp = exp
        self.embedded_stmt = embedded_stmt

    def accept(self, visitor):
        visitor.visitSimpleIfStmt(self)


class IfElseStmt(IfStmt):
    def __init__(self, exp, embedded_stmt1, embedded_stmt2):
        self.exp = exp
        self.embedded_stmt1 = embedded_stmt1
        self.embedded_stmt2 = embedded_stmt2

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


# class SwitchBlock(ABC):
#     @abstractmethod
#     def accept(self, visitor):
#         pass


# class SwitchBlockConcrete(SwitchBlock):
#     def __init__(self, switch_body):
#         self.switch_body = switch_body

#     def accept(self, visitor):
#         visitor.visitSwitchBlockConcrete(self)


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


class PatternConcrete(Pattern):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        visitor.visitPatternConcrete(self)


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
    def __init__(self, exp, embedded_stmt):
        self.exp = exp
        self.embedded_stmt = embedded_stmt

    def accept(self, visitor):
        visitor.visitWhileStmtConcrete(self)


class DoStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class DoStmtConcrete(DoStmt):
    def __init__(self, embedded_stmt, exp):
        self.embedded_stmt = embedded_stmt
        self.exp = exp

    def accept(self, visitor):
        visitor.visitDoStmtConcrete(self)


class ForStmt(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ForStmtConcrete(ForStmt):
    def __init__(self, for_initializer, for_condition, for_iterator, embedded_stmt):
        self.for_initializer = for_initializer  # Pode ser None
        self.for_condition = for_condition  # Pode ser None
        self.for_iterator = for_iterator  # Pode ser None
        self.embedded_stmt = embedded_stmt

    def accept(self, visitor):
        visitor.visitForStmtConcrete(self)


class ForInitializer(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class SimpleForInitializer(ForInitializer):
    def __init__(self, var_declaration):
        self.var_declaration = var_declaration

    def accept(self, visitor):
        visitor.visitSimpleForInitializer(self)


class CompoundForInitializer(ForInitializer):
    def __init__(self, var_declaration, for_initializer):
        self.var_declaration = var_declaration
        self.for_initializer = for_initializer

    def accept(self, visitor):
        visitor.visitCompoundForInitializer(self)


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
    def __init__(self, type, id, exp, embedded_stmt):
        self.type = type
        self.id = id
        self.exp = exp
        self.embedded_stmt = embedded_stmt

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


class PrimaryExpArrayCreation(PrimaryExp):
    def __init__(self, array_creation_exp):
        self.array_creation_exp = array_creation_exp

    def accept(self, visitor):
        visitor.visitPrimaryExpArrayCreation(self)


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


class ParenthesizedExp(NoArrayCreationExp):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        visitor.visitParenthesizedExp(self)


class TupleExpDefinition(NoArrayCreationExp):
    def __init__(self, tuple_exp):
        self.tuple_exp = tuple_exp

    def accept(self, visitor):
        visitor.visitTupleExpDefinition(self)


class MemberAccessExp(NoArrayCreationExp):
    def __init__(self, primary_exp, id):
        self.primary_exp = primary_exp
        self.id = id

    def accept(self, visitor):
        visitor.visitMemberAccessExp(self)


class InvocationExp(NoArrayCreationExp, ExpStmt):
    def __init__(self, primary_exp, arg_list):
        self.primary_exp = primary_exp
        self.arg_list = arg_list  # Pode ser None

    def accept(self, visitor):
        visitor.visitInvocationExp(self)


class ElementAccessExp(NoArrayCreationExp):
    def __init__(self, no_array_creation_exp, exp):
        self.no_array_creation_exp = no_array_creation_exp
        self.exp = exp

    def accept(self, visitor):
        visitor.visitElementAccessExp(self)


class ThisExp(NoArrayCreationExp):
    def __init__(self, this_value):
        self.this_value = this_value

    def accept(self, visitor):
        visitor.visitThisExp(self)


class TypeofExp(NoArrayCreationExp):
    def __init__(self, type):
        self.type = type

    def accept(self, visitor):
        visitor.visitTypeofExp(self)


class SizeofExp(NoArrayCreationExp):
    def __init__(self, value_type):
        self.value_type = value_type

    def accept(self, visitor):
        visitor.visitSizeofExp(self)


class DefaultExp(NoArrayCreationExp):
    def __init__(self, type):
        self.type = type  # Pode ser None

    def accept(self, visitor):
        visitor.visitDefaultExp(self)


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


class ArrayCreationExp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# Pensar ainda
# class ArrayCreationExp(ArrayCreationExp):
#     def __init__(self, exp):
#         self.exp = exp

#     def accept(self, visitor):
#         visitor.visitSingleExpList(self)


# Pensar em remover tuplas

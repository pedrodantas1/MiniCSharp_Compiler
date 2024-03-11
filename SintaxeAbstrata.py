from abc import ABC, abstractmethod


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
        self.param_list = param_list

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
        self.stmt_list = stmt_list

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

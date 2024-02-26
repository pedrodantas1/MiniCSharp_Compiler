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


class Statement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class DeclarationStatement(Statement):
    def __init__(self, declaration_stmt):
        self.declaration_stmt = declaration_stmt

    def accept(self, visitor):
        visitor.visitDeclarationStatement(self)


class EmbeddedStatement(Statement):
    def __init__(self, embedded_stmt):
        self.embedded_stmt = embedded_stmt

    def accept(self, visitor):
        visitor.visitEmbeddedStatement(self)

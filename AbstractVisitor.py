from abc import ABC, abstractmethod


class AbstractVisitor(ABC):

    # @abstractmethod
    # def visitSingleTypeName(self, singletypename):
    #     pass

    # @abstractmethod
    # def visitCompoundTypeName(self, compoundtypename):
    #     pass

    @abstractmethod
    def visitTypeClass(self, typeclass):
        pass

    @abstractmethod
    def visitTypeValue(self, typevalue):
        pass

    # @abstractmethod
    # def visitGenericClassType(self, genericclasstype):
    #     pass

    @abstractmethod
    def visitObjectClassType(self, objectclasstype):
        pass

    @abstractmethod
    def visitStringClassType(self, stringclasstype):
        pass

    @abstractmethod
    def visitIntegralTypeRef(self, integraltyperef):
        pass

    @abstractmethod
    def visitFloatingPointTypeRef(self, floatingpointtyperef):
        pass

    @abstractmethod
    def visitBoolType(self, booltype):
        pass

    @abstractmethod
    def visitVoidType(self, voidtype):
        pass

    @abstractmethod
    def visitIntType(self, inttype):
        pass

    @abstractmethod
    def visitLongType(self, longtype):
        pass

    @abstractmethod
    def visitCharType(self, chartype):
        pass

    @abstractmethod
    def visitFloatType(self, floattype):
        pass

    @abstractmethod
    def visitDoubleType(self, doubletype):
        pass

    @abstractmethod
    def visitDecimalType(self, decimaltype):
        pass

    @abstractmethod
    def visitFuncDeclConcrete(self, funcdecl):
        pass

    @abstractmethod
    def visitSignatureConcrete(self, signature):
        pass

    @abstractmethod
    def visitSingleParamList(self, singleparamlist):
        pass

    @abstractmethod
    def visitCompoundParamList(self, compoundparamlist):
        pass

    @abstractmethod
    def visitSingleStatementList(self, singlestatementlist):
        pass

    @abstractmethod
    def visitCompoundStatementList(self, compoundstatementlist):
        pass

    @abstractmethod
    def visitStatementDeclaration(self, statementdeclaration):
        pass

    @abstractmethod
    def visitStatementEmbedded(self, statementembedded):
        pass

    @abstractmethod
    def visitDeclarationStmtConst(self, declarationstmtconst):
        pass

    @abstractmethod
    def visitDeclarationVar(self, declarationvar):
        pass

    @abstractmethod
    def visitConstDeclarationConcrete(self, constdeclaration):
        pass

    @abstractmethod
    def visitSingleConstDeclarators(self, singleconstdeclarators):
        pass

    @abstractmethod
    def visitCompoundConstDeclarators(self, compoundconstdeclarators):
        pass

    @abstractmethod
    def visitConstDeclaratorConcrete(self, constdeclarator):
        pass

    @abstractmethod
    def visitVarDeclarationConcrete(self, vardeclaration):
        pass

    @abstractmethod
    def visitSingleVarDeclarators(self, singlevardeclarators):
        pass

    @abstractmethod
    def visitCompoundVarDeclarators(self, compoundvardeclarators):
        pass

    @abstractmethod
    def visitVarDeclaratorId(self, vardeclaratorid):
        pass

    @abstractmethod
    def visitVarDeclaratorIdExp(self, vardeclaratoridexp):
        pass

    # @abstractmethod
    # def visitVarDeclaratorIdArray(self, vardeclaratoridarray):
    #     pass

    @abstractmethod
    def visitEmbeddedStmtBlock(self, embeddedstmtblock):
        pass

    @abstractmethod
    def visitEmbeddedStmtEmpty(self, embeddedstmtempty):
        pass

    @abstractmethod
    def visitEmbeddedStmtExp(self, embeddedstmtexp):
        pass

    @abstractmethod
    def visitEmbeddedStmtSelection(self, embeddedstmtselection):
        pass

    @abstractmethod
    def visitEmbeddedStmtIteration(self, embeddedstmtiteration):
        pass

    @abstractmethod
    def visitEmbeddedStmtJump(self, embeddedstmtjump):
        pass

    @abstractmethod
    def visitBlockStmtConcrete(self, blockstmt):
        pass

    @abstractmethod
    def visitEmptyStmtConcrete(self, emptystmt):
        pass

    @abstractmethod
    def visitExpStmtConcrete(self, expstmt):
        pass

    @abstractmethod
    def visitStmtExpInvocation(self, stmtexpinvocation):
        pass

    @abstractmethod
    def visitStmtExpObjectCreation(self, stmtexpobjectcreation):
        pass

    @abstractmethod
    def visitStmtExpAssignment(self, stmtexpassignment):
        pass

    @abstractmethod
    def visitStmtExpPostIncrement(self, stmtexppostincrement):
        pass

    @abstractmethod
    def visitStmtExpPostDecrement(self, stmtexppostdecrement):
        pass

    @abstractmethod
    def visitStmtExpPreIncrement(self, stmtexppreincrement):
        pass

    @abstractmethod
    def visitStmtExpPreDecrement(self, stmtexppredecrement):
        pass

    @abstractmethod
    def visitNoArgsObjectCreation(self, objectcreation):
        pass

    @abstractmethod
    def visitNoArgsWithInitializerObjectCreation(self, objectcreation):
        pass

    @abstractmethod
    def visitObjectCreation(self, objectcreation):
        pass

    @abstractmethod
    def visitWithInitializerObjectCreation(self, objectcreation):
        pass

    @abstractmethod
    def visitObjectInitializerConcrete(self, objectinitializer):
        pass

    @abstractmethod
    def visitSingleMemberInitializerList(self, memberinitializerlist):
        pass

    @abstractmethod
    def visitCompoundMemberInitializerList(self, memberinitializerlist):
        pass

    @abstractmethod
    def visitMemberInitializerConcrete(self, memberinitializer):
        pass

    @abstractmethod
    def visitPostIncrementExpConcrete(self, postincrementexp):
        pass

    @abstractmethod
    def visitPostDecrementExpConcrete(self, postdecrementexp):
        pass

    @abstractmethod
    def visitPreIncrementExpConcrete(self, preincrementexp):
        pass

    @abstractmethod
    def visitPreDecrementExpConcrete(self, predecrementexp):
        pass

    @abstractmethod
    def visitSelectionStmtIf(self, selectionstmtif):
        pass

    @abstractmethod
    def visitSelectionStmtSwitch(self, selectionstmtswitch):
        pass

    @abstractmethod
    def visitSimpleIfStmt(self, simpleifstmt):
        pass

    @abstractmethod
    def visitIfElseStmt(self, ifelsestmt):
        pass

    @abstractmethod
    def visitSwitchStmtConcrete(self, switchstmt):
        pass

    @abstractmethod
    def visitSimpleSwitchBody(self, simpleswitchbody):
        pass

    @abstractmethod
    def visitCompoundSwitchBody(self, compoundswitchbody):
        pass

    @abstractmethod
    def visitSimpleSwitchSection(self, simpleswitchsection):
        pass

    @abstractmethod
    def visitCompoundSwitchSection(self, compoundswitchsection):
        pass

    @abstractmethod
    def visitSwitchLabelCase(self, switchlabelcase):
        pass

    @abstractmethod
    def visitSwitchLabelDefault(self, switchlabeldefault):
        pass

    @abstractmethod
    def visitPatternConcrete(self, pattern):
        pass

    @abstractmethod
    def visitIterationStmtWhile(self, iterationstmtwhile):
        pass

    @abstractmethod
    def visitIterationStmtDo(self, iterationstmtdo):
        pass

    @abstractmethod
    def visitIterationStmtFor(self, iterationstmtfor):
        pass

    @abstractmethod
    def visitIterationStmtForeach(self, iterationstmtforeach):
        pass

    @abstractmethod
    def visitWhileStmtConcrete(self, whilestmt):
        pass

    @abstractmethod
    def visitDoStmtConcrete(self, dostmt):
        pass

    @abstractmethod
    def visitForStmtConcrete(self, forstmt):
        pass

    @abstractmethod
    def visitSimpleForInitializer(self, simpleforinitializer):
        pass

    @abstractmethod
    def visitForConditionConcrete(self, forcondition):
        pass

    @abstractmethod
    def visitForIteratorConcrete(self, foriterator):
        pass

    @abstractmethod
    def visitSimpleStmtExpList(self, simplestmtexplist):
        pass

    @abstractmethod
    def visitCompoundStmtExpList(self, compoundstmtexplist):
        pass

    @abstractmethod
    def visitForeachStmtConcrete(self, foreachstmt):
        pass

    @abstractmethod
    def visitJumpStmtBreak(self, jumpstmtbreak):
        pass

    @abstractmethod
    def visitJumpStmtContinue(self, jumpstmtcontinue):
        pass

    @abstractmethod
    def visitJumpStmtReturn(self, jumpstmtreturn):
        pass

    @abstractmethod
    def visitBreakStmtConcrete(self, breakstmt):
        pass

    @abstractmethod
    def visitContinueStmtConcrete(self, continuestmt):
        pass

    @abstractmethod
    def visitReturnStmtConcrete(self, returnstmt):
        pass

    @abstractmethod
    def visitSimpleArgList(self, simplearglist):
        pass

    @abstractmethod
    def visitCompoundArgList(self, compoundarglist):
        pass

    @abstractmethod
    def visitPrimaryExpNoArrayCreation(self, primaryexp):
        pass

    # @abstractmethod
    # def visitPrimaryExpArrayCreation(self, primaryexp):
    #     pass

    @abstractmethod
    def visitBooleanExp(self, booleanexp):
        pass

    @abstractmethod
    def visitNullExp(self, nullexp):
        pass

    @abstractmethod
    def visitIntNumExp(self, intnumexp):
        pass

    @abstractmethod
    def visitHexNumExp(self, hexnumexp):
        pass

    @abstractmethod
    def visitBinNumExp(self, binnumexp):
        pass

    @abstractmethod
    def visitFloatNumExp(self, floatnumexp):
        pass

    @abstractmethod
    def visitDoubleNumExp(self, doublenumexp):
        pass

    @abstractmethod
    def visitDecimalNumExp(self, decimalnumexp):
        pass

    @abstractmethod
    def visitCharExp(self, charexp):
        pass

    @abstractmethod
    def visitStringExp(self, stringexp):
        pass

    @abstractmethod
    def visitIdExp(self, idexp):
        pass

    @abstractmethod
    def visitPrimaryParenthesizedExp(self, primaryparenthesizedexp):
        pass

    @abstractmethod
    def visitParenthesizedExpConcrete(self, parenthesizedexp):
        pass

    @abstractmethod
    def visitPrimaryMemberAccessExp(self, primarymemberaccessexp):
        pass

    @abstractmethod
    def visitMemberAccessExpConcrete(self, memberaccessexp):
        pass

    @abstractmethod
    def visitPrimaryInvocationExp(self, primaryinvocationexp):
        pass

    @abstractmethod
    def visitInvocationExp(self, invocationexp):
        pass

    @abstractmethod
    def visitPrimaryElementAccessExp(self, primaryelementaccessexp):
        pass

    @abstractmethod
    def visitElementAccessExp(self, elementaccessexp):
        pass

    @abstractmethod
    def visitThisExp(self, thisexp):
        pass

    @abstractmethod
    def visitPrimaryPostIncrementExp(self, primarypostincrementexp):
        pass

    @abstractmethod
    def visitPrimaryPostDecrementExp(self, primarypostdecrementexp):
        pass

    @abstractmethod
    def visitPrimaryObjectCreationExp(self, primaryobjectcreationexp):
        pass

    @abstractmethod
    def visitPrimaryTypeofExp(self, primarytypeofexp):
        pass

    @abstractmethod
    def visitTypeofExpConcrete(self, typeofexp):
        pass

    @abstractmethod
    def visitPrimarySizeofExp(self, primarysizeofexp):
        pass

    @abstractmethod
    def visitSizeofExpConcrete(self, sizeofexp):
        pass

    @abstractmethod
    def visitPrimaryDefaultExp(self, primarydefaultexp):
        pass

    @abstractmethod
    def visitDefaultExpConcrete(self, defaultexp):
        pass

    @abstractmethod
    def visitSingleExpList(self, singleexplist):
        pass

    @abstractmethod
    def visitCompoundExpList(self, compoundexplist):
        pass

    @abstractmethod
    def visitSingleExpList(self, singleexplist):
        pass

    @abstractmethod
    def visitUnaryPrimaryExp(self, unaryprimaryexp):
        pass

    @abstractmethod
    def visitUnaryPreIncrementExp(self, unarypreincrementexp):
        pass

    @abstractmethod
    def visitUnaryPreDecrementExp(self, unarypredecrementexp):
        pass

    @abstractmethod
    def visitUnaryCastExp(self, unarycastexp):
        pass

    @abstractmethod
    def visitCastExpConcrete(self, castexp):
        pass

    @abstractmethod
    def visitUnaryMinusExp(self, unaryminusexp):
        pass

    @abstractmethod
    def visitMinusExpConcrete(self, minusexp):
        pass

    @abstractmethod
    def visitPlusExpConcrete(self, plusexp):
        pass

    @abstractmethod
    def visitPlusExpConcrete(self, plusexp):
        pass

    @abstractmethod
    def visitExpNonAssignment(self, expnonassignment):
        pass

    @abstractmethod
    def visitExpAssignment(self, expassignment):
        pass

    @abstractmethod
    def visitNonAssignmentConditionalExp(self, nonassignmentconditionalexp):
        pass

    @abstractmethod
    def visitTernaryExp(self, ternaryexp):
        pass

    @abstractmethod
    def visitConditionalExpNext(self, conditionalexpnext):
        pass

    @abstractmethod
    def visitConditionalOrExpConcrete(self, conditionalorexp):
        pass

    @abstractmethod
    def visitConditionalOrExpNext(self, conditionalorexpnext):
        pass

    @abstractmethod
    def visitConditionalAndExpConcrete(self, conditionalandexp):
        pass

    @abstractmethod
    def visitConditionalAndExpNext(self, conditionalandexpnext):
        pass

    @abstractmethod
    def visitInclusiveOrExpConcrete(self, inclusiveorexp):
        pass

    @abstractmethod
    def visitInclusiveOrExpNext(self, inclusiveorexpnext):
        pass

    @abstractmethod
    def visitExclusiveOrExpConcrete(self, exclusiveorexp):
        pass

    @abstractmethod
    def visitExclusiveOrExpNext(self, exclusiveorexpnext):
        pass

    @abstractmethod
    def visitAndExpConcrete(self, andexp):
        pass

    @abstractmethod
    def visitAndExpNext(self, andexpnext):
        pass

    @abstractmethod
    def visitEqualExp(self, equalexp):
        pass

    @abstractmethod
    def visitNotEqualExp(self, notequalexp):
        pass

    @abstractmethod
    def visitEqualityExpNext(self, equalityexpnext):
        pass

    @abstractmethod
    def visitLessExp(self, lessexp):
        pass

    @abstractmethod
    def visitGreaterExp(self, greaterexp):
        pass

    @abstractmethod
    def visitLessEqualExp(self, lessequalexp):
        pass

    @abstractmethod
    def visitGreaterEqualExp(self, greaterequalexp):
        pass

    @abstractmethod
    def visitIsTypeExp(self, istypeexp):
        pass

    @abstractmethod
    def visitRelationalExpNext(self, relationalexpnext):
        pass

    @abstractmethod
    def visitLeftShiftExp(self, leftshiftexp):
        pass

    @abstractmethod
    def visitRightShiftExp(self, rightshiftexp):
        pass

    @abstractmethod
    def visitShiftExpNext(self, shiftexpnext):
        pass

    @abstractmethod
    def visitSumExp(self, sumexp):
        pass

    @abstractmethod
    def visitSubExp(self, subexp):
        pass

    @abstractmethod
    def visitAdditiveExpNext(self, additiveexpnext):
        pass

    @abstractmethod
    def visitMultExp(self, multexp):
        pass

    @abstractmethod
    def visitDivExp(self, divexp):
        pass

    @abstractmethod
    def visitModExp(self, modexp):
        pass

    @abstractmethod
    def visitMultiplicativeExpNext(self, multiplicativeexpnext):
        pass

    @abstractmethod
    def visitAssignExp(self, assignexp):
        pass

from functools import partial

from AbstractVisitor import AbstractVisitor
from LanguageParser import *

# fmt: off

myprint = partial(print, end="", sep="")

tab = 0


def blank():
    p = ""
    for x in range(tab):
        p = p + " "
    return p


class Visitor(AbstractVisitor):
    def visitTypeClass(self, typeclass):
        typeclass.class_type.accept(self)

    def visitTypeValue(self, typevalue):
        typevalue.value_type.accept(self)

    def visitObjectClassType(self, objectclasstype):
        myprint(objectclasstype.type_object)

    def visitStringClassType(self, stringclasstype):
        myprint(stringclasstype.type_string)

    def visitIntegralTypeRef(self, integraltyperef):
        integraltyperef.integral_type.accept(self)

    def visitFloatingPointTypeRef(self, floatingpointtyperef):
        floatingpointtyperef.floating_point_type.accept(self)

    def visitBoolType(self, booltype):
        myprint(booltype.bool_type)

    def visitVoidType(self, voidtype):
        myprint(voidtype.void_type)

    def visitIntType(self, inttype):
        myprint(inttype.int_type)

    def visitLongType(self, longtype):
        myprint(longtype.long_type)

    def visitCharType(self, chartype):
        myprint(chartype.char_type)

    def visitFloatType(self, floattype):
        myprint(floattype.float_type)

    def visitDoubleType(self, doubletype):
        myprint(doubletype.double_type)

    def visitDecimalType(self, decimaltype):
        myprint(decimaltype.decimal_type)

    # def visitFuncDeclConcrete(self, funcdecl):
    #     funcdecl.signature.accept(self)
    #     funcdecl.block.accept(self)

    # def visitSignatureConcrete(self, signature):
    #     signature.type.accept(self)
    #     myprint(" ", signature.id, "(")
    #     if signature.param_list != None:
    #         signature.param_list.accept(self)
    #     myprint(")")
        
    def visitSingleParamList(self, singleparamlist):
        singleparamlist.type.accept(self)
        myprint(" ", singleparamlist.id)
    
    def visitCompoundParamList(self, compoundparamlist):
        compoundparamlist.type.accept(self)
        myprint(" ", compoundparamlist.id, ", ")
        compoundparamlist.param_list.accept(self)
    
    def visitSingleStatementList(self, singlestatementlist):
        singlestatementlist.stmt.accept(self)
    
    def visitCompoundStatementList(self, compoundstatementlist):
        compoundstatementlist.stmt.accept(self)
        compoundstatementlist.stmt_list.accept(self)

    def visitStatementDeclaration(self, statementdeclaration):
        statementdeclaration.declaration_stmt.accept(self)
        
    def visitStatementEmbedded(self, statementembedded):
        statementembedded.embedded_stmt.accept(self)
    
    def visitDeclarationStmtConst(self, declarationstmtconst):
        declarationstmtconst.const_declaration.accept(self)
        myprint(";\n")
    
    def visitDeclarationStmtVar(self, declarationstmtvar):
        myprint(blank())
        declarationstmtvar.var_declaration.accept(self)
        myprint(";\n")
    
    def visitLocalConstDeclarationConcrete(self, constdeclaration):
        myprint(blank(), "const ")
        constdeclaration.type.accept(self)
        constdeclaration.const_declarators.accept(self)
    
    def visitSingleConstDeclarators(self, singleconstdeclarators):
        singleconstdeclarators.const_declarator.accept(self)
    
    def visitCompoundConstDeclarators(self, compoundconstdeclarators):
        compoundconstdeclarators.const_declarator.accept(self)
        myprint(",")
        compoundconstdeclarators.const_declarators.accept(self)
    
    def visitConstDeclaratorConcrete(self, constdeclarator):
        myprint(" ", constdeclarator.id)
        myprint(" = ")
        constdeclarator.exp.accept(self)
    
    def visitLocalVarDeclarationConcrete(self, vardeclaration):
        vardeclaration.type.accept(self)
        myprint(" ")
        vardeclaration.var_declarators.accept(self)
    
    def visitSingleVarDeclarators(self, singlevardeclarators):
        singlevardeclarators.var_declarator.accept(self)
    
    def visitCompoundVarDeclarators(self, compoundvardeclarators):
        compoundvardeclarators.var_declarator.accept(self)
        myprint(", ")
        compoundvardeclarators.var_declarators.accept(self)
    
    def visitVarDeclaratorId(self, vardeclaratorid):
        myprint(vardeclaratorid.id)

    def visitVarDeclaratorIdExp(self, vardeclaratoridexp):
        myprint(vardeclaratoridexp.id)
        myprint(" = ")
        vardeclaratoridexp.exp.accept(self)
    
    def visitEmbeddedStmtBlock(self, embeddedstmtblock):
        embeddedstmtblock.block.accept(self)
    
    def visitEmbeddedStmtEmpty(self, embeddedstmtempty):
        embeddedstmtempty.empty_statement.accept(self)
    
    def visitEmbeddedStmtExp(self, embeddedstmtexp):
        embeddedstmtexp.exp_statement.accept(self)
    
    def visitEmbeddedStmtSelection(self, embeddedstmtselection):
        embeddedstmtselection.selection_statement.accept(self)
    
    def visitEmbeddedStmtIteration(self, embeddedstmtiteration):
        embeddedstmtiteration.iteration_statement.accept(self)
    
    def visitEmbeddedStmtJump(self, embeddedstmtjump):
        embeddedstmtjump.jump_statement.accept(self)
    
    def visitBlockStmtConcrete(self, blockstmt):
        global tab
        myprint("\n")
        myprint(blank(), "{\n")
        tab = tab + 4
        if blockstmt.stmt_list != None:
            blockstmt.stmt_list.accept(self)
        tab = tab - 4
        myprint(blank(), "}\n")
    
    def visitEmptyStmtConcrete(self, emptystmt):
        myprint(blank(), ";\n")
    
    def visitExpStmtConcrete(self, expstmt):
        myprint(blank())
        expstmt.statement_exp.accept(self)
        myprint(";\n")
    
    def visitStmtExpInvocation(self, stmtexpinvocation):
        stmtexpinvocation.invocation_exp.accept(self)
    
    def visitStmtExpObjectCreation(self, stmtexpobjectcreation):
        stmtexpobjectcreation.object_creation_exp.accept(self)
    
    def visitStmtExpAssignment(self, stmtexpassignment):
        stmtexpassignment.assignment.accept(self)
    
    def visitStmtExpPostIncrement(self, stmtexppostincrement):
        stmtexppostincrement.post_increment_exp.accept(self)
    
    def visitStmtExpPostDecrement(self, stmtexppostdecrement):
        stmtexppostdecrement.post_decrement_exp.accept(self)
    
    def visitStmtExpPreIncrement(self, stmtexppreincrement):
        stmtexppreincrement.pre_increment_exp.accept(self)
    
    def visitStmtExpPreDecrement(self, stmtexppredecrement):
        stmtexppredecrement.pre_decrement_exp.accept(self)
    
    def visitNoArgsObjectCreation(self, objectcreation):
        myprint("new ")
        objectcreation.type.accept(self)
        myprint("()")
    
    def visitNoArgsWithInitializerObjectCreation(self, objectcreation):
        myprint("new ")
        objectcreation.type.accept(self)
        myprint("()")
        objectcreation.object_initializer.accept(self)
    
    def visitObjectCreation(self, objectcreation):
        myprint("new ")
        objectcreation.type.accept(self)
        myprint("(")
        objectcreation.arg_list.accept(self)
        myprint(")")
    
    def visitWithInitializerObjectCreation(self, objectcreation):
        myprint("new ")
        objectcreation.type.accept(self)
        myprint("(")
        objectcreation.arg_list.accept(self)
        myprint(")")
        objectcreation.object_initializer.accept(self)
    
    def visitObjectInitializerConcrete(self, objectinitializer):
        myprint("{ ")
        objectinitializer.member_initializer_list.accept(self)
        myprint(" }")
    
    def visitSingleMemberInitializerList(self, memberinitializerlist):
        memberinitializerlist.member_initializer.accept(self)
    
    def visitCompoundMemberInitializerList(self, memberinitializerlist):
        memberinitializerlist.member_initializer.accept(self)
        myprint(", ")
        memberinitializerlist.member_initializer_list.accept(self)
    
    def visitMemberInitializerConcrete(self, memberinitializer):
        myprint(memberinitializer.id, " = ")
        memberinitializer.exp.accept(self)
    
    def visitPostIncrementExpConcrete(self, postincrementexp):
        postincrementexp.primary_exp.accept(self)
        myprint("++")
    
    def visitPostDecrementExpConcrete(self, postdecrementexp):
        postdecrementexp.primary_exp.accept(self)
        myprint("--")
    
    def visitPreIncrementExpConcrete(self, preincrementexp):
        myprint("++")
        preincrementexp.unary_exp.accept(self)
    
    def visitPreDecrementExpConcrete(self, predecrementexp):
        myprint("--")
        predecrementexp.unary_exp.accept(self)
    
    def visitSelectionStmtIf(self, selectionstmtif):
        selectionstmtif.if_statement.accept(self)
    
    def visitSelectionStmtSwitch(self, selectionstmtswitch):
        selectionstmtswitch.switch_statement.accept(self)
    
    def visitSimpleIfStmt(self, simpleifstmt):
        myprint(blank(), "if (")
        simpleifstmt.exp.accept(self)
        myprint(")")
        simpleifstmt.block.accept(self)
    
    def visitIfElseStmt(self, ifelsestmt):
        myprint(blank(), "if (")
        ifelsestmt.exp.accept(self)
        myprint(")")
        ifelsestmt.block1.accept(self)
        myprint(blank(), "else")
        ifelsestmt.block2.accept(self)
    
    def visitSwitchStmtConcrete(self, switchstmt):
        global tab
        myprint(blank(), "switch (")
        switchstmt.exp.accept(self)
        myprint(")\n")
        myprint(blank(), "{\n")
        tab = tab + 4
        switchstmt.switch_body.accept(self)
        tab = tab - 4
        myprint(blank(), "}\n")
    
    def visitSimpleSwitchBody(self, simpleswitchbody):
        simpleswitchbody.switch_section.accept(self)
    
    def visitCompoundSwitchBody(self, compoundswitchbody):
        compoundswitchbody.switch_section.accept(self)
        compoundswitchbody.switch_body.accept(self)
    
    def visitSimpleSwitchSection(self, simpleswitchsection):
        simpleswitchsection.switch_label.accept(self)
        simpleswitchsection.stmt_list.accept(self)
    
    def visitCompoundSwitchSection(self, compoundswitchsection):
        compoundswitchsection.switch_label.accept(self)
        compoundswitchsection.switch_section.accept(self)
    
    def visitSwitchLabelCase(self, switchlabelcase):
        myprint(blank(), "case ")
        switchlabelcase.pattern.accept(self)
        myprint(":\n")
        myprint("    ")
    
    def visitSwitchLabelDefault(self, switchlabeldefault):
        myprint(blank(), "default:\n")
        myprint("    ")
    
    def visitPatternRelational(self, pattern):
        pattern.relational_pattern.accept(self)
    
    def visitPatternConstant(self, pattern):
        pattern.constant_pattern.accept(self)
    
    def visitRelationalPatternConcrete(self, pattern):
        pattern.relational_operator.accept(self)
        pattern.constant_exp.accept(self)
    
    def visitRelationalOperatorConcrete(self, relationaloperator):
        myprint(relationaloperator.operator, " ")
    
    def visitConstantExpConcrete(self, constantexp):
        myprint(constantexp.constant_exp)
    
    def visitConstantPatternConcrete(self, pattern):
        myprint(pattern.constant_exp)
    
    def visitIterationStmtWhile(self, iterationstmtwhile):
        iterationstmtwhile.while_statement.accept(self)
    
    def visitIterationStmtDo(self, iterationstmtdo):
        iterationstmtdo.do_statement.accept(self)
    
    def visitIterationStmtFor(self, iterationstmtfor):
        iterationstmtfor.for_statement.accept(self)
    
    def visitIterationStmtForeach(self, iterationstmtforeach):
        iterationstmtforeach.foreach_statement.accept(self)
    
    def visitWhileStmtConcrete(self, whilestmt):
        myprint(blank(), "while (")
        whilestmt.exp.accept(self)
        myprint(")")
        whilestmt.block.accept(self)
    
    def visitDoStmtConcrete(self, dostmt):
        myprint(blank(), "do")
        dostmt.block.accept(self)
        myprint(blank(), "while (")
        dostmt.exp.accept(self)
        myprint(");\n")
    
    def visitForStmtConcrete(self, forstmt):
        myprint(blank(), "for (")
        if forstmt.for_initializer != None:
            forstmt.for_initializer.accept(self)
        myprint("; ")
        if forstmt.for_condition != None:
            forstmt.for_condition.accept(self)
        myprint("; ")
        if forstmt.for_iterator != None:
            forstmt.for_iterator.accept(self)
        myprint(")")
        forstmt.block.accept(self)
    
    def visitSimpleForInitializer(self, simpleforinitializer):
        simpleforinitializer.local_var_declaration.accept(self)
    
    def visitForConditionConcrete(self, forcondition):
        forcondition.exp.accept(self)
    
    def visitForIteratorConcrete(self, foriterator):
        foriterator.stmt_exp_list.accept(self)
    
    def visitSimpleStmtExpList(self, simplestmtexplist):
        simplestmtexplist.exp_stmt.accept(self)
    
    def visitCompoundStmtExpList(self, compoundstmtexplist):
        compoundstmtexplist.exp_stmt.accept(self)
        myprint(", ")
        compoundstmtexplist.stmt_exp_list.accept(self)
    
    def visitForeachStmtConcrete(self, foreachstmt):
        myprint(blank(), "foreach (")
        foreachstmt.type.accept(self)
        myprint(" ", foreachstmt.id, " in ")
        foreachstmt.exp.accept(self)
        myprint(")")
        foreachstmt.block.accept(self)
    
    def visitJumpStmtBreak(self, jumpstmtbreak):
        jumpstmtbreak.break_stmt.accept(self)
    
    def visitJumpStmtContinue(self, jumpstmtcontinue):
        jumpstmtcontinue.continue_stmt.accept(self)
    
    def visitJumpStmtReturn(self, jumpstmtreturn):
        jumpstmtreturn.return_stmt.accept(self)
    
    def visitBreakStmtConcrete(self, breakstmt):
        myprint(blank(), "break;\n")
    
    def visitContinueStmtConcrete(self, continuestmt):
        myprint(blank(), "continue;\n")
    
    def visitReturnStmtConcrete(self, returnstmt):
        myprint(blank(), "return")
        if returnstmt.exp != None:
            myprint(" ")
            returnstmt.exp.accept(self)
        myprint(";\n")
    
    def visitSimpleArgList(self, simplearglist):
        simplearglist.exp.accept(self)
    
    def visitCompoundArgList(self, compoundarglist):
        compoundarglist.exp.accept(self)
        myprint(", ")
        compoundarglist.arg_list.accept(self)
    
    def visitPrimaryExpNoArrayCreation(self, primaryexp):
        primaryexp.no_array_creation_exp.accept(self)
    
    def visitBooleanExp(self, booleanexp):
        myprint(booleanexp.bool_value)
    
    def visitNullExp(self, nullexp):
        myprint(nullexp.null_value)
    
    def visitIntNumExp(self, intnumexp):
        myprint(intnumexp.int_value)
    
    def visitHexNumExp(self, hexnumexp):
        myprint(hexnumexp.hex_value)

    def visitBinNumExp(self, binnumexp):
        myprint(binnumexp.bin_value)
    
    def visitFloatNumExp(self, floatnumexp):
        myprint(floatnumexp.float_value)
    
    def visitDoubleNumExp(self, doublenumexp):
        myprint(doublenumexp.double_value)
    
    def visitDecimalNumExp(self, decimalnumexp):
        myprint(decimalnumexp.decimal_value)
    
    def visitCharExp(self, charexp):
        myprint(charexp.char_literal)
    
    def visitStringExp(self, stringexp):
        myprint(stringexp.string_literal)
    
    def visitIdExp(self, idexp):
        myprint(idexp.id)
    
    def visitPrimaryParenthesizedExp(self, parenthesizedexp):
        parenthesizedexp.parenthesized_exp.accept(self)
    
    def visitParenthesizedExpConcrete(self, parenthesizedexp):
        myprint("(")
        parenthesizedexp.exp.accept(self)
        myprint(")")
    
    def visitPrimaryMemberAccessExp(self, memberaccessexp):
        memberaccessexp.member_access.accept(self)
    
    def visitMemberAccessExpConcrete(self, memberaccessexp):
        memberaccessexp.primary_exp.accept(self)
        myprint(".")
        myprint(memberaccessexp.id)
    
    def visitPrimaryInvocationExp(self, invocationexp):
        invocationexp.invocation_exp.accept(self)
    
    def visitInvocationExpConcrete(self, invocationexp):
        invocationexp.primary_exp.accept(self)
        myprint("(")
        if invocationexp.arg_list != None:
            invocationexp.arg_list.accept(self)
        myprint(")")
    
    # def visitPrimaryElementAccessExp(self, elementaccessexp):
    #     elementaccessexp.element_access.accept(self)
    
    # def visitElementAccessExpConcrete(self, elementaccessexp):
    #     elementaccessexp.no_array_creation_exp.accept(self)
    #     myprint("[")
    #     elementaccessexp.exp.accept(self)
    #     myprint("]")
    
    def visitThisExp(self, thisexp):
        myprint("this")
    
    def visitPrimaryPostIncrementExp(self, postincrementexp):
        postincrementexp.post_increment_exp.accept(self)
    
    def visitPrimaryPostDecrementExp(self, postdecrementexp):
        postdecrementexp.post_decrement_exp.accept(self)
    
    def visitPrimaryObjectCreationExp(self, objectcreationexp):
        objectcreationexp.object_creation_exp.accept(self)
    
    def visitUnaryPrimaryExp(self, unaryprimaryexp):
        unaryprimaryexp.primary_exp.accept(self)
    
    def visitUnaryPreIncrementExp(self, unarypreincrementexp):
        unarypreincrementexp.pre_increment_exp.accept(self)

    def visitUnaryPreDecrementExp(self, unarypredecrementexp):
        unarypredecrementexp.pre_decrement_exp.accept(self)

    def visitUnaryCastExp(self, unarycastexp):
        unarycastexp.cast_exp.accept(self)

    def visitCastExpConcrete(self, castexp):
        myprint("(")
        castexp.type.accept(self)
        myprint(") ")
        castexp.unary_exp.accept(self)

    def visitUnaryMinusExp(self, unaryminusexp):
        unaryminusexp.minus_exp.accept(self)

    def visitMinusExpConcrete(self, minusexp):
        myprint("-")
        minusexp.unary_exp.accept(self)

    def visitUnaryPlusExp(self, unaryplusexp):
        unaryplusexp.plus_exp.accept(self)

    def visitPlusExpConcrete(self, plusexp):
        myprint("+")
        plusexp.unary_exp.accept(self)
    
    def visitExpNonAssignment(self, expnonassignment):
        expnonassignment.non_assignment_exp.accept(self)

    def visitExpAssignment(self, expassignment):
        expassignment.assignment.accept(self)
    
    def visitNonAssignmentConditionalExp(self, conditionalexp):
        conditionalexp.conditional_exp.accept(self)

    def visitTernaryExp(self, ternaryexp):
        ternaryexp.conditional_or_exp.accept(self)
        myprint(" ? ")
        ternaryexp.exp1.accept(self)
        myprint(" : ")
        ternaryexp.exp2.accept(self)

    def visitConditionalExpNext(self, conditionalexpnext):
        conditionalexpnext.conditional_or_exp.accept(self)

    def visitConditionalOrExpConcrete(self, conditionalorexp):
        conditionalorexp.conditional_or_exp.accept(self)
        myprint(" || ")
        conditionalorexp.conditional_and_exp.accept(self)

    def visitConditionalOrExpNext(self, conditionalorexpnext):
        conditionalorexpnext.conditional_and_exp.accept(self)

    def visitConditionalAndExpConcrete(self, conditionalandexp):
        conditionalandexp.conditional_and_exp.accept(self)
        myprint(" && ")
        conditionalandexp.inclusive_or_exp.accept(self)

    def visitConditionalAndExpNext(self, conditionalandexpnext):
        conditionalandexpnext.inclusive_or_exp.accept(self)
    
    def visitInclusiveOrExpConcrete(self, inclusiveorexp):
        inclusiveorexp.inclusive_or_exp.accept(self)
        myprint(" | ")
        inclusiveorexp.exclusive_or_exp.accept(self)

    def visitInclusiveOrExpNext(self, inclusiveorexpnext):
        inclusiveorexpnext.exclusive_or_exp.accept(self)

    def visitExclusiveOrExpConcrete(self, exclusiveorexp):
        exclusiveorexp.exclusive_or_exp.accept(self)
        myprint(" ^ ")
        exclusiveorexp.and_exp.accept(self)

    def visitExclusiveOrExpNext(self, exclusiveorexpnext):
        exclusiveorexpnext.and_exp.accept(self)
    
    def visitAndExpConcrete(self, andexp):
        andexp.and_exp.accept(self)
        myprint(" & ")
        andexp.equality_exp.accept(self)

    def visitAndExpNext(self, andexpnext):
        andexpnext.equality_exp.accept(self)

    def visitEqualExp(self, equalexp):
        equalexp.equality_exp.accept(self)
        myprint(" == ")
        equalexp.relational_exp.accept(self)

    def visitNotEqualExp(self, notequalexp):
        notequalexp.equality_exp.accept(self)
        myprint(" != ")
        notequalexp.relational_exp.accept(self)

    def visitEqualityExpNext(self, equalityexpnext):
        equalityexpnext.relational_exp.accept(self)

    def visitLessExp(self, lessexp):
        lessexp.relational_exp.accept(self)
        myprint(" < ")
        lessexp.shift_exp.accept(self)

    def visitGreaterExp(self, greaterexp):
        greaterexp.relational_exp.accept(self)
        myprint(" > ")
        greaterexp.shift_exp.accept(self)

    def visitLessEqualExp(self, lessequalexp):
        lessequalexp.relational_exp.accept(self)
        myprint(" <= ")
        lessequalexp.shift_exp.accept(self)

    def visitGreaterEqualExp(self, greaterequalexp):
        greaterequalexp.relational_exp.accept(self)
        myprint(" >= ")
        greaterequalexp.shift_exp.accept(self)

    def visitIsTypeExp(self, istypeexp):
        istypeexp.relational_exp.accept(self)
        myprint(" is ")
        istypeexp.type.accept(self)
    
    def visitRelationalExpNext(self, relationalexpnext):
        relationalexpnext.shift_exp.accept(self)
    
    def visitLeftShiftExp(self, leftshiftexp):
        leftshiftexp.shift_exp.accept(self)
        myprint(" << ")
        leftshiftexp.additive_exp.accept(self)

    def visitRightShiftExp(self, rightshiftexp):
        rightshiftexp.shift_exp.accept(self)
        myprint(" >> ")
        rightshiftexp.additive_exp.accept(self)

    def visitShiftExpNext(self, shiftexpnext):
        shiftexpnext.additive_exp.accept(self)

    def visitSumExp(self, sumexp):
        sumexp.additive_exp.accept(self)
        myprint(" + ")
        sumexp.multiplicative_exp.accept(self)

    def visitSubExp(self, subexp):
        subexp.additive_exp.accept(self)
        myprint(" - ")
        subexp.multiplicative_exp.accept(self)

    def visitAdditiveExpNext(self, additiveexpnext):
        additiveexpnext.multiplicative_exp.accept(self)

    def visitMultExp(self, multexp):
        multexp.multiplicative_exp.accept(self)
        myprint(" * ")
        multexp.unary_exp.accept(self)

    def visitDivExp(self, divexp):
        divexp.multiplicative_exp.accept(self)
        myprint(" / ")
        divexp.unary_exp.accept(self)

    def visitModExp(self, modexp):
        modexp.multiplicative_exp.accept(self)
        myprint(" % ")
        modexp.unary_exp.accept(self)

    def visitMultiplicativeExpNext(self, multiplicativeexpnext):
        multiplicativeexpnext.unary_exp.accept(self)
    
    def visitAssignExp(self, assignexp):
        assignexp.unary_exp.accept(self)
        myprint(" = ") # Por enquanto atribuição simples apenas
        assignexp.exp.accept(self)


def main():
    f = open("teste_parser.cs", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print(">>> Programa passado como entrada:")
    visitor = Visitor()
    for r in result:
        r.accept(visitor)


if __name__ == "__main__":
    main()

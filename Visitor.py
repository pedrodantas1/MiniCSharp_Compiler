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

    def visitFuncDeclConcrete(self, funcdecl):
        funcdecl.signature.accept(self)
        funcdecl.block.accept(self)

    def visitSignatureConcrete(self, signature):
        signature.type.accept(self)
        myprint(" ", signature.id, "(")
        if signature.param_list != None:
            signature.param_list.accept(self)
        myprint(")")
        
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
        myprint(";")
    
    def visitvisitDeclarationStmtVar(self, declarationstmtvar):
        declarationstmtvar.var_declaration.accept(self)
        myprint(";")
    
    def visitConstDeclarationConcrete(self, constdeclaration):
        myprint(blank(), "const ")
        constdeclaration.type.accept(self)
        constdeclaration.const_declarators.accept(self)
    
    def visitSingleConstDeclarators(self, singleconstdeclarators):
        singleconstdeclarators.const_declarator.accept(self)
    
    def visitCompoundConstDeclarators(self, compoundconstdeclarators):
        compoundconstdeclarators.const_declarator.accept(self)
        myprint(", ")
        compoundconstdeclarators.const_declarators.accept(self)
    
    def visitConstDeclaratorConcrete(self, constdeclarator):
        myprint(" ", constdeclarator.id)
        myprint(" = ")
        constdeclarator.exp.accept(self)
    
    def visitVarDeclarationConcrete(self, vardeclaration):
        vardeclaration.type.accept(self)
        vardeclaration.var_declarators(self)
    
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
        myprint("{ ")
        tab = tab + 4
        if blockstmt.stmt_list != None:
            blockstmt.stmt_list.accept(self)
        tab = tab - 4
        myprint(blank(), "} ")
    
    def visitEmptyStmtConcrete(self, emptystmt):
        myprint(";")
    
    def visitExpStmtConcrete(self, expstmt):
        expstmt.statement_exp.accept(self)
        myprint(";")
    
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
        myprint(blank(), "new ")
        objectcreation.type.accept(self)
        myprint(" ()")
    
    def visitNoArgsWithInitializerObjectCreation(self, objectcreation):
        myprint(blank(), "new ")
        objectcreation.type.accept(self)
        myprint(" ()")
        objectcreation.object_initializer.accept(self)
    
    def visitObjectCreation(self, objectcreation):
        myprint(blank(), "new ")
        objectcreation.type.accept(self)
        myprint(" (")
        objectcreation.arg_list.accept(self)
        myprint(")")
    
    def visitWithInitializerObjectCreation(self, objectcreation):
        myprint(blank(), "new ")
        objectcreation.type.accept(self)
        myprint(" (")
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
        myprint("else")
        ifelsestmt.block2.accept(self)
    
    def visitSwitchStmtConcrete(self, switchstmt):
        global tab
        myprint(blank(), "switch (")
        switchstmt.exp.accept(self)
        myprint(")\n")
        myprint(blank(), "{")
        tab = tab + 4
        switchstmt.switch_body.accept(self)
        tab = tab - 4
        myprint(blank(), "}")
    
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
        myprint(" :\n")
    
    def visitSwitchLabelDefault(self, switchlabeldefault):
        myprint(blank(), "default :\n")
    
    def visitPatternConcrete(self, pattern):
        pattern.exp.accept(self)
    
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
        myprint("while (")
        dostmt.exp.accept(self)
        myprint(");")
    
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

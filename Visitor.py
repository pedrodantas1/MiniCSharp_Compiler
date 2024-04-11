from functools import partial

from AbstractVisitor import AbstractVisitor
from LanguageParser import *

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
        myprint(signature.id, "(")
        if signature.param_list != None:
            signature.param_list.accept(self)
        myprint(")")

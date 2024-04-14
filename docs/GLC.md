# GLC da linguagem de programação Mini C#
```
type -> class_type |
        value_type

class_type -> OBJECT | 
              STRING

value_type -> integral_type |
              floating_point_type |
              BOOL |
              VOID

integral_type -> INT | LONG | CHAR

floating_point_type -> FLOAT | DOUBLE | DECIMAL

program -> class_declaration |
           class_declaration program

param_list -> type ID |
              type ID ',' param_list

statement_list -> statement |
                  statement statement_list

statement -> declaration_statement |
             embedded_statement

declaration_statement -> local_const_declaration ';' |
                         local_var_declaration ';'

local_const_declaration -> CONST type const_declarators

const_declarators -> const_declarator |
                     const_declarator ',' const_declarators

const_declarator -> ID '=' exp

local_var_declaration -> type var_declarators

var_declarators -> var_declarator |
                   var_declarator ',' var_declarators

var_declarator -> ID |
                  ID '=' exp

embedded_statement -> block |
                      empty_statement |
                      exp_statement |
                      selection_statement |
                      iteration_statement |
                      jump_statement

block -> '{' statement_list '}' |
         '{' '}'

empty_statement -> ';'

exp_statement -> statement_exp ';'

statement_exp -> invocation_exp |
                 object_creation_exp |
                 assignment |
                 post_increment_exp |
                 post_decrement_exp |
                 pre_increment_exp |
                 pre_decrement_exp

object_creation_exp -> NEW type '(' ')' |
                       NEW type '(' ')' object_initializer |
                       NEW type '(' arg_list ')' |
                       NEW type '(' arg_list ')' object_initializer

object_initializer -> '{' member_initializer_list '}'

member_initializer_list -> member_initializer |
                           member_initializer ',' member_initializer_list

member_initializer -> ID '=' exp

post_increment_exp -> primary_exp '++'

post_decrement_exp -> primary_exp '--'

pre_increment_exp -> '++' unary_exp

pre_decrement_exp -> '--' unary_exp

selection_statement -> if_statement |
                       switch_statement

if_statement -> IF '(' exp ')' block |
                IF '(' exp ')' block ELSE block

switch_statement -> SWITCH '(' exp ')' '{' switch_body '}'

switch_body -> switch_section |
               switch_section switch_body

switch_section -> switch_label statement_list |
                  switch_label switch_section

switch_label -> CASE pattern ':' |
                DEFAULT ':'

pattern -> relational_pattern |
           constant_pattern

relational_pattern -> relational_operator constant_exp

relational_operator -> '<' | '>' | '<=' | '>='

constant_exp -> INTNUM | FLOATNUM | CHARLITERAL

constant_pattern -> INTNUM | FLOATNUM | CHARLITERAL | STRINGLITERAL | TRUE | FALSE | NULL

iteration_statement -> while_statement |
                       do_statement |
                       for_statement |
                       foreach_statement

while_statement -> WHILE '(' exp ')' block

do_statement -> DO block WHILE '(' exp ')' ';'

for_statement -> FOR '(' for_initializer ';' for_condition ';' for_iterator ')' block |
                 FOR '(' for_initializer ';' for_condition ';' ')' block |
                 FOR '(' for_initializer ';' ';' for_iterator ')' block |
                 FOR '(' for_initializer ';' ';' ')' block |
                 FOR '(' ';' for_condition ';' for_iterator ')' block |
                 FOR '(' ';' for_condition ';' ')' block |
                 FOR '(' ';' ';' for_iterator ')' block |
                 FOR '(' ';' ';' ')' block

for_initializer -> local_var_declaration

for_condition -> exp

for_iterator -> statement_exp_list

statement_exp_list -> statement_exp |
                      statement_exp ',' statement_exp_list

foreach_statement -> FOREACH '(' type ID IN exp ')' block

jump_statement -> break_statement |
                  continue_statement |
                  return_statement

break_statement -> BREAK ';'

continue_statement -> CONTINUE ';'

return_statement -> RETURN ';' |
                    RETURN exp ';'

arg_list -> exp |
            exp ',' arg_list

primary_exp -> primary_no_array_creation_exp

primary_no_array_creation_exp -> TRUE | FALSE | NULL
                                 INTNUM | HEXADECIMALNUM| BINARYNUM | 
                                 FLOATNUM | DOUBLENUM | DECIMALNUM |
                                 CHARLITERAL | STRINGLITERAL |
                                 ID |
                                 parenthesized_exp |
                                 member_access |
                                 invocation_exp |
                                 THIS |
                                 post_increment_exp |
                                 post_decrement_exp |
                                 object_creation_exp |

parenthesized_exp -> '(' exp ')'

member_access -> primary_exp '.' ID

invocation_exp -> primary_exp '(' ')' |
                  primary_exp '(' arg_list ')'

unary_exp -> primary_exp |
             pre_increment_exp |
             pre_decrement_exp |
             cast_exp |
             minus_exp |
             plus_exp

cast_exp -> '(' type ')' unary_exp

minus_exp -> '-' unary_exp

plus_exp -> '+' unary_exp

exp -> non_assignment_exp |
       assignment

non_assignment_exp -> conditional_exp

conditional_exp -> conditional_or_exp '?' exp ':' exp |
                   conditional_or_exp

conditional_or_exp -> conditional_or_exp '||' conditional_and_exp |
                      conditional_and_exp

conditional_and_exp -> conditional_and_exp '&&' inclusive_or_exp |
                       inclusive_or_exp

inclusive_or_exp -> inclusive_or_exp '|' exclusive_or_exp |
                    exclusive_or_exp

exclusive_or_exp -> exclusive_or_exp '^' and_exp |
                    and_exp

and_exp -> and_exp '&' equality_exp |
           equality_exp

equality_exp -> equality_exp '==' relational_exp |
                equality_exp '!=' relational_exp |
                relational_exp

relational_exp -> relational_exp '<' shift_exp |
                  relational_exp '>' shift_exp |
                  relational_exp '<=' shift_exp |
                  relational_exp '>=' shift_exp |
                  relational_exp 'is' type |
                  shift_exp

shift_exp -> shift_exp '<<' additive_exp |
             shift_exp '>>' additive_exp |
             additive_exp

additive_exp -> additive_exp '+' multiplicative_exp |
                additive_exp '-' multiplicative_exp |
                multiplicative_exp

multiplicative_exp -> multiplicative_exp '*' unary_exp |
                      multiplicative_exp '/' unary_exp |
                      multiplicative_exp '%' unary_exp |
                      unary_exp

assignment -> unary_exp '=' exp

class_declaration -> modifiers CLASS ID class_body |
                     CLASS ID class_body

class_body -> '{' class_member_list '}' |
              '{' '}'

class_member_list -> class_member_decl |
                     class_member_decl class_member_list

class_member_decl -> constant_declaration |
                     field_declaration |
                     method_declaration |
                     constructor_declaration

constant_declaration -> modifiers CONST type const_declarators ';' |
                        CONST type const_declarators ';'

field_declaration -> modifiers_list type var_declarators ';' |
                     type var_declarators ';'

method_declaration -> modifiers_list type method_head block |
                      type method_head block

method_head -> ID '(' param_list ')' |
               ID '(' ')'

constructor_declaration -> modifiers constructor_head block |
                           constructor_head block

constructor_head -> ID '(' param_list ')' |
                    ID '(' ')'

modifiers -> NEW | PUBLIC | PROTECTED | PRIVATE | STATIC

modifiers_list -> modifiers |
                  modifiers modifiers_list

```
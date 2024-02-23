# GLC da linguagem de programação Mini C#
```
type_name -> ID |
             type_name '.' ID

type -> reference_type | 
        value_type

reference_type -> class_type | 
                  interface_type |
                  <!-- array_type -->

class_type -> type_name |
              OBJECT | 
              STRING

interface_type -> type_name

value_type -> struct_type

struct_type -> type_name |
               simple_type | 
               tuple_type

simple_type -> numeric_type |
               BOOL

numeric_type -> integral_type | 
                floating_point_type

integral_type -> SHORT | USHORT | INT | UINT | LONG | ULONG | CHAR

floating_point_type -> FLOAT | DOUBLE | DECIMAL

tuple_type -> '(' tuple_type_part ')'

tuple_type_part -> tuple_type_element tuple_type_final

tuple_type_element -> type |
                      type ID

tuple_type_final -> ',' tuple_type_element |
                    ',' tuple_type_element tuple_type_final

program -> func_declaration |
           func_declaration program

func_declaration -> signature block

signature -> ID ID '(' param_list ')' |
             ID ID '(' ')'

param_list -> ID ID |
              ID ID ',' param_list

statement -> declaration_statement |
             embedded_statement

statement_list -> statement |
                  statement statement_list

declaration_statement -> const_declaration ';' |
                         var_declaration ';'

const_declaration -> CONST type const_declarators

const_declarators -> constant_declarator |
                     constant_declarator ',' constant_declarators

constant_declarator -> ID '=' exp

var_declaration -> type var_declarators

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
                 post_decrement_expression |
                 pre_increment_expression |
                 pre_decrement_expression

object_creation_exp -> NEW type '(' ')' |
                       NEW type '(' arg_list ')' |
                       NEW type '(' ')' object_initializer
                       NEW type '(' arg_list ')' object_initializer

object_initializer -> '{' '}' |
                      '{' member_initializer_list '}'

member_initializer_list -> member_initializer |
                           member_initializer ',' member_initializer_list

member_initializer -> ID '=' exp

post_increment_exp -> primary_exp '++'

post_decrement_exp -> primary_exp '--'

pre_increment_expression -> '++' unary_exp

pre_decrement_expression -> '--' unary_exp

selection_statement -> if_statement |
                       switch_statement

if_statement -> IF '(' exp ')' embedded_statement |
                IF '(' exp ')' embedded_statement ELSE embedded_statement

switch_statement -> SWITCH '(' exp ')' switch_block

switch_block -> '{' switch_body '}'

switch_body -> switch_section |
               switch_section switch_body

switch_section -> switch_label statement_list |
                  switch_label switch_section

switch_label -> CASE pattern ':' | 
                DEFAULT ':'

<!-- Talvez precise retirar o switch -->
pattern -> exp

iteration_statement -> while_statement |
                       do_statement |
                       for_statement |
                       foreach_statement

while_statement -> WHILE '(' exp ')' embedded_statement

do_statement -> DO embedded_statement WHILE '(' exp ')' ';'

for_statement -> FOR '(' for_initializer ';' for_condition ';' for_iterator ')' embedded_statement |
                 FOR '(' for_initializer ';' for_condition ';' ')' embedded_statement |
                 FOR '(' for_initializer ';' ';' for_iterator ')' embedded_statement |
                 FOR '(' for_initializer ';' ';' ')' embedded_statement |
                 FOR '(' ';' for_condition ';' for_iterator ')' embedded_statement |
                 FOR '(' ';' for_condition ';' ')' embedded_statement |
                 FOR '(' ';' ';' for_iterator ')' embedded_statement |
                 FOR '(' ';' ';' ')' embedded_statement

for_initializer -> var_declaration |
                   statement_exp_list

for_condition -> exp

for_iterator -> statement_exp_list

statement_exp_list -> statement_exp |
                      statement_exp ',' statement_exp_list

foreach_statement -> FOREACH '(' type ID IN exp ')' embedded_statement

jump_statement -> break_statement |
                  continue_statement |
                  return_statement

break_statement -> BREAK ';'

continue_statement -> CONTINUE ';'

return_statement -> RETURN ';' |
                    RETURN exp ';'

arg_list -> argument |
            argument ',' arg_list

argument -> exp

primary_exp -> TRUE | FALSE | NULL
               INTNUM | HEXADECIMALNUM| BINARYNUM | 
               FLOATNUM | DOUBLENUM | DECIMALNUM |
               CHARLITERAL | STRINGLITERAL |
               ID |
               parenthesized_exp |
               tuple_exp |
               <!-- member_access |  -->
               <!-- null_conditional_member_access | -->
               invocation_exp |
               <!-- element_access --> |
               THIS |
               post_increment_exp |
               post_decrement_exp |
               object_creation_exp |
               typeof_exp |
               <!-- sizeof_exp | -->
               default_exp

parenthesized_exp -> '(' exp ')'

tuple_exp -> '(' tuple_part ')'

tuple_part -> tuple_element tuple_final_part

tuple_final_part -> ',' tuple_element |
                    ',' tuple_element tuple_final_part

tuple_element -> exp |
                 ID ':' exp

invocation_exp -> primary_exp '(' ')' |
                  primary_exp '(' arg_list ')'

typeof_exp -> TYPEOF '(' type ')'

default_exp -> DEFAULT |
               DEFAULT '(' type ')'

unary_exp -> primary_exp |
             '+' unary_exp |
             '-' unary_exp |
             '!' unary_exp |
             '~' unary_exp |
             pre_increment_exp |
             pre_decrement_exp |
             cast_exp

cast_exp -> '(' type ')' unary_exp

conditional_exp -> null_coalescing_exp |
                   null_coalescing_exp '?' exp ':' exp

null_coalescing_exp -> conditional_or_exp |
                       conditional_or_exp '??' null_coalescing_exp

conditional_or_exp -> conditional_and_exp |
                      conditional_or_exp '||' conditional_and_expr

conditional_and_exp -> inclusive_or_exp |
                       conditional_and_exp '&&' inclusive_or_exp

inclusive_or_exp -> exclusive_or_exp |
                    inclusive_or_exp '|' exclusive_or_exp

exclusive_or_exp -> and_exp |
                    exclusive_or_exp '^' and_exp

and_exp -> equality_exp |
           and_exp '&' equality_exp

equality_exp -> relational_exp |
                equality_exp '==' relational_exp |
                equality_exp '!=' relational_exp

relational_exp -> shift_expression |
                  relational_exp '<' shift_exp |
                  relational_exp '>' shift_exp |
                  relational_exp '<=' shift_exp |
                  relational_exp '>=' shift_exp |
                  relational_exp 'is' type

shift_expression -> additive_exp |
                    shift_exp '<<' additive_exp |
                    shift_exp '>>' additive_exp

additive_exp -> multiplicative_exp |
                additive_exp '+' multiplicative_exp |
                additive_exp '-' multiplicative_exp

multiplicative_exp -> unary_exp |
                      multiplicative_exp '*' unary_exp |
                      multiplicative_exp '/' unary_exp |
                      multiplicative_exp '%' unary_exp

exp -> non_assignment_exp |
       assignment

non_assignment_exp -> declaration_exp |
                      conditional_exp

declaration_exp -> type ID

assignment -> unary_exp assignment_operator exp

assignment_operator -> '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '&=' |
                       '|=' | '^=' | '<<=' | '>>='


             



```
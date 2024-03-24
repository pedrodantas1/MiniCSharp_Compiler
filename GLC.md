# GLC da linguagem de programação Mini C#
```
type_name -> ID |
             type_name '.' ID

type -> class_type | 
        interface_type |
        array_type |
        value_type

class_type -> type_name |
              OBJECT | 
              STRING

interface_type -> type_name

@
array_type -> non_array_type rank_specifiers

@
non_array_type -> value_type |
                  class_type |
                  interface_type

@
rank_specifier -> '[' ']'

@
rank_specifiers -> rank_specifier |
                   rank_specifier rank_specifiers

value_type -> integral_type |
              floating_point_type |
              BOOL

integral_type -> INT | LONG | CHAR

floating_point_type -> FLOAT | DOUBLE | DECIMAL

program -> func_declaration |
           func_declaration program

func_declaration -> signature block

signature -> type ID '(' param_list ')' |
             type ID '(' ')'

param_list -> type ID |
              type ID ',' param_list

statement_list -> statement |
                  statement statement_list

statement -> declaration_statement |
             embedded_statement

declaration_statement -> const_declaration ';' |
                         var_declaration ';'

const_declaration -> CONST type const_declarators

const_declarators -> const_declarator |
                     const_declarator ',' const_declarators

const_declarator -> ID '=' exp

var_declaration -> type var_declarators

var_declarators -> var_declarator |
                   var_declarator ',' var_declarators

var_declarator -> ID |
                  ID '=' exp |
                  ID '=' array_initializer

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

object_initializer -> '{' '}' |
                      '{' member_initializer_list '}'

member_initializer_list -> member_initializer |
                           member_initializer ',' member_initializer_list

member_initializer -> ID '=' exp

post_increment_exp -> primary_exp '++'

post_decrement_exp -> primary_exp '--'

pre_increment_exp -> '++' unary_exp

pre_decrement_exp -> '--' unary_exp

selection_statement -> if_statement |
                       switch_statement

if_statement -> IF '(' exp ')' embedded_statement |
                IF '(' exp ')' embedded_statement ELSE embedded_statement

switch_statement -> SWITCH '(' exp ')' '{' switch_body '}'

<!-- switch_block -> '{' switch_body '}' -->

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
                   var_declaration ',' for_initializer

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

arg_list -> exp |
            exp ',' arg_list

primary_exp -> primary_no_array_creation_exp |
               array_creation_exp

primary_no_array_creation_exp -> TRUE | FALSE | NULL
                                 INTNUM | HEXADECIMALNUM| BINARYNUM | 
                                 FLOATNUM | DOUBLENUM | DECIMALNUM |
                                 CHARLITERAL | STRINGLITERAL |
                                 ID |
                                 parenthesized_exp |
                                 member_access |
                                 invocation_exp |
                                 element_access |
                                 THIS |
                                 post_increment_exp |
                                 post_decrement_exp |
                                 object_creation_exp |
                                 typeof_exp |
                                 sizeof_exp |
                                 default_exp

parenthesized_exp -> '(' exp ')'

member_access -> primary_exp '.' ID

invocation_exp -> primary_exp '(' ')' |
                  primary_exp '(' arg_list ')'

element_access -> primary_no_array_creation_exp '[' exp ']'

typeof_exp -> TYPEOF '(' type ')'

sizeof_exp -> SIZEOF '(' value_type ')'

default_exp -> DEFAULT '(' type ')'

exp_list -> exp |
            exp_list ',' exp

@
array_creation_exp -> NEW non_array_type '[' exp_list ']' |
                      NEW non_array_type '[' exp_list ']' rank_specifiers |
                      NEW non_array_type '[' exp_list ']' array_initializer |
                      NEW non_array_type '[' exp_list ']' rank_specifiers array_initializer

@
array_initializer -> '{' variable_initializer_list '}'

@
variable_initializer_list -> variable_initializer |
                             variable_initializer ',' variable_initializer_list

@
variable_initializer -> exp |
                        array_initializer

unary_exp -> primary_exp |
             pre_increment_exp |
             pre_decrement_exp |
             cast_exp

cast_exp -> '(' type ')' unary_exp

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

exp -> non_assignment_exp |
       assignment

non_assignment_exp -> declaration_exp |
                      conditional_exp

declaration_exp -> type ID

assignment -> unary_exp assignment_operator exp

assignment_operator -> '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '&=' |
                       '|=' | '^=' | '<<=' | '>>='
```
# GLC da linguagem de programação Mini C#
```
program -> func_declaration |
           func_declaration program

func_declaration -> signature block

signature -> ID ID '(' param_list ')' |
             ID ID '(' ')'

param_list -> ID ID |
              ID ID ',' param_list

statement -> declaration_statement |
             embedded_statement

declaration_statement -> const_declaration ';' |
                         var_declaration ';'

embedded_statement -> block |
                      empty_statement |
                      exp_statement |
                      selection_statement |
                      iteration_statement |



const_declaration -> CONST ID const_declarators

const_declarators -> constant_declarator |
                     constant_declarator ',' constant_declarators

constant_declarator -> ID '=' exp

var_declaration -> ID var_declarators

var_declarators -> var_declarator |
                   var_declarator ',' var_declarators

var_declarator -> ID |
                  ID '=' exp

block -> '{' statement_list '}' |
         '{' '}'

statement_list -> statement |
                  statement statement_list

empty_statement -> ';'

exp_statement -> statement_exp ';'

statement_exp -> invocation_exp |
                 object_creation_exp |
                 assignment |
                 post_increment_exp |
                 post_decrement_expression |
                 pre_increment_expression |
                 pre_decrement_expression

<!-- Source: §12.8.16.2 -->
object_creation_exp -> NEW ID '(' ')' |
                       NEW ID '(' arg_list ')' |
                       NEW ID '(' ')' object_initializer
                       NEW ID '(' arg_list ')' object_initializer

object_initializer -> '{' '}' |
                      '{' member_initializer_list '}' |
                      '{' member_initializer_list ',' '}'

member_initializer_list -> member_initializer |
                           member_initializer ',' member_initializer_list

member_initializer -> initializer_target '=' initializer_value

initializer_target -> ID | 
                      '[' arg_list ']'

initializer_value -> expression | 
                     object_initializer

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

for_statement -> FOR '(' for_initializer ';' for_condition? ';' for_iterator? ')' embedded_statement

for_initializer -> var_declaration |
                   statement_exp_list


primary_exp -> TRUE | FALSE | NULL
               INTNUM | FLOATNUM | DOUBLENUM | DECIMALNUM |
               CHARLITERAL | STRINGLITERAL |
               parenthesized_exp |
               tuple_exp |
               <!-- member_access |  -->
               <!-- null_conditional_member_access | -->
               invocation_exp |
               >> continuar e analisar oq colocar

parenthesized_exp -> '(' exp ')'

tuple_exp -> '(' tuple_part ')'

tuple_part -> tuple_element tuple_final_part

tuple_final_part -> ',' tuple_element |
                    ',' tuple_element tuple_final_part

tuple_element -> exp |
                 ID ':' exp

<!-- ID no lugar de primary_exp -->
invocation_exp -> primary_exp '(' ')' |
                  primary_exp '(' arg_list ')'

arg_list -> argument |
            argument ',' arg_list

argument -> exp  <!-- talvez mude -->









exp -> non_assignment_exp |
       assignment

non_assignment_exp -> declaration_exp

declaration_exp -> ID ID  <!-- tipo + identificador -->

assignment -> ID assignment_operator exp

assignment_operator -> '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '&=' |
                       '|=' | '^=' | '<<=' | '>>='

<!-- talvez remover primary_exp -->
unary_exp -> primary_exp |
             



```
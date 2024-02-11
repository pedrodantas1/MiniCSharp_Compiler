# GLC da linguagem de programação Mini C#
```
program -> func_declaration |
           func_declaration program

func_declaration -> signature body

signature -> ID ID '(' param_list ')' |
             ID ID '(' ')'

param_list -> ID ID |
              ID ID ',' param_list

body -> '{' statement_list '}' |
        '{' '}'     <!-- função vazia -->

statement_list -> statement |
                  statement statement_list

statement -> const_declaration ';' |
             var_declaration ';' |
             >> continuar

const_declaration -> CONST ID const_declarators

const_declarators -> constant_declarator |
                     constant_declarator ',' constant_declarators

constant_declarator -> ID '=' expression

var_declaration -> ID var_declarators

var_declarators -> var_declarator |
                   var_declarator ',' var_declarators

var_declarator -> ID |
                  ID '=' expression

expression -> TRUE | FALSE | NULL
              INTNUM | FLOATNUM | DOUBLENUM | DECIMALNUM |
              CHARLITERAL | STRINGLITERAL |
              parenthesized_expression |
              tuple_expression


parenthesized_expression -> '(' expression ')'

tuple_expression -> '(' tuple_part ')'

tuple_part -> tuple_element ',' tuple_element |
              tuple_element ',' tuple_element



```
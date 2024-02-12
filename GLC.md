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

constant_declarator -> ID '=' exp

var_declaration -> ID var_declarators

var_declarators -> var_declarator |
                   var_declarator ',' var_declarators

var_declarator -> ID |
                  ID '=' exp

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

assignment_operator -> EQUAL | PLUSEQUAL | MINUSEQUAL | STAREQUAL |
                       SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | PIPEEQUAL |
                       CIRCUMEQUAL | LSHIFTEQUAL | RSHIFTEQUAL


<!-- talvez remover primary_exp -->
unary_exp -> primary_exp |
             



```
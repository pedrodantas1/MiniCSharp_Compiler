# Documentação Sintática da Linguagem Mini C#

# 1. Elementos Sintáticos

Um programa em Mini C# é composto por uma ou mais classes. Uma classe apresenta é representada pelas seguinte produções:
``` 
class_declaration -> modifiers CLASS ID class_body |
                     CLASS ID class_body
```
Onde o modifiers se refere aos modificadores de acessibilidade, o ID se refere ao nome da classe e class_body representa o corpo da função. Na próximo seção será apresentada os comandos da linguagem Mini C#.


## 1.1 Comandos da Linguagem Mini C#

Com relação aos comandos aceitos, Mini C# lida apenas com os principais comando existentes na linguagem C#, conforme apresentado nas seguintes regras:

```
statement -> declaration_statement |
             embedded_statement

declaration_statement -> local_const_declaration ';' |
                         local_var_declaration ';'

embedded_statement -> block |
                      empty_statement |
                      exp_statement |
                      selection_statement |
                      iteration_statement |
                      jump_statement
```

## 1.2 Expressões em Mini C#
Mini C# dá suporte a expressões aritméticas de soma, subtração multiplicação, divisão e módulo. Também dá suporte operações bit a bit, operações de shift, operações lógicas binárias e condicional ternária. A sintaxe das expressões em Mini C# é apresentada pelas seguinte regras:

```
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
```

### 1.2.1 Expressões Primárias

Mini C# dá suporte a expressões primárias, como chamadas a métodos e expressões dentro de parênteses, como mostrado a seguir:

```
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
```


# 2. Exemplos de Código.

A seguir, alguns exemplos de código na Linguagem Mini C#:

```
class Teste3 {
    private static int x = 2;
    const int y = 33;
    private float altura;

    public Teste3(float altura){
        this.altura = altura;
    }

    public void func1(){
        bool cliente = false;
        int i=0;
        while(cliente == true)
        {
            i++;
        }
        double valor = 2 * (8 - 4 + (3 - 1));
        int a = -77+1;
        --a = a++;
        int b,c,d;
    }

    static int func2(int a, float y, string z){
        bool existe = false;
        if (a == 1){
            if (y != 20){
                return a;
            }
        }else{
            return 12;
        }
    }

    void func3(){
        int a = 1;
        for(int i=0; i<10; i++){
            a = a * 2;
        }
    }
    void func4(int z, float x){
        return;
    }
}
```

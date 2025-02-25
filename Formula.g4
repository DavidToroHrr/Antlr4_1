grammar Formula;

// Regla principal para múltiples fórmulas
file: formula+ EOF;

// Regla principal para una fórmula
formula: expression NEWLINE*;

// Expresión puede ser una operación aritmética o una función estadística
expression
    : expression ('*' | '/' | '%') expression  # MulDivMod
    | expression ('+' | '-') expression        # AddSub
    | '(' expression ')'                       # Parens
    | NUMBER                                   # Number
    | FUNC '(' expression (',' expression)* ')'  # FunctionCall
    | ID                                       # ColumnReference
    ;

// Definición de funciones explícitas
FUNC: 'suma' | 'promedio' | 'mediaPonderada' | 'desviacion' | 'mediana' | 'varianza';

// Definición de identificadores (columnas)
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Definición de números (soporte para decimales)
NUMBER: [0-9]+ ('.' [0-9]+)?;

// Nueva línea
NEWLINE: '\r'? '\n';

// Ignorar espacios en blanco
WS: [ \t\r]+ -> skip;

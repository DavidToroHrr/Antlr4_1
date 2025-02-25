grammar Formula;

// Regla principal para una fórmula
formula: expression EOF;

// Expresión puede ser una operación aritmética o una función estadística
expression
    : expression ('*' | '/' | '%') expression  # MulDivMod
    | expression ('+' | '-') expression        # AddSub
    | '(' expression ')'                       # Parens
    | NUMBER                                   # Number
    | ID '(' expression (',' expression)* ')'  # FunctionCall
    ;

// Funciones estadísticas
ID: 'suma' | 'promedio' | 'desviacion' | 'mediaPonderada';

// Números
NUMBER: [0-9]+ ('.' [0-9]+)?;

// Ignorar espacios en blanco
WS: [ \t\r\n]+ -> skip;
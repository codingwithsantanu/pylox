from enum import Enum, auto
from dataclasses import dataclass

class TokenKind(Enum):
    # Delimiters.
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()

    # Separators.
    DOT = auto()
    COMMA = auto()
    SEMICOLON = auto()

    # Operators.
    PLUS = auto()
    MINUS = auto()
    SLASH = auto()
    STAR = auto()

    LESS = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    BANG = auto()
    BANG_EQUAL = auto()

    # Literals.
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()

    # Keywords.
    AND = auto()
    CLASS = auto()
    ELSE = auto()
    FALSE = auto()
    FUN = auto()
    FOR = auto()
    IF = auto()
    NIL = auto()
    OR = auto()
    PRINT = auto()
    RETURN = auto()
    SUPER = auto()
    THIS = auto()
    TRUE = auto()
    VAR = auto()
    WHILE = auto()

    # End of file.
    EOF = auto()

@dataclass
class Token:
    kind: TokenKind
    lexeme: str
    literal: float | bool | str | None
    line: int


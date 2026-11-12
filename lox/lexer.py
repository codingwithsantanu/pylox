from .errors import ErrorHandler
from .tokens import Token, TokenKind

class Lexer:
    def __init__(self, source: str, error_handler: ErrorHandler) -> None:
        self.source: str = source
        self.error_handler: ErrorHandler = error_handler
        
        self.length: int = len(self.source)
        self.tokens: list[Token] = []
        
        # Store the location information.
        self.start: int = 0
        self.current: int = 0
        self.line: int = 1

        # A dictionary of keywords.
        self.keywords: dict[str, TokenKind] = {
            "and":    TokenKind.AND,
            "class":  TokenKind.CLASS,
            "else":   TokenKind.ELSE,
            "false":  TokenKind.FALSE,
            "for":    TokenKind.FOR,
            "fun":    TokenKind.FUN,
            "if":     TokenKind.IF,
            "nil":    TokenKind.NIL,
            "or":     TokenKind.OR,
            "print":  TokenKind.PRINT,
            "return": TokenKind.RETURN,
            "super":  TokenKind.SUPER,
            "this":   TokenKind.THIS,
            "true":   TokenKind.TRUE,
            "var":    TokenKind.VAR,
            "while":  TokenKind.WHILE
        }

    def scan_tokens(self) -> list[Token]:
        # Scan all tokens present in the source.
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        
        # Add an EOF token at the end and return all tokens.
        self.tokens.append(
            Token(TokenKind.EOF, "", None, self.line)
        )
        return self.tokens

    def scan_token(self) -> None:
        char: str = self.advance()
        match char:
            # Delimiters.
            case '(':
                self.add_token(TokenKind.LEFT_PAREN)
            case ')':
                self.add_token(TokenKind.RIGHT_PAREN)
            case '{':
                self.add_token(TokenKind.LEFT_BRACE)
            case '}':
                self.add_token(TokenKind.RIGHT_BRACE)

            # Separators.
            case '.':
                self.add_token(TokenKind.DOT)
            case ',':
                self.add_token(TokenKind.COMMA)
            case ';':
                self.add_token(TokenKind.SEMICOLON)

            # Operators.
            case '+':
                self.add_token(TokenKind.PLUS)
            case '-':
                self.add_token(TokenKind.MINUS)
            case '*':
                self.add_token(TokenKind.STAR)
            case '/':
                if self.peek() == "/":
                    # A comment goes until the end of the line.
                    while not self.is_at_end() and self.peek() != "\n":
                        self.advance()
                else:
                    self.add_token(TokenKind.SLASH)

            case '<':
                if self.match_next('='):
                    self.add_token(TokenKind.LESS_EQUAL)
                else:
                    self.add_token(TokenKind.LESS)
            case '>':
                if self.match_next('='):
                    self.add_token(TokenKind.GREATER_EQUAL)
                else:
                    self.add_token(TokenKind.GREATER)
            case '!':
                if self.match_next('='):
                    self.add_token(TokenKind.BANG_EQUAL)
                else:
                    self.add_token(TokenKind.BANG)
            case '=':
                if self.match_next('='):
                    self.add_token(TokenKind.EQUAL_EQUAL)
                else:
                    self.add_token(TokenKind.EQUAL)

            # Whitespace (Ignored).
            case ' ' | '\t' | '\r':
                pass
            case '\n':
                self.line += 1

            # String Literals.
            case '"':
                self.handle_strings()

            # Other literals and unexpected characters.
            case _:
                if self.is_alpha(char):
                    self.handle_identifiers()
                elif self.is_digit(char):
                    self.handle_numbers()
                else:
                    self.error_handler.syntax(self.line, f"Unexpected character: '{char}'")

    def handle_strings(self) -> None:
        # Consume all characters until the closing quotes or EOF.
        while not self.is_at_end() and self.peek() != '"':
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        # Handle unterminated strings.
        if self.is_at_end():
            self.error_handler.syntax(self.line, "Unterminated string.")
            return

        # Consume the closing quotes ".
        self.advance()

        # Trim the surrounding quotes and add the token.
        literal: str = self.source[self.start + 1 : self.current - 1]
        self.add_token(TokenKind.STRING, literal)

    def handle_numbers(self) -> None:
        # Consume the integer part.
        while self.is_digit(self.peek()):
            self.advance()
        # NOTE: At EOF, peek() returns '\0' which is not a digit.

        # Look for a fractional part.
        if self.peek() == '.' and self.is_digit(self.peek_next()):
            self.advance()
            # Consume the fractional part.
            while self.is_digit(self.peek()):
                self.advance()

        # Parse the number and add the token.
        lexeme: str = self.source[self.start : self.current]
        literal: float = float(lexeme)
        self.add_token(TokenKind.NUMBER, literal)

    def handle_identifiers(self) -> None:
        # Consume the entire identifier.
        while self.is_alpha_numeric(self.peek()):
            self.advance()

        # Check whether its a keyword or not and add the token.
        lexeme = self.source[self.start : self.current]
        kind = TokenKind.IDENTIFIER
        if lexeme in self.keywords:
            kind = self.keywords[lexeme]
        self.add_token(kind)

    def is_alpha(self, char: str) -> bool:
        return (
            ("a" <= char <= "z") or
            ("A" <= char <= "Z") or
            char == "_"
        )

    def is_digit(self, char: str) -> bool:
        return "0" <= char <= "9"

    def is_alpha_numeric(self, char: str) -> bool:
        return self.is_alpha(char) or self.is_digit(char)

    def is_at_end(self) -> bool:
        return self.current >= self.length

    def advance(self) -> str:
        # Returns the current character being processed and increments the
        # counter by 1, so as to advance forward.
        self.current += 1
        return self.source[self.current - 1]

    def peek(self) -> str:
        # Lookahead by distance 1.
        if self.is_at_end():
            return '\0'
        return self.source[self.current]

    def peek_next(self) -> str:
        # Lookahead by distance 2.
        if self.current + 1 >= self.length:
            return '\0'
        return self.source[self.current + 1]

    def match_next(self, expected: str) -> bool:
        # NOTE: At EOF, peek() returns '\0' which is not equal to '='.
        if self.peek() != expected:
            return False
        self.current += 1
        return True

    def add_token(
        self,
        kind: TokenKind,
        literal: float | bool | str | None = None
    ) -> None:
        lexeme: str = self.source[self.start : self.current]
        self.tokens.append(
            Token(kind, lexeme, literal, self.line)
        )


class ErrorHandler:
    def __init__(self) -> None:
        self.had_error: bool = False

    def reset_flags(self) -> None:
        self.had_error = False

    def syntax(self, line: int, message: str) -> None:
        self.had_error = True
        self.report(line, "Syntax", "", message)

    def report(self, line: int, kind: str, where: str, message: str) -> None:
        print(f"[line {line}] {kind}Error{where}: {message}")
        # TODO: Redirect the errors to stderr instead of stdout.


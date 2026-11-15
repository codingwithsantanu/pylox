from pathlib import Path
from typing import TextIO

# Base points to the pylox directory.
BASE: Path = Path(__file__).parent.parent
SRC: Path = BASE / "lox"
EXPR_FILE: Path = SRC / "expr.py"

type Ast = dict[str, tuple[tuple[str, str]]]
EXPR: Ast = {
    # Phase: Evaluating Expresions.
    "Binary": (
        ("left", "Expr"),
        ("operator", "Token"),
        ("right", "Expr")
    ),
    "Grouping": (
        ("expression", "Expr")
    ),
    "Literal": (
        ("value", "float | bool | str")
    ),
    "Unary": (
        ("operator", "Token"),
        ("expression", "Expr")
    )
}

def main() -> None:
    # define_ast()
    pass

def define_ast(base_name: str, file_path: Path, specification: Ast) -> None:
    with filepath.open("w", encoding="utf-8") as file:
        pass

if __name__ == "__main__":
    main()


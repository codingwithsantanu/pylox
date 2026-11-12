from .exitcodes import EX_OK, EX_DATAERR, EX_NOINPUT, EX_SOFTWARE

def run_prompt() -> None:
    print("Opening the REPL")

def run_file(filePath: str) -> int:
    print(f"Opening the file: {filePath}")
    return EX_OK


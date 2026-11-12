import sys
import lox

def main(args: list[str]) -> None:
    if len(args) == 0:
        lox.run_prompt()
        sys.exit(lox.EX_OK)
    elif len(args) == 1:
        exit_code = lox.run_file(args[0])
        sys.exit(exit_code)
    else:
        print("Usage: lox [script]")
        sys.exit(lox.EX_USAGE)

if __name__ == "__main__":
    main(sys.argv[1:])


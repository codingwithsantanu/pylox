from .exitcodes import EX_OK, EX_DATAERR, EX_NOINPUT, EX_SOFTWARE
from .errors import ErrorHandler

def run_prompt() -> None:
    # Initialise the error handler.
    error_handler: ErrorHandler = ErrorHandler()

    # Main loop.
    while True:
        try:
            # Try to take the input.
            line: str = input(">>> ")

            # Exit the REPL, if required.
            if line.strip() == "q":
                break

            # Process the line.
            run(line, error_handler)

            # Reset error flags.
            error_handler.reset_flags()

        except KeyboardInterrupt:
            break

    # Display a final message.
    print("The REPL has been closed successfully.")

def run_file(filePath: str) -> int:
    try:
        # Try to open the file and fetch its contents.
        with open(filePath, "r") as file:
            contents: str = file.read()

        # Try to execute the code.
        error_handler: ErrorHandler = ErrorHandler()

        run(contents, error_handler)

        # Indicate an error in the return value, if any.
        if error_handler.had_error:
            return EX_DATAERR

        # If everything went well.
        return EX_OK
    
    except FileNotFoundError:
        print(f"File {filePath} was not found.")
        return EX_NOINPUT

def run(source: str, error_handler: ErrorHandler) -> None:
    print(f"Running: {source}")


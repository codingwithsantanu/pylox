from .exitcodes import EX_OK, EX_DATAERR, EX_NOINPUT, EX_SOFTWARE

def run_prompt() -> None:
    while True:
        try:
            # Try to take the input.
            line: str = input(">>> ")

            # Exit the REPL, if required.
            if line.strip() == "q":
                break

            # Process the line.
            run(line)

            # Reset error flags.
            pass

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
        run(contents)

        # Indicate an error in the return value, if any.
        pass

        # If everything went well.
        return EX_OK
    
    except FileNotFoundError:
        print(f"File {filePath} was not found.")
        return EX_NOINPUT

def run(source: str) -> None:
    print(f"Running: {source}")


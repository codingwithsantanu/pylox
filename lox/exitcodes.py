# The exit codes are based on the conventions defined in the sysexits.h
# header file as in UNIX. See the following website for more information.
# Link: 

EX_OK: int       = 0
EX_USAGE: int    = 64
EX_DATAERR: int  = 65
EX_NOINPUT: int  = 66
EX_SOFTWARE: int = 70

# EX_OK: Successful execution of the program, as intended.
# EX_USAGE: The command was used incorrectly in some way.
# EX_NOINPUT: The input file did not exist or was not readable.
# EX_DATAERR: The input data was incorrect in some way.
#     It is used currently to report syntax errors.
# EX_SOFTWARE: An internal software error has been detected.
#     It is used currently to report runtime errors.


# Pseudocode

START
DISPLAY welcome screen
INPUT account number and PIN

IF PIN is valid THEN
    DISPLAY transaction menu
    PROCESS selected transaction
ELSE
    INCREMENT attempt counter
    IF attempts = 3 THEN
        BLOCK account
    ENDIF
ENDIF
END

#!/bin/bash

# Ensure the script is executable
chmod +x hooks/pre-commit.py

# Forward the call to the Python pre-commit script
hooks/pre-commit.py

# Capture the exit code of the Python script
RESULT=$?

# Exit with the same code
exit $RESULT

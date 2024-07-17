import sys
import os
import re
from typing import List

# List of debug methods to check for
DEBUG_METHODS = ["print", "pdb.set_trace"]


def scan_file(file_path: str) -> List[str]:
    """
    Scans a file for debug methods that do not have the `# noqa` comment.

    :param file_path: Path to the file to scan
    :return: List of lines containing debug methods without `# noqa`
    """
    violations = []
    with open(file_path, "r") as file:
        for line_no, line in enumerate(file, 1):
            if any(re.search(rf"\b{debug_method}\b", line) for debug_method in DEBUG_METHODS) and "# noqa" not in line:
                violations.append(f"{file_path}:{line_no} {line.strip()}")
    return violations


def main() -> int:
    """
    Main function to scan all files in the commit for debug methods without `# noqa`.

    :return: Exit code (0 if no violations, 1 otherwise)
    """
    staged_files = [file.strip() for file in os.popen("git diff --cached --name-only").readlines()]
    violations = []

    for file_path in staged_files:
        if (
            file_path.endswith(".py")
            and not file_path.endswith("detect_debug_methods.py")
            and os.path.exists(file_path)
        ):
            violations.extend(scan_file(file_path))

    if violations:
        print("Debug methods found without `# noqa` comment:")  # noqa
        for violation in violations:
            print(violation)  # noqa
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

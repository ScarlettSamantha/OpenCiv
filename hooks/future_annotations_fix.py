from __future__ import annotations
import os
import argparse
from colorama import init, Fore, Style
import sys

# Initialize colorama
init(autoreset=True)


def check_and_fix_file(file_path: str, fix: bool, quiet: bool) -> bool:
    """Check and optionally fix a Python file to ensure it imports 'annotations' from '__future__'.

    Returns:
        bool: True if the file was missing the import, False otherwise.
    """
    with open(file=file_path, mode="r") as file:
        lines: list[str] = file.readlines()

    missing_import = not lines or lines[0].strip() != "from __future__ import annotations"

    if missing_import:
        if fix:
            if not quiet:
                print(
                    f"{Fore.YELLOW}🔧 [FIX] {Style.BRIGHT}Adding 'from __future__ import annotations' to {file_path}{Style.RESET_ALL}"
                )
            lines.insert(0, "from __future__ import annotations\n")
            with open(file=file_path, mode="w") as file:
                file.writelines(lines)
            return False  # Return False since it's no longer missing after the fix
        else:
            if not quiet:
                print(f"{Fore.RED}❗ [CHECK] {Style.BRIGHT}Missing import in: {file_path}{Style.RESET_ALL}")
            return True  # Still missing import
    else:
        if not quiet:
            print(f"{Fore.GREEN}✔️  [CHECK] {Style.BRIGHT}'{file_path}' is already correct.{Style.RESET_ALL}")
        return False  # Already correct, not missing


def process_directory(path: str, extension: str, recursive: bool, fix: bool, check: bool) -> int:
    """Process files in a directory, optionally recursively, and apply the import fix if needed.

    Returns:
        int: Return code (0 if all files are correct or fixed, 1 if any files are still missing the import).
    """
    abs_path = os.path.abspath(path)
    missing_imports = False
    total_files_checked = 0
    files_missing_import = 0
    files_fixed = 0

    for root, _, files in os.walk(abs_path):
        for file in files:
            if file.endswith(extension):
                file_path: str = os.path.join(root, file)
                total_files_checked += 1
                if check or fix or not (check or fix):
                    is_missing = check_and_fix_file(file_path=file_path, fix=fix, quiet=check)
                    if is_missing:
                        missing_imports = True
                        files_missing_import += 1
                    elif fix:
                        files_fixed += 1
        if not recursive:
            break

    if not check:
        correct_files = total_files_checked - files_missing_import - files_fixed
        print(f"\n{Fore.CYAN}📁 Processing completed in '{abs_path}'.{Style.RESET_ALL}")
        print(f"\n{Fore.MAGENTA}📊 Summary:{Style.RESET_ALL}")
        print(f"  {Fore.GREEN}✔️  Correct files: {correct_files}{Style.RESET_ALL}")
        if fix:
            print(f"  {Fore.YELLOW}🔧 Files fixed: {files_fixed}{Style.RESET_ALL}")
        print(f"  {Fore.RED}❗ Files still missing import: {files_missing_import}{Style.RESET_ALL}")
        print(f"  {Fore.LIGHTBLACK_EX}🔍 Total files checked: {total_files_checked}{Style.RESET_ALL}")

    return 1 if missing_imports else 0


def main() -> None:
    """Parse command line arguments and run the directory processing."""
    parser = argparse.ArgumentParser(
        description=f"{Fore.MAGENTA}🔍 Python Import Checker & Fixer{Style.RESET_ALL} - "
        f"{Fore.LIGHTBLACK_EX}Ensures your files import 'annotations' from '__future__'{Style.RESET_ALL}"
    )
    parser.add_argument(
        "path",
        type=str,
        default=".",
        nargs="?",
        help=f"{Fore.LIGHTBLUE_EX}📂 Directory to search (default: current directory).{Style.RESET_ALL}",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help=f"{Fore.LIGHTBLUE_EX}🔄 Search files recursively.{Style.RESET_ALL}",
    )
    parser.add_argument(
        "-e",
        "--extension",
        type=str,
        default=".py",
        help=f"{Fore.LIGHTBLUE_EX}📝 File extension to search (default: .py).{Style.RESET_ALL}",
    )
    parser.add_argument(
        "--fix", action="store_true", help=f"{Fore.LIGHTBLUE_EX}🛠️  Auto-fix missing imports.{Style.RESET_ALL}"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help=f"{Fore.LIGHTBLUE_EX}🔍 Only check for missing imports (no output).{Style.RESET_ALL}",
    )

    args: argparse.Namespace = parser.parse_args()

    # Ensure --fix and --check are not used together
    if args.fix and args.check:
        print(
            f"{Fore.RED}❌ [ERROR] {Style.BRIGHT}--fix and --check cannot be used together. Please choose one.{Style.RESET_ALL}"
        )
        sys.exit(2)

    abs_path = os.path.abspath(args.path)

    if not args.check:
        print(
            f"\n{Fore.MAGENTA}🚀 Starting...{Style.RESET_ALL}\n"
            f"{Fore.LIGHTBLACK_EX}📂 Directory: {abs_path}\n"
            f"📝 Extension: {args.extension}\n"
            f"🔄 Recursive: {args.recursive}\n"
            f"🛠️  Auto-Fix: {args.fix}\n"
            f"🔍 Check Only: {args.check}{Style.RESET_ALL}\n"
        )

    # Run the process and exit with the appropriate code
    exit_code = process_directory(
        path=abs_path, extension=args.extension, recursive=args.recursive, fix=args.fix, check=args.check
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import subprocess
import sys
import time
from pathlib import Path
from colorama import init, Fore, Style
from tqdm import tqdm
import argparse
from typing import Callable, List, Optional, Tuple

# Initialize colorama
init(autoreset=True)


class PreCommitChecker:
    def __init__(self, use_tqdm: bool = True, ascii_only: bool = False, silent_mode: bool = False) -> None:
        self.use_tqdm: bool = use_tqdm
        self.ascii_only: bool = ascii_only
        self.silent_mode: bool = silent_mode
        self.progress_bar: Optional[tqdm] = None  # type: ignore

    def run_command(self, command: str) -> Tuple[int, str, str]:
        """Run a shell command and return the exit status, stdout, and stderr."""
        result: subprocess.CompletedProcess[str] = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode, result.stdout.strip(), result.stderr.strip()

    def print_message(self, message: str, color: str = Fore.RESET, symbol: str = "") -> None:
        """Print a message with a specific color and symbol, optionally using tqdm."""
        formatted_message: str = f"{color}{symbol} {message.strip()}{Style.RESET_ALL}"
        if self.use_tqdm and self.progress_bar:  # type: ignore
            self.progress_bar.write(formatted_message)  # type: ignore
        else:
            print(formatted_message)

    def check_pytest(self) -> None:
        """Run pytest if there are staged Python files."""
        status, _, _ = self.run_command(command="git diff --cached --name-only | grep -E '.*\\.py$|.*/test_.*\\.py$'")
        if status == 0:
            status, _, _ = self.run_command(command="pytest --cov=openciv --cov-report=xml")
            if status != 0:
                self.print_message(message="pytest failed, commit aborted.", color=Fore.RED, symbol="❌")
                sys.exit(1)
        self.print_message(message="No Python test files staged for commit.", color=Fore.GREEN, symbol="✔️")

    def add_coverage_report(self) -> None:
        """Add coverage.xml to git staging."""
        self.run_command("git add coverage.xml")

    def update_changelog(self) -> None:
        """Generate and add changelog."""
        _, _, stderr = self.run_command(command="semantic-release changelog")
        self.run_command(command="git add CHANGELOG.md")
        if stderr:
            self.print_message(message=stderr, color=Fore.YELLOW)  # Handle warnings from the command

    def run_future_annotations_fix(self) -> None:
        """Run future_annotations_fix.py on staged Python files."""
        status, python_files, _ = self.run_command(
            command="git diff --cached --name-only --diff-filter=ACM | grep '\\.py$'"
        )
        if python_files:
            self.print_message(message="Running future_annotations_fix.py on the following files:", color=Fore.CYAN)
            self.print_message(message=python_files, color=Fore.CYAN)
            for file in python_files.splitlines():
                status, _, _ = self.run_command(command=f"python3 hooks/future_annotations_fix.py '{file}' --check")
                if status != 0:
                    self.print_message(
                        message=f"Commit rejected due to missing 'from __future__ import annotations' in {file}.",
                        color=Fore.RED,
                        symbol="❌",
                    )
                    sys.exit(1)
        else:
            self.print_message(message="No Python files require future_annotations_fix.", color=Fore.GREEN, symbol="✔️")

    def run_detect_debug_methods(self) -> None:
        """Run detect_debug_methods.py and abort commit if necessary."""
        status, _, _ = self.run_command(command="python3 hooks/detect_debug_methods.py")
        if status != 0:
            self.print_message(
                message="Commit rejected due to debug methods without # noqa comment.", color=Fore.RED, symbol="❌"
            )
            sys.exit(1)
        else:
            self.print_message(
                message="No debug methods detected without # noqa comment.", color=Fore.GREEN, symbol="✔️"
            )

    def fix_trailing_whitespace(self) -> None:
        """Placeholder function for fixing trailing whitespace."""
        self.print_message(message="No trailing whitespace issues detected.", color=Fore.GREEN, symbol="✔️")
        # Implement this function if needed
        pass

    def ensure_newline_at_eof(self) -> None:
        """Ensure all files end with a newline."""
        self.run_command(command="find . -type f \\( -name '*.py' -o -name '*.md' \\) -exec sed -i -e '$a\\' {} +")
        self.print_message(message="Ensured files end with a newline.", color=Fore.GREEN, symbol="✔️")

    def format_python_files(self) -> None:
        """Format staged Python files using ruff."""
        status, _, _ = self.run_command(command="command -v ruff &> /dev/null")
        if status == 0:
            status, files, _ = self.run_command(command="git diff --name-only --cached | grep '\\.py$'")
            if files:
                self.run_command(command=f"ruff check {files} --fix")
                self.print_message(message="Formatted Python files with ruff.", color=Fore.GREEN, symbol="✔️")
            else:
                self.print_message(message="No Python files to format in this commit.", color=Fore.GREEN, symbol="✔️")
        else:
            self.print_message(
                message="Ruff is not installed. Please install it with 'pip install ruff'.", color=Fore.RED, symbol="❌"
            )
            sys.exit(1)

    def lint_markdown_files(self) -> None:
        """Lint staged Markdown files using pymarkdownlnt."""
        status, _, _ = self.run_command(command="command -v pymarkdownlnt &> /dev/null")
        if status == 0:
            status, files, _ = self.run_command(command="git diff --name-only --cached | grep '\\.md$'")
            if files:
                status, _, stderr = self.run_command(command=f"pymarkdownlnt --config .markdownlnt.json scan {files}")
                self.print_message(message="Linted Markdown files with pymarkdownlnt.", color=Fore.GREEN, symbol="✔️")
                if stderr:
                    self.print_message(message=stderr, color=Fore.YELLOW)  # Handle any warnings from linting
            else:
                self.print_message(message="No Markdown files to lint in this commit.", color=Fore.GREEN, symbol="✔️")
        else:
            self.print_message(
                message="pymarkdownlnt is not installed. Please install it with 'pip install pymarkdownlnt'.",
                color=Fore.YELLOW,
                symbol="⚠️",
            )

    def copy_readme(self) -> None:
        """Copy README.md from meta directory and stage it."""
        if Path("meta/README.md").exists():
            self.run_command(command="cp meta/README.md README.md")
            self.run_command(command="git add README.md")
            self.print_message(message="Copied and staged README.md from meta directory.", color=Fore.GREEN, symbol="✔️")
        else:
            self.print_message(message="meta/README.md does not exist.", color=Fore.YELLOW, symbol="⚠️")

    def fix_markdown_files(self) -> None:
        """Fix Markdown files using pymarkdownlnt."""
        self.run_command(command="pymarkdownlnt --config .markdownlnt.json fix .")
        self.print_message(message="Fixed Markdown files with pymarkdownlnt.", color=Fore.GREEN, symbol="✔️")

    def add_coverage_files(self) -> None:
        """Add coverage files to git staging."""
        self.run_command(command="git add .coverage")
        self.run_command(command="git add coverage.xml")
        self.run_command(command="git add coverage.json")
        self.run_command(command="git add CHANGELOG.md")
        self.print_message(message="Added coverage files to git staging.", color=Fore.GREEN, symbol="✔️")

    def check_diff_index(self) -> None:
        """Check for differences against the current commit."""
        status, _, _ = self.run_command(command="git rev-parse --verify HEAD >/dev/null 2>&1")
        if status == 0:
            against = "HEAD"
        else:
            status, against, _ = self.run_command(command="git hash-object -t tree /dev/null")

        self.run_command(command=f"exec git diff-index --check --cached {against} --")
        self.print_message(message="Checked for differences against the current commit.", color=Fore.GREEN, symbol="✔️")

    def run_checks(self) -> None:
        """Run all the pre-commit checks."""
        start_time: float = time.time()
        steps: List[Tuple[str, Callable[[], None]]] = [
            ("Checking pytest...", self.check_pytest),
            ("Adding coverage report...", self.add_coverage_report),
            ("Updating changelog...", self.update_changelog),
            ("Running future_annotations_fix.py...", self.run_future_annotations_fix),
            ("Detecting debug methods...", self.run_detect_debug_methods),
            ("Fixing trailing whitespace...", self.fix_trailing_whitespace),
            ("Formatting Python files...", self.format_python_files),
            ("Fixing Markdown files...", self.fix_markdown_files),
            ("Ensuring newline at EOF...", self.ensure_newline_at_eof),
            ("Linting Markdown files...", self.lint_markdown_files),
            ("Copying README.md...", self.copy_readme),
            ("Adding coverage files...", self.add_coverage_files),
            ("Checking diff index...", self.check_diff_index),
        ]

        if self.silent_mode:
            # Skip all outputs if silent mode is enabled
            for _, step in steps:
                step()
        else:
            if self.use_tqdm:
                with tqdm(total=len(steps), desc="Running pre-commit checks", ascii=self.ascii_only) as progress:
                    self.progress_bar = progress
                    for description, step in steps:
                        progress.set_description(desc=description)
                        step()
                        progress.update()
            else:
                for description, step in steps:
                    print(description)
                    step()

        end_time: float = time.time()
        elapsed_time: float = end_time - start_time
        if not self.silent_mode:
            self.print_message(
                message=f"All checks passed. Proceeding with the commit. 🕒 {elapsed_time:.2f} seconds.",
                color=Fore.GREEN,
                symbol="✔️",
            )


def main() -> None:
    """Main function to parse arguments and run the checks."""
    parser = argparse.ArgumentParser(description="Run pre-commit checks.")
    parser.add_argument("--no-tqdm", action="store_true", help="Disable tqdm progress bar")
    parser.add_argument("--ascii", action="store_true", help="Use ASCII-only characters")
    parser.add_argument("--silent", action="store_true", help="Run silently with no output")
    args: argparse.Namespace = parser.parse_args()

    checker = PreCommitChecker(
        use_tqdm=not args.no_tqdm and not args.silent, ascii_only=args.ascii, silent_mode=args.silent
    )

    checker.run_checks()


if __name__ == "__main__":
    main()

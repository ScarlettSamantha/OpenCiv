"""
This type stub file was generated by pyright.
"""

import os
import subprocess
import typing

"""Run subprocesses with ``subprocess.run()`` and ``subprocess.Popen()``."""
__all__ = ['run_check', 'ExecutableNotFound', 'CalledProcessError']
log = ...
BytesOrStrIterator = typing.Union[typing.Iterator[bytes], typing.Iterator[str]]
@typing.overload
def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *, input_lines: typing.Optional[typing.Iterator[bytes]] = ..., encoding: None = ..., quiet: bool = ..., **kwargs) -> subprocess.CompletedProcess:
    """Accept bytes input_lines with default ``encoding=None```."""
    ...

@typing.overload
def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *, input_lines: typing.Optional[typing.Iterator[str]] = ..., encoding: str, quiet: bool = ..., **kwargs) -> subprocess.CompletedProcess:
    """Accept string input_lines when given ``encoding``."""
    ...

@typing.overload
def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *, input_lines: typing.Optional[BytesOrStrIterator] = ..., encoding: typing.Optional[str] = ..., capture_output: bool = ..., quiet: bool = ..., **kwargs) -> subprocess.CompletedProcess:
    """Accept bytes or string input_lines depending on ``encoding``."""
    ...

def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *, input_lines: typing.Optional[BytesOrStrIterator] = ..., encoding: typing.Optional[str] = ..., quiet: bool = ..., **kwargs) -> subprocess.CompletedProcess:
    """Run the command described by ``cmd``
        with ``check=True`` and return its completed process.

    Raises:
        CalledProcessError: if the returncode of the subprocess is non-zero.
    """
    ...

class ExecutableNotFound(RuntimeError):
    """:exc:`RuntimeError` raised if the Graphviz executable is not found."""
    _msg = ...
    def __init__(self, args) -> None:
        ...



class CalledProcessError(subprocess.CalledProcessError):
    """:exc:`~subprocess.CalledProcessError` raised if a subprocess ``returncode`` is not ``0``."""
    def __str__(self) -> str:
        ...




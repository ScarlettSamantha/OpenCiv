"""
This type stub file was generated by pyright.
"""

import os
import pathlib
import typing

"""Generic re-useable self-contained helper functions."""
__all__ = ['attach', 'mkdirs', 'mapping_items', 'promote_pathlike', 'promote_pathlike_directory', 'deprecate_positional_args']
log = ...
def attach(object: typing.Any, /, name: str) -> typing.Callable:
    """Return a decorator doing ``setattr(object, name)`` with its argument.

    >>> spam = type('Spam', (object,), {})()  # doctest: +NO_EXE

    >>> @attach(spam, 'eggs')
    ... def func():
    ...     pass

    >>> spam.eggs  # doctest: +ELLIPSIS
    <function func at 0x...>
    """
    ...

def mkdirs(filename: typing.Union[os.PathLike, str], /, *, mode: int = ...) -> None:
    """Recursively create directories up to the path of ``filename``
        as needed."""
    ...

def mapping_items(mapping, /): # -> Iterator[Any]:
    """Return an iterator over the ``mapping`` items,
        sort if it's a plain dict.

    >>> list(mapping_items({'spam': 0, 'ham': 1, 'eggs': 2}))  # doctest: +NO_EXE
    [('eggs', 2), ('ham', 1), ('spam', 0)]

    >>> from collections import OrderedDict
    >>> list(mapping_items(OrderedDict(enumerate(['spam', 'ham', 'eggs']))))
    [(0, 'spam'), (1, 'ham'), (2, 'eggs')]
    """
    ...

@typing.overload
def promote_pathlike(filepath: typing.Union[os.PathLike, str], /) -> pathlib.Path:
    """Return path object for path-like-object."""
    ...

@typing.overload
def promote_pathlike(filepath: None, /) -> None:
    """Return None for None."""
    ...

@typing.overload
def promote_pathlike(filepath: typing.Union[os.PathLike, str, None], /) -> typing.Optional[pathlib.Path]:
    """Return path object or ``None`` depending on ``filepath``."""
    ...

def promote_pathlike(filepath: typing.Union[os.PathLike, str, None]) -> typing.Optional[pathlib.Path]:
    """Return path-like object ``filepath`` promoted into a path object.

    See also:
        https://docs.python.org/3/glossary.html#term-path-like-object
    """
    ...

def promote_pathlike_directory(directory: typing.Union[os.PathLike, str, None], /, *, default: typing.Union[os.PathLike, str, None] = ...) -> pathlib.Path:
    """Return path-like object ``directory`` promoted into a path object (default to ``os.curdir``).

    See also:
        https://docs.python.org/3/glossary.html#term-path-like-object
    """
    ...

def deprecate_positional_args(*, supported_number: int, category: typing.Type[Warning] = ..., stacklevel: int = ...): # -> Callable[..., _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]]:
    """Mark supported_number of positional arguments as the maximum.

    Args:
        supported_number: Number of positional arguments
            for which no warning is raised.
        category: Type of Warning to raise
            or None to return a nulldecorator
            returning the undecorated function.
        stacklevel: See :func:`warning.warn`.

    Returns:
        Return a decorator raising a category warning
            on more than supported_number positional args.

    See also:
        https://docs.python.org/3/library/exceptions.html#FutureWarning
        https://docs.python.org/3/library/exceptions.html#DeprecationWarning
        https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning
    """
    ...

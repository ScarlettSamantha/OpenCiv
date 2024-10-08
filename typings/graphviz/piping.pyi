"""
This type stub file was generated by pyright.
"""

import typing
from . import backend, base, encoding

"""Pipe DOT code objects through Graphviz ``dot``."""
__all__ = ['Pipe']
log = ...
class Pipe(encoding.Encoding, base.Base, backend.Pipe):
    """Pipe source lines through the Graphviz layout command."""
    @typing.overload
    def pipe(self, format: typing.Optional[str] = ..., renderer: typing.Optional[str] = ..., formatter: typing.Optional[str] = ..., neato_no_op: typing.Union[bool, int, None] = ..., quiet: bool = ..., *, engine: typing.Optional[str] = ..., encoding: None = ...) -> bytes:
        """Return bytes with default ``encoding=None``."""
        ...

    @typing.overload
    def pipe(self, format: typing.Optional[str] = ..., renderer: typing.Optional[str] = ..., formatter: typing.Optional[str] = ..., neato_no_op: typing.Union[bool, int, None] = ..., quiet: bool = ..., *, engine: typing.Optional[str] = ..., encoding: str) -> str:
        """Return string when given encoding."""
        ...

    @typing.overload
    def pipe(self, format: typing.Optional[str] = ..., renderer: typing.Optional[str] = ..., formatter: typing.Optional[str] = ..., neato_no_op: typing.Union[bool, int, None] = ..., quiet: bool = ..., *, engine: typing.Optional[str] = ..., encoding: typing.Optional[str]) -> typing.Union[bytes, str]:
        """Return bytes or string depending on encoding argument."""
        ...

    def pipe(self, format: typing.Optional[str] = ..., renderer: typing.Optional[str] = ..., formatter: typing.Optional[str] = ..., neato_no_op: typing.Union[bool, int, None] = ..., quiet: bool = ..., *, engine: typing.Optional[str] = ..., encoding: typing.Optional[str] = ...) -> typing.Union[bytes, str]:
        """Return the source piped through the Graphviz layout command.

        Args:
            format: The output format used for rendering
                (``'pdf'``, ``'png'``, etc.).
            renderer: The output renderer used for rendering
                (``'cairo'``, ``'gd'``, ...).
            formatter: The output formatter used for rendering
                (``'cairo'``, ``'gd'``, ...).
            neato_no_op: Neato layout engine no-op flag.
            quiet (bool): Suppress ``stderr`` output
                from the layout subprocess.
            engine: Layout engine for rendering
                (``'dot'``, ``'neato'``, ...).
            encoding: Encoding for decoding the stdout.

        Returns:
            Bytes or if encoding is given decoded string
                (stdout of the layout command).

        Raises:
            ValueError: If ``engine``, ``format``, ``renderer``, or ``formatter``
                are unknown.
            graphviz.RequiredArgumentError: If ``formatter`` is given
                but ``renderer`` is None.
            graphviz.ExecutableNotFound: If the Graphviz ``dot`` executable
                is not found.
            graphviz.CalledProcessError: If the returncode (exit status)
                of the rendering ``dot`` subprocess is non-zero.

        Example:
            >>> doctest_mark_exe()
            >>> import graphviz
            >>> source = 'graph { spam }'
            >>> graphviz.Source(source, format='svg').pipe()[:14]
            b'<?xml version='
            >>> graphviz.Source(source, format='svg').pipe(encoding='ascii')[:14]
            '<?xml version='
            >>> graphviz.Source(source, format='svg').pipe(encoding='utf-8')[:14]
            '<?xml version='
        """
        ...




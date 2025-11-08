from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Annotated, Any, TypeVar

import typer

from .logging_config import setup_logging

app = typer.Typer(help="CLI entrypoint for the boilerplate project.")

F = TypeVar("F", bound=Callable[..., Any])

if TYPE_CHECKING:  # Provide typed decorator stubs for mypy

    def typed_callback(**_: Any) -> Callable[[F], F]:  # pragma: no cover - type helper
        def decorator(func: F) -> F:
            return func

        return decorator

    def typed_command(**_: Any) -> Callable[[F], F]:  # pragma: no cover - type helper
        def decorator(func: F) -> F:
            return func

        return decorator
else:  # Use real Typer decorators at runtime
    typed_callback = app.callback  # type: ignore[assignment]
    typed_command = app.command  # type: ignore[assignment]


@typed_callback(invoke_without_command=True)
def main(
    debug: Annotated[bool, typer.Option(help="Enable debug mode")] = False,
    json_logs: Annotated[bool, typer.Option(help="Output logs in JSON")] = False,
) -> None:
    level = "DEBUG" if debug else "INFO"
    setup_logging(level=level, json=json_logs)


@typed_command()
def hello(
    name: Annotated[str, typer.Argument(help="Name to greet")] = "world",
) -> None:
    typer.echo(f"Hello, {name}!")

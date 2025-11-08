from collections.abc import Callable
from typing import Annotated, Any, TypeVar, cast

import typer

from .logging_config import setup_logging

app = typer.Typer(help="CLI entrypoint for the boilerplate project.")

F = TypeVar("F", bound=Callable[..., None])


def typed_callback(**kwargs: Any) -> Callable[[F], F]:
    return cast(Callable[[F], F], app.callback(**kwargs))


def typed_command(**kwargs: Any) -> Callable[[F], F]:
    return cast(Callable[[F], F], app.command(**kwargs))


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

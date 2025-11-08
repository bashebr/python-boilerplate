from collections.abc import Callable
from typing import Any, TypeVar, cast

from fastapi import FastAPI

from .config import settings
from .logging_config import setup_logging

setup_logging()

app = FastAPI(title="Boilerplate FastAPI App")

RouteFn = TypeVar("RouteFn", bound=Callable[..., dict[str, str]])


def typed_get(path: str, **kwargs: Any) -> Callable[[RouteFn], RouteFn]:
    return cast(Callable[[RouteFn], RouteFn], app.get(path, **kwargs))


@typed_get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "env": settings.env}

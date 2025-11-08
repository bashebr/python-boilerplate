from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, TypeVar

from fastapi import FastAPI

from .config import settings
from .logging_config import setup_logging

setup_logging()

app = FastAPI(title="Boilerplate FastAPI App")

RouteFn = TypeVar("RouteFn", bound=Callable[..., dict[str, str]])

if TYPE_CHECKING:  # Provide typed decorator stubs for tooling

    def typed_get(
        *_: Any, **__: Any
    ) -> Callable[[RouteFn], RouteFn]:  # pragma: no cover
        def decorator(func: RouteFn) -> RouteFn:
            return func

        return decorator
else:
    typed_get = app.get  # type: ignore[assignment]


@typed_get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "env": settings.env}

from typing import Any

_Text = str | unicode

class Completer:
    def __init__(self, namespace: dict[str, Any] | None = ...) -> None: ...
    def complete(self, text: _Text, state: int) -> str | None: ...
    def attr_matches(self, text: _Text) -> list[str]: ...
    def global_matches(self, text: _Text) -> list[str]: ...

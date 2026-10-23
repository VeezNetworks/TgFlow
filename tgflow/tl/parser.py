import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(slots=True)
class TLDefinition:
    name: str
    id: int
    params: list[str]
    result: str
    is_function: bool

    @property
    def predicate(self) -> str:
        return self.name


class TLParser:
    ENTRY_PATTERN = re.compile(
        r"^([a-zA-Z0-9_\.]+)"
        r"(?:#([0-9a-fA-F]+))?"
        r"(?:\s+([^{=;]+))?"
        r"\s*=\s*([a-zA-Z0-9_<>\.]+);$"
    )

    def __init__(self, scheme_path: Optional[Path] = None):
        self.scheme_path = scheme_path
        self.types: dict[str, TLDefinition] = {}
        self.functions: dict[str, TLDefinition] = {}
        self.id_map: dict[int, TLDefinition] = {}

    @property
    def constructors(self) -> dict[str, TLDefinition]:
        return self.types

    def parse_string(self, content: str) -> None:
        is_function_section = False
        for raw_line in content.splitlines():
            line = raw_line.strip()
            if not line or line.startswith("//"):
                continue

            if line == "---types---":
                is_function_section = False
                continue
            if line == "---functions---":
                is_function_section = True
                continue

            match = self.ENTRY_PATTERN.match(line)
            if not match:
                continue

            name = match.group(1)
            hex_id = match.group(2)
            raw_params = match.group(3) or ""
            result = match.group(4)

            numeric_id = int(hex_id, 16) if hex_id else 0
            params = [p.strip() for p in raw_params.split() if p.strip()]

            defn = TLDefinition(
                name=name,
                id=numeric_id,
                params=params,
                result=result,
                is_function=is_function_section,
            )

            if is_function_section:
                self.functions[name] = defn
            else:
                self.types[name] = defn

            if numeric_id:
                self.id_map[numeric_id] = defn

    def parse(self) -> None:
        if not self.scheme_path or not self.scheme_path.exists():
            return
        with open(self.scheme_path, "r", encoding="utf-8") as f:
            self.parse_string(f.read())

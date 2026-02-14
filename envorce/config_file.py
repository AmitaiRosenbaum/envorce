from pathlib import Path
from typing import Optional

import tomllib

from envorce.errors import EnvorcementConfigError


def find_file_vars() -> list[str]:
    toml = _find_toml_file()
    if not toml:
        return []
    config = _read_envorce_file(toml)

    envorce = config.get("envorce")
    if envorce is None:
        raise EnvorcementConfigError(
            "Could not find key `envorce` in `envorce.toml`.")

    return envorce


def _read_envorce_file(path: Path) -> dict[str, list[str]]:
    with open(path, 'rb') as f:
        try:
            return tomllib.load(f)
        except tomllib.TOMLDecodeError as e:
            raise EnvorcementConfigError(
                f"The `envorce.toml` configuration file is not valid: {e}")


def _find_toml_file(base: Path | None = None, idx: int = 25) -> Optional[Path]:
    if base is None:
        base = Path.cwd()  # Starting point

    if not idx or base == Path.home():  # Stopping condition
        return

    candidate = base / 'envorce.toml'
    if candidate.exists():
        return candidate  # Found

    return _find_toml_file(base.parent, idx - 1)  # Search parent

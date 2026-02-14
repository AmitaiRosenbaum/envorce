
import os


def get_missing_variables(*args: str) -> list[str]:
    missing: list[str] = []
    for arg in args:
        if os.getenv(arg) is None:
            missing.append(arg)
    return missing

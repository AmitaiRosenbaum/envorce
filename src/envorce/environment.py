import os
import csv

from envorce.errors import EnvorcementConfigError


def find_environment_vars() -> list[str]:
    raw_env_vars = os.getenv("ENVORCE")
    if raw_env_vars is None:
        return []

    env_vars = _parse_environment_vars(raw_env_vars)
    stripped_vars = [x.strip() for x in env_vars]
    return stripped_vars


def _parse_environment_vars(raw_env_vars: str, **fmtparams) -> list[str]:
    try:
        envs = csv.reader([raw_env_vars], **fmtparams)
    except csv.Error as e:
        raise EnvorcementConfigError(
            f"Failed to parse `ENVORCE`: {e}")

    return list(envs)[0]

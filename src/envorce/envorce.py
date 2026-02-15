
from envorce.errors import EnvorcementError
from envorce.config_file import find_file_vars
from envorce.environment import find_environment_vars
from envorce.process import get_missing_variables


def envorce(*env_vars):
    discovered: list[str] = list(env_vars)

    discovered.extend(find_file_vars())
    discovered.extend(find_environment_vars())

    _envorce(*discovered)


def _envorce(*env_vars: str):
    missing = get_missing_variables(*env_vars)
    if missing:
        raise EnvorcementError(
            f"Envorced environment variables are missing: {missing}")


from .errors import EnvorcementError
from .config_file import find_file_vars
from .dotenv import find_dotenv_vars
from .process import get_missing_variables


def envorce(*args):
    discovered: list[str] = list(args)

    discovered.extend(find_file_vars())
    discovered.extend(find_dotenv_vars())

    _envorce(*discovered)


def _envorce(*args: str):
    missing = get_missing_variables(*args)
    if missing:
        raise EnvorcementError(
            f"Envorced environment variables are missing: {missing}")

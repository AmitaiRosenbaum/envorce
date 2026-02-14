# Envorce

Mini package for verifying environment variables at runtime to catch misconfigurations as early as possible.

# Configuration

There are a number of different ways in which you can specify the environment variables which need to be "envorced". They can be used individually or simultaneously.

## Via environment variables

Set the environment variable `ENVORCE` as a comma-separated list of required environment variable.

```bash
ENVORCE=DB_USERNAME, DB_PASSWORD, API_URL
```

Then, in your top-level script simply call

```python
from envorce import envorce

envorce()
```

## Via function arguments

Specify required variables by passing them into the top-level function call.

```python
from envorce import envorce

envorce("AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY")
```

## Via configuration file

Add a file `envorce.toml` into your project repository and set the key `envorce` as a list of required environment variables.

```toml
# envorce.toml
envorce = ["DATABASE_HOST", "DATABASE_USERNAME", "DATABASE_PASSWORD"]
```

Then, in your top-level script simply call

```python
from envorce import envorce

envorce()
```

The program will continue to search parent directories for the file `envorce.toml` until reaching the home directory or the iteration limit.

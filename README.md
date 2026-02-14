# Envorce

Mini package for verifying environment variables before running your project

# Configuration

## Via .env file

In your `.env` file, you can mark multi-line or single-line required environment variables.

```bash
OPTIONAL_ENV_1=

### ENVORCE-START ###
REQUIRED_ENV=
ANOTHER_REQUIRED_ENV=
### ENVORCE-END ###

OPTIONAL_ENV_2=

### ENVORCE
REQUIRED_ENV=
OPTIONAL_ENV_1=
```

Then, in your top-level script simply call

```python
from dotenv import load_dotenv
from envorce import envorce

load_dotenv()
envorce()
```

## Via function arguments

Specify required variables by passing them into the top-level function call.

```python
from envorce import envorce

envorce("AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY")
```

## Via configuration file

Add a file `envorce.toml` into your project repository and populate it with required environment variables.

### Separate by new line

```bash
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
REQUIRED_VARIABLE
```

Then, in your top-level script simply call

```python
from envorce import envorce

envorce()
```

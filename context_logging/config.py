import os


def parse_env_to_bool(val: str) -> bool:
    return val.lower() in ['yes', 'true', '1']


class Config:
    FILL_EXCEPTIONS_DEFAULT: bool = parse_env_to_bool(
        os.getenv('CONTEXT_LOGGING_FILL_EXCEPTIONS_DEFAULT', 'yes')
    )
    LOG_EXECUTION_TIME_DEFAULT: bool = parse_env_to_bool(
        os.getenv('CONTEXT_LOGGING_LOG_EXECUTION_TIME_DEFAULT', 'yes')
    )


config = Config()

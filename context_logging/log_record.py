import logging
from typing import Any

from .context import get_current_context_shapshot


class ContextLogRecord(logging.LogRecord):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.context = get_current_context_shapshot()


def setup_log_record() -> None:
    logging.setLogRecordFactory(ContextLogRecord)

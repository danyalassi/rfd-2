from . import filter, flog_table
import re

patterns = [
    # 2021E
    (
        br'^'

        # Current timestamp.
        br'(?P<timestamp>[\d\.]+),'

        # Changes randomly between RCC sessions.
        br'[0-9a-f]+,'

        # RCC's own log level.
        br'(?P<rcc_log_num>\d+),'

        # Constant across all RCC logs.
        br'GameServer,'

        # Defaults to 1818.
        br'[^\s,]+,'

        # Defaults to 13058.
        br'[^\s,]+,'

        # Defaults to "https://localhost:2005/.127.0.0.1".
        br'[^\s,]+,'

        # Constant across all RCC logs.
        br'Test,'

        # Defaults to "https://localhost:2005".
        br'[^\s,]+,'

        # Constant across all RCC logs.
        br'unknown,'

        # Constant across all RCC logs.
        br'Test'

        # Gets FLog type.
        br' \[(?P<log_name>.*?)\]'

        # Captures the rest of the line.
        br' (?P<rest_of_line>.+)$'
    ),

    # 2021E
    (
        br'^'

        # Current timestamp.
        br'(?P<timestamp>[\d\.]+),'

        # Changes randomly between RCC sessions.
        br'[0-9a-f]+,'

        # RCC's own log level.
        br'(?P<rcc_log_num>\d+)'

        # Gets FLog type.
        br' \[(?P<log_name>.*?)\]'

        # Captures the rest of the line.
        br' (?P<rest_of_line>.+)$'
    ),

    # 2018M
    (
        br'^'

        # Current timestamp.
        br'(?P<timestamp>[\d\.]+),'

        # Changes randomly.
        br'[0-9a-f]+,'

        # RCC's own log level.
        br'(?P<rcc_log_num>\d+)'

        # Captures the rest of the line.
        br' (?P<rest_of_line>.+)$'
    ),

    # 2018M
    (
        br'^'

        # Current timestamp.
        br'(?P<timestamp>[\d\.]+),'

        # Changes randomly.
        br'[0-9a-f]+,'

        # RCC's own log level.
        br'(?P<rcc_log_num>\d+),'

        # Constant across all RCC logs.
        br'GameServer,'

        # Defaults to 1818.
        br'[^\s,]+,'

        # Defaults to 13058.
        br'[^\s,]+,'

        # Defaults to "https://localhost:2005/.127.0.0.1".
        br'[^\s,]+,'

        # Constant across all RCC logs.
        br'Test,'

        # Defaults to "https://localhost:2005".
        br'[^\s,]+,'

        # Constant across all RCC logs.
        br'unknown,'

        # Constant across all RCC logs.
        br'Test'

        # Captures the rest of the line.
        br' (?P<rest_of_line>.+)$'
    ),
]


def get_level_table(filter: filter.filter_type) -> dict[str, int]:
    return {
        i: (v if v in filter.rcc_logs.flogs else 0)
        for i, v in flog_table.LOG_LEVEL_DICT.items()
    }
    # TODO: allow hosters to determine if they want a verbose log file or not.
    return flog_table.LOG_LEVEL_DICT


def get_log_name(i: int) -> str:
    if i - flog_table.INDEX_OFFSET < len(flog_table.LOG_LEVEL_LIST):
        return flog_table.LOG_LEVEL_LIST[i - flog_table.INDEX_OFFSET]
    else:
        return '%3d (unknown log level)' % i


def get_message(text: bytes, log_filter: filter.filter_type) -> str | None:
    if log_filter.rcc_logs.is_empty():
        return

    match = next(
        (
            re.match(pattern, text)
            for pattern in patterns
            if (match := re.match(pattern, text)) is not None
        ), None,
    )

    if match is None:
        return None

    rcc_log_num = int(match['rcc_log_num'])
    if rcc_log_num not in log_filter.rcc_logs:
        return

    rcc_log_type = get_log_name(rcc_log_num)
    decoded_line = match['rest_of_line'].decode(
        'utf-8', errors='backslashreplace',
    )

    # For cases in 2018M when the log line begins with
    # `[Output] Output:` or `[Error] Error:`.
    if decoded_line.startswith(f'{rcc_log_type}: '):
        decoded_line = decoded_line[len(rcc_log_type) + 2:]

    return (
        f'{log_filter.bcolors.OKGREEN}[RCC %s]{log_filter.bcolors.ENDC} %s'
    ) % (
        rcc_log_type,
        decoded_line,
    )

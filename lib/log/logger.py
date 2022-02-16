from loguru import logger
from lib.log import notify


def init_logger(program_name, log_level='DEBUG'):
    """
    Logger for program
    :type program_name: name of current program
    :type log_level: log level to filter output
    """
    # set log format
    logger.add('{program_name}.log'.format(program_name=program_name),
               format='{time:!UTC} {level} {message}',
               level=log_level,
               rotation='1 MB',
               compression='zip')
    # add mail notification
    notify.add_gmail_sender(logger)
    # add telegram notification
    # notify.add_telegram_sender(logger)

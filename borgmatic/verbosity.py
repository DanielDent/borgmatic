import logging


VERBOSITY_SOME = 1
VERBOSITY_LOTS = 2


def verbosity_to_log_level(verbosity):
    '''
    Given a borgmatic verbosity value, return the corresponding Python log level.
    '''
    return {
        VERBOSITY_SOME: logging.INFO,
        VERBOSITY_LOTS: logging.DEBUG,
    }.get(verbosity, logging.ERROR)

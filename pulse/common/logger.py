# -*- coding: utf-8 -*-
import logging

formatter = logging.Formatter(
    fmt='%(asctime)s %(levelname)-8s: %(name)-11s, (%(filename)-18s:%(lineno)-4d) - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)


def logger_init(name, logfile=None):
    lgr = logging.getLogger(name)
    lgr.setLevel(logging.INFO)

    lgr.handlers.clear()
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(logging.INFO)
    lgr.addHandler(console)
    return lgr


def logger_addpath(lgr, path):
    if path:
        # создаём обрабочтик файла лога
        filehandler = logging.FileHandler(path)
        # задаём уровень логгирования
        filehandler.setLevel(logging.DEBUG)
        # устанавливаем формат для обработчика
        filehandler.setFormatter(formatter)
        # добавляем обработчик к логгеру
        lgr.addHandler(filehandler)
    return lgr


if __name__ == "__main__":
    logger = logger_init('TEST')
    # logger_addpath(logger, './logs.log')
    logger.info('Logging test 1!')
    logger.debug('Logging test 2!')
    logger.warning('Logging test 3!')
    logger.error('Logging test 4!')

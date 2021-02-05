import time
import numpy as np
import billiard.exceptions
import celery.exceptions


def str_tubes(tubes):
    tubestr = '[\t'
    tubestr += '\n\t'.join([repr(t) for t in tubes])
    tubestr += ']'
    return tubestr


def derr2m(x, y):
    eps = np.finfo(float).eps
    return [np.abs(200*(xi-yi)/(xi+yi+eps)) for xi, yi in zip(x, y)]


def derr2m_norm(x, y, p=np.inf):
    from numpy import finfo
    eps = finfo(float).eps
    return np.linalg.norm([np.abs(200*(xi-yi)/(xi+yi+eps)) for xi, yi in zip(x, y)], ord=p)


def isin(val, arr):
    return np.any(np.abs(np.array(arr) - val) < 1e-6)


def tic():
    return time.time()


def toc(start):
    return time.time() - start


def profile_decorator(logger=None):
    if not logger:
        import logging as logger

    def profile(method):
        def wrapper(*args, **kwargs):
            import time
            start = time.time()
            output = method(*args, **kwargs)
            end = time.time()
            logger.info('Process "{}" took {} seconds'.format(method.__name__, end - start))
            return output
        return wrapper
    return profile


def message_to_try_except(message):
    def try_except(fn):
        def wrapped(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except (billiard.exceptions.TimeLimitExceeded, celery.exceptions.TimeoutError) as e:
                if not e.args:
                    e.args = ('',)
                e.args = ('Timeout error. Please, repeat calculation.',)
                raise e
            except Exception as e:
                if not e.args:
                    e.args = ('',)
                e.args = (message,)
                raise e
        return wrapped
    return try_except


def make_las(data_dict):
    import lasio
    import datetime
    las_file = lasio.LASFile()
    las_file.well['DATE'].value = str(datetime.datetime.today())
    las_file.params['ENGI'] = lasio.HeaderItem('ENGI', '', 'test@test.com', 'Creator of this file...')
    las_file.other = 'LAS file using lasio'
    las_file.curves.clear()
    las_file.add_curve('DEPT', data_dict['DEPT'], unit='ft')
    for key in data_dict.keys():
        if key != 'DEPT':
            las_file.add_curve(str(key), data_dict[key], unit='mV', descr='Made-up curve data for example')
    return las_file


def profile(method):
    def wrapper(*args, **kwargs):
        start = tic()
        output = method(*args, **kwargs)
        print('Process "{}" took {} seconds'.format(method.__name__, toc(start)), flush=True)
        return output
    return wrapper

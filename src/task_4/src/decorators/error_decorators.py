from helper.color_loger import  log_warning, log_error
from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            ##log_warning(f"{e}")
            log_error(f"{e}")
        except Warning as e:
            log_warning(f"{e}")

    return inner
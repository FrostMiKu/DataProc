def debug(func):
    """装饰器 @debug"""
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper
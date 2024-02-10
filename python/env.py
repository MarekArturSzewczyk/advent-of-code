import os

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)


def data(edition_year, day, test=False, root_dir=ROOT_DIR):
    with open(os.path.join(root_dir, f"data{'_test' if test else ''}", str(edition_year), f'd{day}.txt')) as f:
        return f.read()

def inspect(f):
    def _inner(*args, **kwargs):
        res = f(*args, **kwargs)
        print(f"{f.__qualname__}({args}, {kwargs}) = {res}")
        return res
    return _inner

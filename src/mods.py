import os


def env(name:str, _def=''):
    return os.environ.get(name, _def)


def set_output(key:str, value:str):
    with open(env('GITHUB_OUTPUT'), 'a') as f:
        f.write(f'{key}={value}\n')


# ENV
spec = env('spec')



# spec file name without extension
specName = spec.removesuffix('.py').removesuffix('.spec')
set_output('spec_name', specName)

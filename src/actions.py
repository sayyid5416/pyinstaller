import os
from typing import Literal


def env(name:str, _def=''):
    return os.environ.get(name, _def)

#-bug: Previous step annotations are being overwritten
def set_annotation(
    message:str,
    title:str='',
    _type:Literal['debug', 'notice', 'warning', 'error']='notice',
):
    title = f' title={title}' if title else ''
    print(f'::{_type}{title}::{message}')
    if _type == 'error':
        exit(1)


def set_output(key:str, value:str):
    with open(env('GITHUB_OUTPUT'), 'a') as f:
        f.write(f'{key}={value}\n')

import os
from typing import Literal


def env(name: str, _def=''):
    """ Returns environment variable """
    return os.environ.get(
        name,
        _def
    )


def set_annotation(
    message: str,
    title: str='',
    _type: Literal['debug', 'notice', 'warning', 'error']='notice',
):
    """
    Sets annotation with `message` text
    - `title`: If provided, `title` text will be shown as title
    - `_type`: Type of annotation to set
    """
    title = f' title={title}' if title else ''
    print(f'::{_type}{title}::{message}')
    if _type == 'error':
        exit(1)


def set_output(key: str, value: str):
    """ Sets the output to `$GITHUB_OUTPUT` file
    - Using `key=value`
    """
    with open(env('GITHUB_OUTPUT'), 'a') as f:
        f.write(
            f'{key}={value}\n'
        )

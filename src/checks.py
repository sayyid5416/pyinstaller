import os
from typing import Literal


def env(name:str, _def=''):
    return os.environ.get(name, _def)


def set_annotation(
    message:str,
    title:str=None,
    _type:Literal['debug', 'notice', 'warning', 'error']='notice',
):
    title = f' title={title}' if title else ''
    print(f'::{_type}{title}::{message}')
    if _type == 'error':
        exit(1)



# ENV
spec = env('spec')
upload_exe_with_name = env('upload_exe_with_name')



""" Checks """
# If required inputs missing -> ERROR
if not spec:
    set_annotation(
        "Required input missing: 'spec'.",
        'Input-Error',
        'error'
    )

# If passed inputs are not supported -> ERROR
supported_spec = ('.py', '.spec')
if not spec.endswith(supported_spec):
    set_annotation(
        f"Unsupported input 'spec = {spec}' was provided. Supported types: {', '.join(supported_spec)}",
        'Input-Error',
        'error'
    )

# If useful optional arguments missing -> NOTICE
if not upload_exe_with_name:
    set_annotation(
        "Executable couldn't upload. Provide input for 'upload_exe_with_name', if you want to upload the executable as artifact.",
        'No-Upload'
    )
 
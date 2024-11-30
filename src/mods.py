from actions import *
from typing import List
import os
import env



### ENV
spec = env('spec')
options = env('options')
spec_options = env('spec_options')


# Minor parsing
specPath, specExt = os.path.splitext(spec)                                          # spec-name-with-path & spec-extension 
providedOptions = [
    i.strip() for i in options.split(',') if i.strip() != ''
]                                                                                   # list of provided options




## ---------------------- Pyinstaller Options ---------------------- ##
# Supported options
pyOptions = [
    '--uac-admin',
    '--uac-uiaccess',
    '--noupx',
    
    '--onedir',                         '-D',
    '--onefile',                        '-F',
    '--ascii',                          '-a',
    '--console',    '--nowindowed',     '-c',
    '--windowed',   '--noconsole',      '-w',
    
    '--key <KEY>',
    '--upx-dir <UPX_DIR>',
    '--upx-exclude <FILE>',

    '--add-data <SRC;DEST or SRC:DEST>',
    '--add-binary <SRC;DEST or SRC:DEST>',
    '--collect-data <MODULENAME>',
    '--collect-all <MODULENAME>',
    '--version-file <FILE>',

    '--name <NAME>',                    '-n <NAME>',
    '--icon <FILEICON>',                '-i <FILEICON>',
]
specOptions = [
    '--ascii',                          '-a',
    '--upx-dir <UPX_DIR>',
]

# Keys of Supported options (w/o values)
pyOptions_keys = [
    i.split()[0] for i in pyOptions
]
specOptions_keys = [
    i.split()[0] for i in specOptions
]

# Distinguish provided options -> into supported & unsupported options
supported_options: List[str] = []
unsupported_options: List[str] = []
for option in providedOptions:
    option_key = option.split()[0]
    if bool(option_key in pyOptions_keys and specExt == '.py') or \
        bool(option_key in specOptions_keys and specExt == '.spec'):
            supported_options.append(option)
    else:
        unsupported_options.append(option)

## Supported options -> OUTPUT -> NOTICE
if supported_options:
    set_output(
        'supported_options',
        ' '.join(supported_options)
    )
    set_annotation(
        f"Options setted for '{specExt}' spec type: {', '.join(supported_options)}",
        'Pyinstaller Options'
    )

## Unsupported options -> WARNING
if unsupported_options:
    set_annotation(
        f"Unsupported options found for '{specExt}' spec type: {', '.join(unsupported_options)}",
        'Pyinstaller Options',
        'warning'
    )


def get_option_value(option: str):
    """ Returns: Value of `option` from provided options """
    for i in supported_options: 
        iList = i.split(maxsplit=1)
        if len(iList) < 2:
            continue
        key, value, *_ = iList
        if key == option:
            return value.strip('"').strip("'")



## ---------------------- Spec path ---------------------- ##
_specPath = str(specPath)

# If "--name" option is specified in options
specfiedName = get_option_value('-n') or get_option_value('--name')
if specfiedName:
    _specPath = os.path.join(
        os.path.split(_specPath)[0],                                                #path w/o filename
        specfiedName                                                                #new filename
    )                                                                               #new path of spec file

set_output(
    'spec_name',
    os.path.basename(_specPath)
)



## ---------------------- Spec options ---------------------- ##
set_output(
    'supported_spec_options',
    f'-- {spec_options}' if bool(spec_options) else ""
)

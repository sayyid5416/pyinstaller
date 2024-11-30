from actions import *
from typing import List



### ENV
spec = env('spec')
options = env('options')
spec_options = env('spec_options')


# General
specPath, specExt = os.path.splitext(spec)
isPyType = bool(specExt == '.py')
isSpecType = bool(specExt == '.spec')




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
pyOptionKeys = [i.split()[0] for i in pyOptions]
specOptionKeys = [i.split()[0] for i in specOptions]

# Distinguish provided options -> into supported & unsupported options
providedOptions = [i.strip() for i in options.split(',') if i.strip() != '']
supportedOptions: List[str] = []
unsupportedOptions: List[str] = []

for option in providedOptions:
    optionKey = option.split()[0]
    if bool(isPyType and optionKey in pyOptionKeys) or bool(isSpecType and optionKey in specOptionKeys):
        supportedOptions.append(option)
    else:
        unsupportedOptions.append(option)

## Supported options -> OUTPUT -> NOTICE
if supportedOptions:
    set_output(
        'supported_options',
        ' '.join(supportedOptions)
    )
    set_annotation(
        f"Options setted for '{specExt}' spec type: {', '.join(supportedOptions)}",
        'Pyinstaller Options'
    )

## Unsupported options -> WARNING
if unsupportedOptions:
    set_annotation(
        f"Unsupported options found for '{specExt}' spec type: {', '.join(unsupportedOptions)}",
        'Pyinstaller Options',
        'warning'
    )


def get_option_value(option: str):
    """ Returns: Value of `option` from provided options """
    for i in supportedOptions: 
        iList = i.split(maxsplit=1)
        if len(iList) < 2:
            continue
        key, value, *_ = iList
        if key == option:
            return value.strip('"').strip("'")



## ---------------------- Spec path ---------------------- ##
specPathNew = str(specPath)

# If "--name" option is specified in options
specfiedName = get_option_value('-n') or get_option_value('--name')
if specfiedName:
    specPathNew = os.path.join(
        os.path.dirname(specPathNew),                                               # path w/o filename
        specfiedName                                                                # new filename
    )                                                                               # new path of spec file

set_output(
    'spec_path',
    os.path.basename(specPathNew) + '.spec'
)



## ---------------------- Spec options ---------------------- ##
isOptionSet = isSpecType and bool(spec_options)
set_output(
    'supported_spec_options',
    f'-- {spec_options}' if isOptionSet else ""
)
if isOptionSet:
    set_annotation(
        f"Custom Spec Options: {spec_options}",
        'Pyinstaller Options'
    )

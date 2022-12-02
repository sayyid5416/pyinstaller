from actions import *



### ENV
spec = env('spec')
options = env('options')


# Minor parsing
specName, specExt = os.path.splitext(spec)                                          # spec-name-with-path & spec-extension 
providedOptions = [i.strip() for i in options.split(',') if i.strip() != '']        # list of provided options




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

    '--name <NAME>',                    '-n <NAME>',
    '--icon <FILEICON>',                '-i <FILEICON>',
]
specOptions = [
    '--ascii',                          '-a',
    '--upx-dir <UPX_DIR>',
]

# Keys of Supported options (w/o values)
pyOptions_keys = [i.split()[0] for i in pyOptions]
specOptions_keys = [i.split()[0] for i in specOptions]

# Distinguish provided options -> into supported & unsupported options
supported_options :list[str] = []
unsupported_options :list[str] = []
for option in providedOptions:
    print(f'{option=}')
    option_key = option.split()[0]
    print(f'{option_key=}')
    if bool(option_key in pyOptions_keys and specExt == '.py') or \
        bool(option_key in specOptions_keys and specExt == '.spec'):
            supported_options.append(option)
    else:
        unsupported_options.append(option)

## Supported options -> OUTPUT -> NOTICE
if supported_options:
    set_output('supported_options', ' '.join(supported_options))
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


def get_option_value(option:str):
    """ Returns: Value of `option` from provided options (if available) """
    for i in supported_options: 
        iList = i.split(maxsplit=1)
        
        if len(iList) < 2:
            continue
        
        key, value, *_ = iList
        if key == option:
            return value



## ---------------------- Spec Name ---------------------- ##
_specName = str(specName)

# If "--name" option is specified in options
specfiedName = get_option_value('-n') or get_option_value('--name')
if specfiedName:
    _specName = os.path.join(
        os.path.split(_specName)[0],                                                #path w/o filename
        specfiedName                                                                #new filename
    )                                                                               #new path of spec file

set_output('spec_name', _specName)

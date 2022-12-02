from actions import *



### ENV
spec = env('spec')
options = env('options')


# Minor parsing
specName, specExt = os.path.splitext(spec)                                  # spec-name-with-path & spec-extension 
providedOptions = [i.strip() for i in options.split(',') if i != '']        # list of provided options




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
    
    '--upx-dir UPX_DIR',
    '--key KEY',
    '--upx-exclude FILE',

    '--name NAME',                      '-n NAME',
    '--icon FILEICON',                  '-i FILEICON',
]
specOptions = [
    '--ascii',                          '-a',
    '--upx-dir UPX_DIR',
]

# Keys of Supported options (w/o values)
pyOptions_keys = [i.split()[0] for i in pyOptions]
specOptions_keys = [i.split()[0] for i in specOptions]

# Distinguish provided options -> into supported & unsupported options
supported_options :list[str] = []
unsupported_options :list[str] = []
for option in providedOptions:
    option_key = option.split()[0]
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





## ---------------------- Spec Name ---------------------- ##
_specName = str(specName)
set_output('spec_name', _specName)

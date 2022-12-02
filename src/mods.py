from actions import *



### ENV
spec = env('spec')


# Minor parsing
specName, specExt = os.path.splitext(spec)                            # spec-name-with-path & spec-extension 





## ---------------------- Pyinstaller Options ---------------------- ##
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






## ---------------------- Spec Name ---------------------- ##
_specName = str(specName)
set_output('spec_name', _specName)

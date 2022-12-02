from actions import *



### ENV
spec = env('spec')






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

# spec file name without extension
specName = spec.removesuffix('.py').removesuffix('.spec')
set_output('spec_name', specName)

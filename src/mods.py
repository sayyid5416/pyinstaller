from actions import *



### ENV
spec = env('spec')


# spec file name without extension
specName = spec.removesuffix('.py').removesuffix('.spec')
set_output('spec_name', specName)



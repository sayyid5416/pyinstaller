from actions import *




# ENV
spec = env('spec')
upload_exe_with_name = env('upload_exe_with_name')



# [ERROR] If required inputs missing
if not spec:
    set_annotation(
        "Required input missing: 'spec'.",
        'Input-Error',
        'error'
    )


# [ERROR] If passed inputs are not supported
supported_spec = (
    '.py',
    '.spec'
)
if not spec.endswith(supported_spec):
    set_annotation(
        f"Unsupported input 'spec = {spec}' was provided. Supported types: {', '.join(supported_spec)}",
        'Input-Error',
        'error'
    )


# [WARNING] If useful optional arguments missing
if not upload_exe_with_name:
    set_annotation(
        "Executable not uploaded. Provide 'upload_exe_with_name' to upload it as an artifact."
        'No-Upload',
        'warning'
    )
 
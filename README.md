Check all available usable tags [here](../../tags)
<br>
You can also use any major tags like `@v1` for any `@v1.*.*`


<br>


# 🔰 PyInstaller
  - This action packages the python source code into executables using [pyinstaller](https://pyinstaller.org).
  - Use this action in your workflow to **create** & **upload** executables to GitHub _(as artifacts)_.
  - Use [inputs](#-inputs--outputs) to configure this action.
  - Use [outputs](#-inputs--outputs) to get information from this action.


<br>


# 🔰 Features
### 💠 Multi-OS support
  - Create executable for different kinds of os like linux, windows, mac etc.
  - Specify OS in `jobs.<job-id>.runs-on=<your-os-name>` in your workflow file.
  - see [examples](#-examples) for more info.

### 💠 .py and .spec support
  - You can use either `.py` or `.spec` file to create the executable.
  - Specify it in `inputs.spec: <file.py/file.spec>`.
  - When `.py` file is used, generated `.spec` file will also be uploaded as artifact.
  - Modify your `.spec` file according to your needs.

### 💠 Third party modules
  - Write your third party modules in a file _(Ex: `requirements.txt`)_ , and
  - Use `inputs.requirements: <path-to-your-requirement-file>`.

### 💠 Pyinstaller options
  - Specify pyinstaller options in `inputs.options: <comma-seperated-options-here>`.
  - `.py` and `.spec` both supports different kind of options.
  - Check list of all [supported options here](#-inputs--outputs).

### 💠 Python versions
  - You can specify any python version for the executable.
  - Specify specific python-version in `inputs.python_ver: <python-version-here>`.

### 💠 Executable uploads
  - You can control if generated executable needs to be uploaded as artifact.
  - You can choose a name of your liking.
  - Specify the artifact name in `inputs.upload_exe_with_name: <name-here>`.


<br>


# 🔰 Inputs & Outputs
  - Some **inputs** are **required**, while rest are optional. 
  - Check detailed info about these inputs & outputs [here](/action.yml).

### 💠 Available Inputs

  | Input                 | Default   | Description |
  |-----------------------|:---------:|-------------|
  | `spec`  _(required)_  | -        | Path of your `.py` or `.spec` file
  | `requirements`        | -        | Path of your `requirements.txt` file
  | `options`             | -        | Options to set for pyinstaller command
  | `python_ver`          | 3.10     | Specific python version you want to use
  | `exe_path`            | ./dist   | Path on runner-os, where generated executable files are stored
  | `upload_exe_with_name`| -        | If passed, uploads executable artifact  with this name. Else, artifact won't be uploaded.

  **\*** `-` in default value = empty string

### 💠 Available Outputs

  | Output                | Description |
  |-----------------------|-------------|
  | `executable_path`     | Path on runner-os, where generated executable files are stored
  | `is_uploaded`         | `true`, if packaged executable has been uploaded as artifact

### 💠 Supported Pyinstaller options
  - Usage: `inputs.options: <option-1>, <option-2>, ...`
  - Read more about [pyinstaller options here](https://pyinstaller.org/en/stable/usage.html#options)
  - Options supported for `.py` type `spec`:

    |Options|Options|Options|
    |:-----:|:-----:|:-----:|
    | `--uac-admin`     | `--onedir`,                         `-D` | `--upx-dir <UPX_DIR>`
    | `--uac-uiaccess`  | `--onefile`,                        `-F` | `--key <KEY>`
    | `--noupx`         | `--ascii`,                          `-a` | `--upx-exclude <FILE>`
    |                   | `--console`,    `--nowindowed`,     `-c` | `--name <NAME>`,                    `-n <NAME>`
    |                   | `--windowed`,   `--noconsole`,      `-w` | `--icon <FILEICON>`,                `-i <FILEICON>`
    
  - Options supported for `.spec` type `spec`:
    - `--ascii`,                          `-a`
    - `--upx-dir <UPX_DIR>`


<br>


# 🔰 Examples

```yaml
jobs:
  pyinstaller-build:
    runs-on: <windows-latest / ubuntu-latest / ..... etc>
    steps:
      - name: Create Executable
        uses: sayyid5416/pyinstaller@v1
        with:
          python_ver: '3.6'
          spec: 'src/build.spec'
          requirements: 'src/requirements.txt'
          upload_exe_with_name: 'My executable'
```

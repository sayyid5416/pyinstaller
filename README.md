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
<br>
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
  - Check list of all [supported options here](#-supported-pyinstaller-options).

### 💠 Python and Pyinstaller versions
  - You can specify any python version for the executable.
  - Specify specific python-version in `inputs.python_ver: <python-version-here>`.
  - Specify specific pyinstaller-version in `inputs.pyinstaller_ver: <pyinstaller-version-here-with-proper-signs, like '==5.13.2'>`.

### 💠 Executable uploads
  - You can control if generated executable needs to be uploaded as artifact.
  - You can choose a name of your liking.
  - You can also customise the level of compression for the archive.
  - Specify the artifact name in `inputs.upload_exe_with_name: <name-here>`.


<br>
<br>
<br>


# 🔰 Inputs & Outputs
  - Some **inputs** are **required**, while rest are optional. 
  - Check detailed info about these inputs & outputs [here](/action.yml).

### 💠 Available Inputs
  | Input                 | Default <br> _(`-` = empty string)_  | Description 
  |-----------------------|:--------:|-------------
  | `spec`  _(required)_  | -        | Path of your `.py` or `.spec` file
  | `requirements`        | -        | Path of your `requirements.txt` file
  | `options`             | -        | [Options](#-supported-pyinstaller-options) to set for pyinstaller command
  | `spec_options`        | -        | [Custom parameters for the spec file](https://pyinstaller.org/en/v6.0.0/spec-files.html#adding-parameters-to-spec-files)
  | `python_ver`          | 3.10     | Specific python version you want to use
  | `python_arch`         | x64      | Specific python architecture you want to use
  | `pyinstaller_ver`     | -        | Specific pyinstaller version you want to use <br>*(with proper signs, like `==5.13.2`)*
  | `exe_path`            | ./dist   | Path on runner-os, where executable will be stored
  | `upload_exe_with_name`| -        | Upload exe_ artifact with this name. Else, it won't upload
  | `clean_checkout`      | true     | If true, perform a clean checkout; if false, skip cleaning. Cleaning will remove all existing local files not in the repository during checkout. If you use utilities like pyinstaller-versionfile, set this to false.
  | `lfs`                 | false    | Whether to download Git-LFS files (passed to `lfs` option in actions/checkout step)
  | `compression_level`   | 6        | Level of compression for archive. <br>Range: 0 and 9. <br>_(0 = No compression, 9 = Max compression)_.

<br>

### 💠 Available Outputs
  | Output                | Description 
  |-----------------------|-------------
  | `executable_path`     | Path on runner-os, where executable will be stored
  | `is_uploaded`         | `true`, if packaged executable has been uploaded as artifact

<br>

### 💠 Supported [Pyinstaller options](https://pyinstaller.org/en/stable/usage.html#options)
 | For `.py`                               | For `.py`                               | For `.spec`
 |-----------------------------------------|-----------------------------------------|------------
 | `--uac-admin`                           | `--name <NAME>`,        `-n <NAME>`     | `--ascii`,  `-a`
 | `--uac-uiaccess`                        | `--icon <FILEICON>`,    `-i <FILEICON>` | `--upx-dir <UPX_DIR>`
 | `--noupx`                               | `--key <KEY>`                           | 
 | `--onedir`,                        `-D` | `--upx-dir <UPX_DIR>`                   |
 | `--onefile`,                       `-F` | `--upx-exclude <FILE>`                  |
 | `--ascii`,                         `-a` | `--add-data <SRC;DEST or SRC:DEST>`     |
 | `--console`,    `--nowindowed`,    `-c` | `--add-binary <SRC;DEST or SRC:DEST>`   |
 | `--windowed`,   `--noconsole`,     `-w` | `--collect-data <MODULENAME>`           |
 |                                         | `--collect-all <MODULENAME>`            |
 |                                         | `--version-file <FILE>`                 |


<br>
<br>
<br>


# 🔰 Examples

```yaml
jobs:
  pyinstaller-build:
    runs-on: #<windows-latest / ubuntu-latest / ..... etc>
    steps:
      - name: Create Executable
        uses: sayyid5416/pyinstaller@v1
        with:
          python_ver: '3.6'
          pyinstaller_ver: '==5.13.2'
          spec: 'src/build.spec'
          requirements: 'src/requirements.txt'
          upload_exe_with_name: 'My executable'
          options: --onefile, --name "My App", --windowed
          spec_options: # any custom arguments you want like: `--debug`
```


<br>
<br>
<br>


# 🔰 Main Repository : [sayyid5416/pyinstaller](https://github.com/sayyid5416/pyinstaller)

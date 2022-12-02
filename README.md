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
  - When `.py` file is used, generated `.spec` file will also be uploaded as artifact.
  - Modify your `.spec` file according to your needs.

### 💠 Pyinstaller options
  - You can specify many pyinstaller options in `inputs.options: <comma-seperated-options-here>`.
  - `.py` and `.spec` both supports different kind of options.
  - Check list of all [supported options here](#-inputs--outputs).

### 💠 Python versions
  - You can specify any python version for the executable.

### 💠 Executable uploads
  - You can control if generated executable needs to be uploaded as artifact.
  - You can choose a name of your liking.


<br>


# 🔰 Inputs & Outputs

  - Some **inputs** are **required**, while rest are optional. 
  - Check all inputs & outputs [here](/action.yml).
  - Supported options for `inputs.options`:
    - Ex: `options: -D, -a, --noconsole, --uac-admin`
    - Read more about them [here](https://pyinstaller.org/en/stable/usage.html#options)
    - Options supported for `.py` type `spec`:
      - `--uac-admin`
      - `--uac-uiaccess`
      - `--noupx`
      
      - `--onedir`,                         `-D`
      - `--onefile`,                        `-F`
      - `--ascii`,                          `-a`
      - `--console`,    `--nowindowed`,     `-c`
      - `--windowed`,   `--noconsole`,      `-w`
      
      - `--upx-dir <UPX_DIR>`
      - `--key <KEY>`
      - `--upx-exclude <FILE>`

      - `--name <NAME>`,                    `-n <NAME>`
      - `--icon <FILEICON>`,                `-i <FILEICON>`
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

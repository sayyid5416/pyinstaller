Check all available usable tags [here](../../tags)
<br>
You can also use any major tags like `@v1` for any `@v1.*.*`

# PyInstaller
This action packages the python source code into executables using [pyinstaller](https://pyinstaller.org)
  - Use this action in your workflow to **create** & **upload** executables to GitHub _(as artifacts)_
  - Executable will be based on `jobs.<job-id>.runs-on=<your-os-name>` you uses in your workflow _(see [examples](#examples))_
  - Use [inputs](#inputs) to configure this action
  - Use [outputs](#outputs) to get information from this action


<br>


# Pre-requisites

  <details>
  <summary>Generate .spec file</summary>

  - Clone your repository to your PC
  - Install pyinstaller: `pip install pyinstaller`
  - Run pyinstaller to generate `.spec` file: `pyinstaller <appname>.py`
  - Modify `.spec` file according to your needs
  - Push that `.spec` file to your repo
  </details>


<br>


# Inputs

  ### Required inputs
  - `spec`: Path of your `.spec` file

  ### Optional inputs
  - `python_ver`: Specific python version you want to use _(default: 3.10)_
  - `requirements`: Path of your requirements.txt file
  - `exe_path`: Path where executable will be saved on the runner
  - `upload_exe_with_name`: If passed, An executable with this name will be uploaded _(as artifact)_ in the workflow


<br>


# Outputs
  - `executable_path`: Path where generated executable files are stored on the runner
  - `is_uploaded`: Returns true, if executable was uploaded _(as artifact)_ successfully


<br>


# Examples

```bash
jobs:
  build-job:
    runs-on: <windows-latest / ubuntu-latest / ..... and so on>
    steps:
      - name: Create Executable
        uses: sayyid5416/pyinstaller@v1
        with:
          python_ver: '3.6'
          spec: 'src/build.spec'
          requirements: 'src/requirements.txt'
          upload_exe_with_name: 'My executable'
```

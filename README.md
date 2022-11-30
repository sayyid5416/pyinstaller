Check all available usable tags [here](../../tags)
<br>
You can also use any major tags like `@v1` for any `@v1.*.*`

# PyInstaller
This action packages the python source code into executables using [pyinstaller](https://pyinstaller.org)
  - Use this action in your workflow to **create** & **upload** executables to GitHub _(as artifacts)_
  - Executable will be based on `jobs.<job-id>.runs-on=<your-os-name>` you uses in your workflow _(see [examples](#examples))_
  - Use [inputs](#inputs--outputs) to configure this action
  - Use [outputs](#inputs--outputs) to get information from this action


<br>


# Inputs & Outputs

  - Some **inputs** are **required**, while rest are optional.
  - Check these inputs and outputs in [action.yml](../../action.yml).


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


# Examples

```bash
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

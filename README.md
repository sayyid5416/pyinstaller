# pyinstaller
This action packages the python source code into executables using [pyinstaller](https://pyinstaller.org)
  - Use this action in your workflows to **create** & **upload** executables directly to GitHub
  - Current usable tags available: `@main`
  - Use inputs to confiure this action


# Pre-requisites

  <details>
  <summary>Generate .spec file</summary>

  - Clone your repository to your PC
  - Install pyinstaller: `pip install pyinstaller`
  - Run pyinstaller to generate `.spec` file: `pyinstaller <appname>.py`
  - Modify `.spec` file according to your needs
  - Push that `.spec` file to your repo
  </details>



# Inputs

  ### Required inputs
    - `spec`: Path of your `.spec` file


  ### Optional inputs
    - `python_ver`: Specific python version you want to use _(default: 3.10)_
    - `requirements`: Path of your requirements.txt file
    - `exe_path`: Path where executable will be saved
    - `upload_exe_with_name`: Executable with this name will be uploaded _(If passed)_, as artifact in the workflow



# Outputs
  - `executable_path`: Path where generated executable files are stored
  - `is_uploaded`: Returns true, if executable was uploaded as artifact successfully

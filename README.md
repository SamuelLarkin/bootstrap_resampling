# Confidence Estimation using Bootstrap Resampling

## Install

```sh
python -m pip install git+https://github.com/SamuelLarkin/bootstrap_resampling.git
```

### One file

[PyInstaller Manual](https://pyinstaller.org/en/stable/index.html)
Install `bootstrap-resampling` as a one binary file.

```sh
python -m venv venv
source venv/bin/activate ""
python -m pip install .[install]
pyinstaller --onefile venv/bin/bootstrap-resampling
install dist/bootstrap-resampling ~/.local/bin/
```

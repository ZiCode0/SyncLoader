# SyncLoader
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-brains.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/not-a-bug-a-feature.svg)](https://forthebadge.com)

[comment]: [![License](https://img.shields.io/pypi/l/obspy.svg)](https://pypi.python.org/pypi/obspy/)
[comment]: [![LGPLv3](https://www.gnu.org/graphics/lgplv3-88x31.png)](https://www.gnu.org/licenses/lgpl.html)

[![LICENSE](https://img.shields.io/static/v1?label=LICENSE&message=GPLv3&color=brightgreen&style=for-the-badge&color=grey)](https://www.gnu.org/licenses/lgpl.html)
[![Github watchers](https://img.shields.io/github/watchers/ZiCode0/DrumCorr?label=Watch&style=for-the-badge)](https://github.com/ZiCode0/DrumCorr)


SyncLoader allows you to download source files from remote ssh



## Installation

Simply clone the repository and run the main file:

```bash
# git clone
git clone https://github.com/ZiCode0/SyncLoader.git
cd SyncLoader
# create python virtual environment
python -m venv .venv
# enter venv, linux:
source .venv/bin/activate  # windows: .venv\\Scripts\\activate.bat
# install dependencies
pip install -r requirements.txt
# Copy and edit config file(example/example_config.yaml) to root project folder 
cp example/example_config.yaml config.yaml
# run script
python main
```


## Usage
Example yaml config file: [example/example_config.yaml](https://github.com/ZiCode0/SyncLoader/blob/main/example/example_config.yaml)
### Windows
 ```bash
SyncLoader.bat -s PET -d 2022.02.10
 ```
### Linux
Enter venv and start the program:
 ```bash
source .venv/bin/activate
python main.py -s PET -d 2022.02.10
 ```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
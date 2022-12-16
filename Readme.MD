![Platform](https://img.shields.io/badge/Lang-Python-blue)
![License](https://img.shields.io/github/license/allen870619/ServerMonit0r-server?style=flat)
![Date](https://img.shields.io/github/last-commit/allen870619/ServerMonit0r-server?style=flat)
# ServerMonit0r Server
### This is the server end of [ServerMonit0r](https://github.com/allen870619/ServerMonit0r) written by Python.

## Usage
### Install
```
pip3 install -r requirments.txt
```

### .env
Modified `.env.example` file, and rename to `.env`

### Execute
```
// Please run with admin privilege.
sudo python3 serverMain.py
```

## Available Feature
### Dashboard
|Features|Avbl. Operate System|Memo|
|:-:|:-:|:-:|
|CPU Usage|Windows, Linux, MacOS||
|CPU Temp|Linux, MacOS|MacOS sometimes lost signal|
|CPU Freq.|Window, Linux, MacOS|MacOS will be fixed freq on Intel, Sillicon CPU not test yet.|
|Memory Usage|Windows, Linux, MacOS||
|Network|Windows, Linux, MacOS||
|Uptime|Windows, Linux, MacOS||

### System Info
Most of data works. But some info won't be shown if SDK doesn't provide.

### Charts
Same as Dashboard.

## Knowning Issue
* Most of data are captured by Psutil, so there might have  some data not available for specific OS.
* See [documents](https://psutil.readthedocs.io/en/latest/) for more information.

## Author
[Me :)](https://github.com/allen870619)

# BetterInstaReport Version : 1.0

InstaReport is a script that takes bulk Instagram accounts and uses web automation to report a victim's account in a loop.

The previous version, from which this is forked, did not meet any of its original expectations. There was no loop, and there was poor error handling and retries. This new script has improved functionalities including robust error handling, automatic retries, and continuous looping to report accounts efficiently.

[![forthebadge Made-With-Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### Features
Works On:
<a href="https://t.me/hackerExploits"><img src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white"></a>
<a href="https://t.me/hackerExploits"><img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white"></a>
<a href="https://t.me/hackerExploits"><img src="https://img.shields.io/badge/-kali%20linux-lightgrey"></a>

```
[+] A tool with the capability to automatically report any account.
```

## Requirements
- [Python3 or Above](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

# Usage 

### INSTALLATION [Termux] (Not working for Android right now) 

1. `apt update`
2. `apt upgrade`
3. `pkg install python`
4. `pkg install python3`
5. `pkg install git`
6. `git clone https://github.com/KJdotIO/InstaReport`
7. `cd instareport`
8. `pip install -r requirements.txt`
9. `chmod +x *`
10. Create a file `acc.txt` and run `python main.py` or `python main.py -u <TARGET_USERNAME> -f acc.txt`

### INSTALLATION [Windows]

1. [Download Python](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads)
2. `git clone https://github.com/KJdotIO/InstaReport`
3. `cd instareport`
4. `pip install -r requirements.txt`
5. Create a file `acc.txt` and run `python main.py` or `python main.py -u <TARGET_USERNAME> -f acc.txt`

### INSTALLATION [Kali Linux]

1. `sudo apt install python`
2. `sudo apt install python3`
3. `sudo apt install git`
4. `git clone https://github.com/KJdotIO/InstaReport`
5. `cd instareport`
6. `pip3 install -r requirements.txt`
7. `chmod +x *`
8. Create a file `acc.txt` and run `python main.py` or `python main.py -u <TARGET_USERNAME> -f acc.txt`

Where `acc.txt` is populated with one or more premade accounts that will bot for you. The format is username:password, separated by a new line.
## Disclaimer:
#### This tool is intended for educational and research purposes only. Misuse of this tool for unauthorized access to computer systems or networks is strictly prohibited and may result in legal consequences. The author of this tool takes no responsibility for any damage or harm caused by its usage. It is the user's responsibility to ensure compliance with all applicable laws and regulations while using this tool. By downloading, installing, or using this tool, you agree to use it responsibly and lawfully.

---

### Script Features

This script includes:

- **Automatic Looping**: Continuously reports the target account.
- **Error Handling**: Manages various exceptions such as `NoSuchElementException`, `TimeoutException`, and more.
- **Retry Mechanism**: Retries failed operations to ensure completion.
- **Multiprocessing**: Handles multiple accounts simultaneously for efficient processing.
- **WebDriver Management**: Manages WebDriver sessions effectively, including initialization and cleanup.

The script employs Selenium WebDriver for automating web interactions, ensuring that the account reporting process is robust and reliable.

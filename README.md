# Secure FTP

This is a Python script that provides a command-line interface to securely connect to an FTP server, allowing users to perform various operations like listing directory contents, downloading files, uploading files, and disconnecting from the server. The script supports both FTP and SFTP protocols and includes error handling for robustness.

## Features

- Connect to FTP server securely using FTP or SFTP protocol.
- List directory contents on the remote server.
- Download files from the remote server to the local machine.
- Upload files from the local machine to the remote server.
- Disconnect from the FTP server.

## Requirements

- Python 3.x
- `ftplib` library (usually included in Python standard library)
- `paramiko` library for SFTP support

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries using pip:
```
pip install paramiko
```

3. Download or clone the project repository to your local machine.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script by executing the following command:
```
python secure_ftp.py
```

4. Follow the prompts to enter the FTP server details, such as hostname, port, username, and password.
5. Once connected, choose from the menu options to perform desired operations.

## Example

```sh
$ python secure_ftp.py
FTP Host: example.com
Port (default 21 for FTP, 22 for SFTP): 22
Username: your_username
Password: your_password

Connected successfully!

1. List Directory
2. Download File
3. Upload File
4. Disconnect
Enter your choice: 1
drwxr-xr-x   3 user group   4096 May  6 10:23 directory1
-rw-r--r--   1 user group   1234 May  5 15:32 file1.txt
...

Enter your choice: 4
Disconnected successfully!
```

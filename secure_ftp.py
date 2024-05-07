import os
from ftplib import FTP_TLS
import paramiko

class SecureFTPClient:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.protocol = None

    def connect(self):
        try:
            self.protocol = FTP_TLS()  # We'll decide on the protocol in the connect method
            self.protocol.connect(self.host, self.port)
            self.protocol.login(user=self.username, passwd=self.password)
            self.protocol.prot_p()  # Set up secure data connection
            print("Connected successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def list_directory(self):
        try:
            self.protocol.retrlines('LIST')
        except Exception as e:
            print(f"Error: {e}")

    def download_file(self, remote_filename, local_filename):
        try:
            with open(local_filename, 'wb') as f:
                self.protocol.retrbinary(f'RETR {remote_filename}', f.write)
            print(f"File '{remote_filename}' downloaded to '{local_filename}'")
        except Exception as e:
            print(f"Error: {e}")

    def upload_file(self, local_filename, remote_filename):
        try:
            with open(local_filename, 'rb') as f:
                self.protocol.storbinary(f'STOR {remote_filename}', f)
            print(f"File '{local_filename}' uploaded to '{remote_filename}'")
        except Exception as e:
            print(f"Error: {e}")

    def disconnect(self):
        try:
            self.protocol.quit()
            print("Disconnected successfully!")
        except Exception as e:
            print(f"Error: {e}")


def main():
    host = input("FTP Host: ")
    port = int(input("Port (default 21 for FTP, 22 for SFTP): "))
    username = input("Username: ")
    password = input("Password: ")

    ftp_client = SecureFTPClient(host, port, username, password)
    ftp_client.connect()

    while True:
        print("\n1. List Directory\n2. Download File\n3. Upload File\n4. Disconnect")
        choice = input("Enter your choice: ")

        if choice == '1':
            ftp_client.list_directory()
        elif choice == '2':
            remote_file = input("Enter remote filename: ")
            local_file = input("Enter local filename to save: ")
            ftp_client.download_file(remote_file, local_file)
        elif choice == '3':
            local_file = input("Enter local filename: ")
            remote_file = input("Enter remote filename to save: ")
            ftp_client.upload_file(local_file, remote_file)
        elif choice == '4':
            ftp_client.disconnect()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

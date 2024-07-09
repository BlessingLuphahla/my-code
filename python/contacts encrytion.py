from pathlib import Path
from cryptography.fernet import Fernet

location = Path(r'C:\Users\Admin\Desktop\contacts\data.txt')
THE_KEY = b'urbcyyoFKJ0pKPsEiyD0mkGxLzCAVRm51P3PaK-MBok='


def encrypt_file(file_location):
    with open(file_location, 'rb+') as contacts:
        info = contacts.read()
        key = THE_KEY
        key = Fernet(key)
        info = key.encrypt(info)

        contacts.seek(0)
        contacts.write(info)
    return 'done'


def decrypt_file(file_location):
    with open(file_location, 'rb+') as contacts:
        source_info = contacts.read()
        the_key = THE_KEY
        key = Fernet(the_key)
        contacts.seek(0)
        info = b'\n\n' + b'_' * 100 + b'\n' + key.decrypt(source_info) + b'\n' + b'_' * 100 + b'\n' * 3
        contacts.write(info)
    return 'done'


def main():
    done = decrypt_file(location)
    print(done)


if __name__ == '__main__':
    main()

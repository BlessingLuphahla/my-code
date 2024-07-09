from qrcode import QRCode
from pathlib import Path


class MakeCustomQR:
    def __init__(self, location, data: str):
        self.location = location
        self.data = data

        self.save_location = self.location / f'{self.data[::-1][:5].replace(' ', '').lower()}.png'

    def create_and_save(self):
        qr = QRCode()
        qr.add_data(self.data)
        qr.make(fit=True)
        qr = qr.make_image()
        qr.save(self.save_location)


def main():
    data = 'i m redd axe'
    location = Path(r'C:\Users\Admin\Desktop\qr_codes')
    instance = MakeCustomQR(location, data)
    instance.create_and_save()


if __name__ == '__main__':
    main()

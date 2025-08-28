# QR-Coder

QR-Coder is a Flask web application for generating and scanning QR codes. It provides a simple interface to create QR codes from text, scan uploaded images for QR codes, and perform live QR code scanning using your webcam.

## Features
- Generate QR codes from user input
- Save generated QR codes as images
- Scan uploaded images for QR codes and display decoded data
- Live QR code scanning using a webcam
- Download generated QR codes
- Simple and modern UI

## Installation
1. Clone the repository:
   ```powershell
   git clone https://github.com/wajidkorkani/QR-Coder.git
   cd QR-Coder/Src
   ```
2. Install dependencies:
   ```powershell
   pip install flask qrcode pillow pyzbar opencv-python
   ```

## Usage
1. Run the Flask app:
   ```powershell
   python app.py
   ```
2. Open your browser and go to `http://localhost:5000`
3. Use the navigation to generate or scan QR codes

## Folder Structure
```
QR-Coder/
├── LICENSE
├── README.md
└── Src/
    ├── app.py                # Main Flask application
    ├── App.class             # (Binary, not used in Python)
    ├── image.jpg             # Sample image
    ├── index.css, index.html # Static and template files
    ├── static/               # Static assets (CSS, images)
    │   ├── css/
    │   └── images/
    └── Templates/            # HTML templates
        ├── about.html
        ├── generate.html
        ├── generateQrImage.html
        ├── index.html
        ├── liveScan.html
        ├── scan.html
        └── showQRCode.html
```

## Dependencies
- Flask
- qrcode
- Pillow
- pyzbar
- OpenCV (opencv-python)

## License
MIT License

See `LICENSE` for details.
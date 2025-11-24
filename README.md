# QR Code Generator

A simple Python-based QR code generator that creates custom-styled QR codes from any text or URL input.

## Features

- Generate QR codes from any text or URL
- Custom color styling (red fill on white background)
- Easy-to-use command-line interface
- Saves output as PNG image
- Configurable QR code parameters

## Requirements

- Python 3.x
- qrcode library

## Installation

Install the required library using pip:

```bash
pip install qrcode[pil]
```

## Usage

1. Run the script:
```bash
python qr_code.py
```

2. Enter the data you want to encode when prompted:
```
enter the data you want to generate qr for: google.com
```

3. The QR code will be saved as `MyQRCode2.png` in the current directory

## Configuration

You can customize the QR code by modifying these parameters:

- **version**: Controls the size (1-40, where 1 is 21x21 modules)
- **box_size**: Size of each box in pixels (default: 10)
- **border**: Border thickness in boxes (default: 5)
- **fill_color**: QR code color (default: 'red')
- **back_color**: Background color (default: 'white')

## Example

Input: `https://www.google.com`

Output: A red and white QR code saved as `MyQRCode2.png`

## Use Cases

- Share website URLs
- Encode contact information
- Generate WiFi connection codes
- Create product labels
- Event ticketing
- Business cards

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available for personal and commercial use.

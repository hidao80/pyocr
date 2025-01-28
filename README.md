# pyocr

A simple OCR script.

## Overview

This script uses [EasyOCR](https://github.com/JaidedAI/EasyOCR) to extract text from images. It supports both Japanese (`ja`) and English (`en`) languages and provides rotation handling for better text recognition.

## Features

- Extracts text from images in Japanese and English.
- Handles image rotation for improved accuracy.
- Lightweight and easy to use.

## Requirements

- Python 3.6 or later
- EasyOCR library

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. Install the required dependencies:
    ```bash
    pip install easyocr
    ```

## Usage

Run the script with the path to an image file as an argument:

```bash
python ocr.py <image_path>
```

### Example

```bash
python ocr.py sample_image.jpg
```

The output will display the extracted text.

## Notes

- Ensure the image contains text in Japanese or English for accurate recognition.
- The script handles rotation (`90 degrees`) for better text alignment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

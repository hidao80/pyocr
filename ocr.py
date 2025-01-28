import easyocr
import sys

# Only need to select the languages once
reader = easyocr.Reader(['ja','en'], gpu=False)
if len(sys.argv) != 2:
    print("Usage: python ocr.py <image_path>")
    sys.exit(1)

path = sys.argv[1]

# Consider image rotation
print(reader.readtext(path, rotation_info=[90], paragraph=True, detail=0, mag_ratio=1.05))

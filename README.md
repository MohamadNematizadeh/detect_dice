# detect dice 🎲
detect_dice is a simple and fast dice detection library made in Python based on cv2(opencv. This library allows you to perform dice detection operations on images for you

## Install

Install the package with pip in a Python>=3.8 environment:

```bash
pip install detect_dice
```

## Usage
### CLI

Pinterest Crawler may be used directly in the Command Line Interface (CLI):

```bash
python3 detector_dice.py --input dice.jpg --output output.jpg

```

### Python

```python
from detect_dice import detect_dice
url = detect_dice.detect_dice(image_path="/content/۳.jpg",output_path="/content/1.jpg")
```

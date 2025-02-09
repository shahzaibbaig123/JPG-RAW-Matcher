# JPG-RAW-Matcher 📸➡️📁

A Python script to match JPG files with their corresponding RAW counterparts and copy them to a specified folder. Supports multiple RAW formats across popular camera brands.

## Features
- 🖼️ Matches JPGs with RAW files by filename
- 📋 Interactive CLI for selecting camera brands/formats
- 🗂️ Supports 15+ RAW formats (CR2, NEF, ARW, RAF, etc.)
- 🖥️ Cross-platform (Windows/macOS/Linux)
- 🛠️ Case-insensitive filename matching
- 📊 Progress tracking and error handling

## Supported Formats 📁

| Brand       | RAW Extensions |
|-------------|----------------|
| Canon       | .cr2, .cr3     |
| Nikon       | .nef, .nrw     |
| Sony        | .arw           |
| Fujifilm    | .raf           |
| Panasonic   | .rw2           |
| Olympus     | .orf           |
| Pentax      | .pef, .dng     |
| Leica       | .dng, .raw     |
| Sigma       | .x3f           |
| Hasselblad  | .3fr, .fff     |

## Prerequisites
- Python 3.6 or newer

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/JPG-RAW-Matcher.git
   cd JPG-RAW-Matcher
   ```
2. Run the script:
   ```bash
    python copy_raws.py
   ```  

4. Follow the prompts:

- Enter paths to your JPGS, RAWS, and Found folders
- Select your camera brand from the list
- Choose your specific RAW format

5. The script will copy matching RAW files to the "Found" folder



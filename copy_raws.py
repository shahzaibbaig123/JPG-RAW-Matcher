import os
import shutil

def select_raw_format():
    formats = {
        "Canon": [
            ("CR2", "Canon Raw 2"),
            ("CR3", "Canon Raw 3, used in newer models")
        ],
        "Nikon": [
            ("NEF", "Nikon Electronic Format"),
            ("NRW", "Nikon Raw, used in some compact cameras")
        ],
        "Sony": [
            ("ARW", "Sony Alpha Raw")
        ],
        "Fujifilm": [
            ("RAF", "Fujifilm Raw")
        ],
        "Panasonic": [
            ("RW2", "Panasonic Raw")
        ],
        "Olympus": [
            ("ORF", "Olympus Raw Format")
        ],
        "Pentax": [
            ("PEF", "Pentax Electronic Format"),
            ("DNG", "Digital Negative, used in some models")
        ],
        "Leica": [
            ("DNG", "Digital Negative, commonly used in Leica cameras"),
            ("RAW", "Leica-specific raw format in some models")
        ],
        "Sigma": [
            ("X3F", "Sigma X3F, used in Foveon sensor cameras")
        ],
        "Hasselblad": [
            ("3FR", "Hasselblad Raw"),
            ("FFF", "Hasselblad Raw")
        ]
    }

    print("\nAvailable camera brands:")
    brands = list(formats.keys())
    for i, brand in enumerate(brands, 1):
        print(f"{i}. {brand}")

    # Get brand selection
    while True:
        try:
            brand_choice = int(input("\nEnter brand number: "))
            if 1 <= brand_choice <= len(brands):
                selected_brand = brands[brand_choice - 1]
                break
            print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Get format selection
    brand_formats = formats[selected_brand]
    print(f"\nAvailable formats for {selected_brand}:")
    for i, (ext, desc) in enumerate(brand_formats, 1):
        print(f"{i}. {ext} - {desc}")

    while True:
        try:
            format_choice = int(input("\nEnter format number: "))
            if 1 <= format_choice <= len(brand_formats):
                selected_ext, selected_desc = brand_formats[format_choice - 1]
                return selected_ext
            print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def copy_raw_files():
    # Get folder paths
    jpgs_folder = input("Enter path to JPGS folder: ").strip()
    raws_folder = input("Enter path to RAWS folder: ").strip()
    found_folder = input("Enter path to Found folder: ").strip()

    # Validate paths
    if not all(map(os.path.isdir, [jpgs_folder, raws_folder])):
        print("Error: JPGS or RAWS folder does not exist")
        return

    # Create found folder if needed
    os.makedirs(found_folder, exist_ok=True)

    # Get raw format selection
    raw_extension = select_raw_format()
    raw_ext_lower = raw_extension.lower()

    # Build case-insensitive index of raw files
    raw_files = {}
    for filename in os.listdir(raws_folder):
        base, ext = os.path.splitext(filename)
        ext_clean = ext.lstrip('.').lower()
        key = base.lower()
        if key not in raw_files:
            raw_files[key] = []
        raw_files[key].append((ext_clean, filename))

    # Process files
    copied = 0
    for jpg in os.listdir(jpgs_folder):
        if not jpg.lower().endswith('.jpg'):
            continue
            
        base_name = os.path.splitext(jpg)[0]
        search_key = base_name.lower()

        if search_key in raw_files:
            for ext, raw_file in raw_files[search_key]:
                if ext == raw_ext_lower:
                    src = os.path.join(raws_folder, raw_file)
                    dst = os.path.join(found_folder, raw_file)
                    shutil.copy2(src, dst)
                    print(f"Copied: {raw_file}")
                    copied += 1
                    break

    print(f"\nOperation complete. {copied} files copied to {found_folder}")

if __name__ == "__main__":
    copy_raw_files()
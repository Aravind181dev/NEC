from PIL import Image
from pathlib import Path

INPUT_FOLDER = Path("static/website/images/products-original")
OUTPUT_FOLDER = Path("static/website/images/products")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

MAX_WIDTH = 720
MAX_HEIGHT = 825
QUALITY = 80

valid_extensions = [".jpg", ".jpeg", ".png"]

converted_count = 0
skipped_count = 0

for image_path in INPUT_FOLDER.rglob("*"):
    if image_path.is_dir():
        continue

    if image_path.suffix.lower() not in valid_extensions:
        skipped_count += 1
        print(f"Skipped: {image_path}")
        continue

    relative_path = image_path.relative_to(INPUT_FOLDER)
    output_path = OUTPUT_FOLDER / relative_path.with_suffix(".webp")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        img = Image.open(image_path).convert("RGB")
        img.thumbnail((MAX_WIDTH, MAX_HEIGHT))
        img.save(output_path, "WEBP", quality=QUALITY, optimize=True)

        converted_count += 1
        print(f"Converted: {image_path.name} -> {output_path.name}")

    except Exception as e:
        skipped_count += 1
        print(f"Error converting {image_path}: {e}")

print("-----------------------------")
print(f"Total converted: {converted_count}")
print(f"Total skipped/error: {skipped_count}")
print("-----------------------------")
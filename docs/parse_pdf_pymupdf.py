import fitz  # PyMuPDF
from pathlib import Path
import json


def extract_images_from_pdf(pdf_path, output_dir):
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    image_dir = output_dir / "images"
    image_dir.mkdir(parents=True, exist_ok=True)
    metadata = []

    doc = fitz.open(pdf_path)
    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list, 1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"page_{page_index+1}_img_{img_index}.{image_ext}"
            image_path = image_dir / image_filename
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
            metadata.append({
                "page": page_index + 1,
                "img_index": img_index,
                "file": str(image_path.relative_to(output_dir)),
                "width": base_image.get("width"),
                "height": base_image.get("height"),
                "ext": image_ext
            })
    # Save metadata
    with open(output_dir / "metadata_pymupdf.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    print(f"Extracted {len(metadata)} images from {pdf_path}")

if __name__ == "__main__":
    extract_images_from_pdf(
        pdf_path=Path(__file__).parent / "nist.ai.100-1.pdf",
        output_dir=Path(__file__).parent / "data"
    )

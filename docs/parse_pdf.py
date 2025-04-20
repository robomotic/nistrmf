import logging
import json
from pathlib import Path
import pdfplumber
from pdf2image import convert_from_path
from PIL import Image
import io

# Configure logging
logging.basicConfig(level=logging.INFO)
_log = logging.getLogger(__name__)

def parse_nist_pdf():
    # Setup paths
    base_dir = Path(__file__).parent
    pdf_path = base_dir / 'nist.ai.100-1.pdf'
    data_dir = base_dir / 'data'
    image_dir = data_dir / 'images'
    text_dir = data_dir / 'text'
    
    # Create directories
    for dir_path in [data_dir, image_dir, text_dir]:
        dir_path.mkdir(exist_ok=True)
    
    metadata = {
        'pages': [],
        'images': [],
        'text_sections': [],
        'figures': []
    }

    try:
        _log.info(f"Starting conversion of {pdf_path}")
        
        # Convert PDF pages to images
        pages = convert_from_path(pdf_path, dpi=300)
        for i, page in enumerate(pages, 1):
            page_image_path = image_dir / f'page_{i}.png'
            page.save(str(page_image_path), 'PNG')
            metadata['pages'].append({
                'number': i,
                'image_file': str(page_image_path.relative_to(data_dir)),
                'width': page.width,
                'height': page.height
            })

        # Extract text and figures using pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages, 1):
                # Extract text
                text = page.extract_text()
                if text:
                    text_file = text_dir / f'page_{i}.txt'
                    with open(text_file, 'w', encoding='utf-8') as f:
                        f.write(text)
                    metadata['text_sections'].append({
                        'page': i,
                        'file': str(text_file.relative_to(data_dir)),
                        'char_count': len(text)
                    })

                # Extract images
                images = page.images
                for img_num, img in enumerate(images, 1):
                    try:
                        if 'stream' in img:
                            image_data = img['stream'].get_data()
                            image = Image.open(io.BytesIO(image_data))
                            image_path = image_dir / f'figure_p{i}_{img_num}.png'
                            image.save(str(image_path), format='PNG')
                            metadata['figures'].append({
                                'id': f'p{i}_{img_num}',
                                'page': i,
                                'file': str(image_path.relative_to(data_dir)),
                                'bbox': img['bbox'],
                                'width': image.width,
                                'height': image.height
                            })
                    except Exception as e:
                        _log.warning(f"Error extracting image {img_num} from page {i}: {str(e)}")

                # Extract raster images
                raster_images = page.objects.get('Im', [])
                for img_num, img in enumerate(raster_images, 1):
                    try:
                        if hasattr(img, 'stream'):
                            raw_image = img.stream.get_data()
                            image_path = image_dir / f'raster_p{i}_{img_num}.png'
                            with open(image_path, 'wb') as f:
                                f.write(raw_image)
                            
                            metadata['images'].append({
                                'id': f'raster_p{i}_{img_num}',
                                'page': i,
                                'file': str(image_path.relative_to(data_dir)),
                                'type': 'raster'
                            })
                    except Exception as e:
                        _log.warning(f"Error extracting raster image {img_num} from page {i}: {str(e)}")

        # Save metadata
        with open(data_dir / 'metadata.json', 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)

        _log.info(f"Extraction complete: {len(metadata['pages'])} pages, "
                 f"{len(metadata['figures'])} figures, {len(metadata['images'])} raster images")

    except Exception as e:
        _log.error(f"Error processing PDF: {str(e)}")
        raise

if __name__ == '__main__':
    parse_nist_pdf()
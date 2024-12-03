from pdf2image import convert_from_path
from PIL import Image, ImageOps
import img2pdf
import os

def invert_color(filepath, threshold=160, dpi=450):  # Added DPI parameter
    """
    Invert the colors of a PDF with high resolution output.

    Parameters:
    - filepath (str): Path to the input PDF file
    - threshold (int): Threshold for binary conversion
    - dpi (int): Resolution of output images (default 300)
    """
    try:
        # Convert PDF pages to images with specified DPI
        images = convert_from_path(filepath, dpi=dpi)

        idx_counter = []
        for idx, img in enumerate(images):
            inverted_img = ImageOps.invert(img.convert('RGB'))
            
            if inverted_img.mode != 'RGB':
                inverted_img = inverted_img.convert('RGB')
            
            r, g, b = inverted_img.split()
            
            # Binary conversion
            r = r.point(lambda p: 255 if p > threshold else 0)
            g = g.point(lambda p: 255 if p > threshold else 0)
            b = b.point(lambda p: 255 if p > threshold else 0)
            
            thresholded_img = Image.merge('RGB', (r, g, b))
            
            # Save with high quality
            output_filename = f'output{idx}.jpeg'
            thresholded_img.save(output_filename, quality=100, dpi=(dpi, dpi))
            idx_counter.append(output_filename)

        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(idx_counter))
            
        for filename in idx_counter:
            os.remove(filename)
        
        print(f"Converted PDF saved at {dpi} DPI as output.pdf")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        for filename in idx_counter:
            if os.path.exists(filename):
                os.remove(filename)
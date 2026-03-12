import os
from PIL import Image
from rembg import remove
import io

class BackgroundRemover:
    """Core class to handle background removal using rembg library."""
    
    @staticmethod
    def remove_background(input_path, output_path):
        """
        Removes background from a single image.
        
        Args:
            input_path (str): Path to the input image file.
            output_path (str): Path where the processed image will be saved.
        """
        try:
            with open(input_path, 'rb') as i:
                input_image = i.read()
                output_image = remove(input_image)
                
                with open(output_path, 'wb') as o:
                    o.write(output_image)
            return True
        except Exception as e:
            print(f"Error processing {input_path}: {e}")
            return False

    @staticmethod
    def batch_process(input_dir, output_dir):
        """
        Processes all images in a directory.
        
        Args:
            input_dir (str): Directory containing input images.
            output_dir (str): Directory to save processed images.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        supported_extensions = ('.jpg', '.jpeg', '.png', '.webp')
        files = [f for f in os.listdir(input_dir) if f.lower().endswith(supported_extensions)]
        
        results = []
        for filename in files:
            input_path = os.path.join(input_dir, filename)
            # Save as PNG to preserve transparency
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_dir, output_filename)
            
            success = BackgroundRemover.remove_background(input_path, output_path)
            results.append((filename, success))
            
        return results

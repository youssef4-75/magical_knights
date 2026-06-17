from PIL import Image
from pathlib import Path
from typing import Union
import os

def remove_background_from_folder(folder_path: Union[str, Path]) -> None:
    """
    Recursively go through all files in a folder and remove backgrounds from images.
    """
    folder = Path(folder_path)
    print(folder.absolute())
    for item in folder.rglob('*'):
        if item.is_file() and item.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            print("found one")
            try:
                img = Image.open(item).convert('RGBA')
                
                # Find dominant color (simple background removal)
                data = img.getdata()
                bg_color = data[0]  # Assume top-left pixel is background
                
                new_data = []
                for pixel in data:
                    if pixel[:3] == bg_color[:3]:
                        new_data.append((255, 255, 255, 0))  # Transparent
                    else:
                        new_data.append(pixel)
                
                img.putdata(new_data)
                img.save(item)  # Overwrite or save with different name
                print(f"Processed: {item}")
                
            except Exception as e:
                print(f"Error processing {item}: {e}")


if __name__ == "__main__":
    
    remove_background_from_folder("assets/anim_set01")
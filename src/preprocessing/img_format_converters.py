import os
import rawpy
import pillow_heif
from PIL import Image

def convert_dng_to_png(input_folder, output_folder):
    """
    Converts all the .DNG files in input_folder to .PNG files,
    and saves those .PNG files in output_folder
    """

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process all .DNG files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".dng"):
            print("Converting " + str(filename) + "...")
            dng_path = os.path.join(input_folder, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(output_folder, png_filename)

            # Open DNG file
            with open(dng_path, "rb") as dng_file:
                dng_file.seek(0)  # Ensure file pointer is at the beginning
                with rawpy.imread(dng_file) as raw:
                    rgb_image = raw.postprocess()  # Process RAW image

            # Convert to Pillow image
            image = Image.fromarray(rgb_image)

            # Ensure no alpha channel (convert to RGB)
            if image.mode in ("RGBA", "LA"):
                image = image.convert("RGB")

            image.save(png_path, "PNG")
            print(f"Converted: {filename} -> {png_filename}")


def convert_heic_to_png(input_folder, output_folder):
    """
    Converts all the .HEIC files in input_folder to .PNG files,
    and saves those .HEIC files in output_folder
    """

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process all .HEIC files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic") and not filename.lower().startswith("._"):
            print("Converting " + str(filename) + "...")
            heic_path = os.path.join(input_folder, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(output_folder, png_filename)

            # Open HEIC file
            with open(heic_path, "rb") as heic_file:
                heic_file.seek(0)  # Ensure file pointer is at the beginning
                heif_image = pillow_heif.open_heif(heic_file)
          
            image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)

            # Ensure no alpha channel
            if image.mode in ("RGBA", "LA"):
                image = image.convert("RGB")

            image.save(png_path, "PNG")
            print(f"Converted: {filename} -> {png_filename}")

def convert_jpg_to_png(input_folder, output_folder):
    """
    Converts all the .JPG files in input_folder to .PNG files,
    and saves those .PNG files in output_folder
    """

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process all .JPG or .JPEG files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".JPG", ".JPEG")):
            print("Converting " + str(filename) + "...")
            jpg_path = os.path.join(input_folder, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(output_folder, png_filename)

            # Open JPG file
            with Image.open(jpg_path) as img:
                img = img.convert("RGB")  # Ensure no transparency
                img.save(png_path, "PNG")
                print(f"Converted: {filename} -> {png_filename}")
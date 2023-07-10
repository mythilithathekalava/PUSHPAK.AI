import os

image_folder = "/home/hp/Documents/Annotation/images"

for image_file in os.listdir(image_folder):
    if image_file.endswith(".jpg") or image_file.endswith(".png"):
        image_name = os.path.splitext(image_file)[0]
        txt_file = image_name + ".txt"
        txt_path = os.path.join(image_folder, txt_file)
        
        if not os.path.exists(txt_path):
            image_path = os.path.join(image_folder, image_file)
            os.remove(image_path)
            print(f"Removed {image_file}")
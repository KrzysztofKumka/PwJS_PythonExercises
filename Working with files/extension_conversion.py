from PIL import Image

def photo_conversion(file):
    image = Image.open(file)  # jpg
    new_name = str(file[:6]) + "_PNG.png"
    image.save(new_name)


if __name__ == "__main__":
    file = "photo1.jpg"
    photo_conversion(file)
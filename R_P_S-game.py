import PIL.Image
# ascii character used to build the output text
ascii_charc = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# resize image according to a new width
def resize_image(image, new_width = 100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel ti=o grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
def main():
    path = input("enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")

main()
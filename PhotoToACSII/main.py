from PIL import Image

#Sorted from darkest symbol to lightest
symbols = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

#Convert the pixels to the proper corresponding ASCII text
def pixel_to_ascii(img):
    pixels = img.getdata()
    ascii_str = ""
    for pixel in pixels:
        #Divid the pixel
        ascii_str += symbols[pixel//25]
    return ascii_str

#Converts image to grayscale so we can get pixel data
def Convert_grayscale(img):
    return img.convert("L")

#Resizing image by calculating aspect ratio and halving it to reduce size
def resize(img):
    new_width = 100
    width, height = img.size
    aspect_ratio = height/width
    new_height = aspect_ratio * new_width * 0.5
    img = img.resize((new_width, int(new_height)))
    return img

def main():
    file = input(r"Enter the path to the image: ")
    try:
        img = Image.open(file)
    except:
        print("Invalid Path")

    img = resize(img)

    #convert image to grayscale image
    grayscale_image = Convert_grayscale(img)

    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(grayscale_image)
    img_width = grayscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    #save the string to a txt file and writes to it.
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

main()
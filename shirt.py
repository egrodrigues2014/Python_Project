# CS50 P-Shirt

import sys
import os
from PIL import Image, ImageOps


def main():
    check_command_line_args()
    print(sys.argv)
    paste_image()


def check_command_line_args():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit()
    else:
        file1 = os.path.splitext(sys.argv[1])
        file2 = os.path.splitext(sys.argv[2])
        extension = [".jpeg", ".jpg", ".png"]
        # print(argv1[1],argv2[1])
        if file1[1] not in extension:
            print("Invalid input")
            sys.exit()
        elif file2[1] not in extension:
            print("Invalid output")
            sys.exit()
        elif file1[1].lower() != file2[1].lower():
            print("")
            sys.exit("Input and output have different extensions")

    # elif not (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png")):
    #     print(f"{sys.argv[1]} is not a jpg,jpeg or png file")
    #     sys.exit()
    # elif not (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".png")):
    #     print(f"{sys.argv[2]} is not a jpg,jpeg or png file")
    #     sys.exit()


def paste_image():
    # Open image using Image module
    shirt = Image.open("shirt.png")

    try:
        photo = Image.open(sys.argv[1])
    except:
        sys.exit("Input does not exist")

    # Get size of shirt
    shirt_size = shirt.size

    # resize and crop photo with shirt size
    new_photo = ImageOps.fit(photo, shirt_size)

    # Paste a shirt inside a photo
    new_photo.paste(shirt, shirt)

    # Save a new photo
    new_photo.save(sys.argv[2], quality=95)


if __name__ == "__main__":
    main()

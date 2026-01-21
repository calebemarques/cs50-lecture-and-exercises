from PIL import Image
from PIL import ImageFilter



def main():
   with Image.open("in.jpeg") as img:
         img = img.rotate(0)
         img = img.filter(ImageFilter.FIND_EDGES)
        # img = img.filter(ImageFilter.BLUR)
         img.save("out.jpeg")
         print(img)

   img.close()

main()

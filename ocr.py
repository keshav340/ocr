from PIL import Image
image = Image.open("notes.png")
display(image)
import pytesseract


#by icreasing base width.
import PIL
basewidth =700 
image = Image.open("notes.png")

#we wnant to get the correct aspect ratio , so we can do by taking base width divoded by its actual width of image.
wpercent =(basewidth/float(image.size[0])) 
hsize = int((float(image.size[1])* float(wpercent))) 
image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
image.save('note1.png')

text = pytesseract.image_to_string(Image.open('note1.png'))
print(text)

image = Image.open("notes.png")
image = image.convert('L')
image.save('greyscale.notes2.png')
text = pytesseract.image_to_string(Image.open('greyscale.notes2.png'))
print(text)


#by convert function
image = Image.open("notes.png").convert('1')
image.save('blacknotes.png')

text = pytesseract.image_to_string(Image.open('blacknotes.png'))
print(text)

#binarisation
def binarize(image_to_transform, thresold):
    output_image = image_to_transform.convert("L")
    for x in range( output_image.width):
        for y in range( output_image.height):
            #for a given pixel w,h  let check the value against its thresold
            if  output_image.getpixel((x,y))< thresold:
                output_image.putpixel((x,y), 0)
            else:
                 output_image.putpixel((x,y), 255)
                    
    return output_image 

for thres in range(240,260):
    print("trying with thresold" + str(thres))
    display(binarize(Image.open('notes.png'), thres))
    print(pytesseract.image_to_string(binarize(Image.open('notes.png'), thres)))#it increase the accuracy not much


#by increasing contrast
im1 = image.filter(ImageFilter.EDGE_ENHANCE_MORE) 
display(im1)
im2 = im1.save("notes.png") 
text = pytesseract.image_to_string(Image.open('notes.png'))
print(text)

oldName = "spritesheet.png"
newName = "new_spritesheet.png"
leftStripes = 4

width = 80
spriteHeight = 20

from PIL import Image, ImageDraw
from glob import glob
images = glob("*.png")
images.extend(glob("*.jpg"))
images.extend(glob("*.jpeg"))
images.extend(glob("*.tiff"))
images.extend(glob("*.gif"))
images.extend(glob("*.bmp"))
images.remove(oldName)
images.remove(newName)
print(images)
oldSheet = Image.open(oldName)
newSheet = Image.new('RGB', (width, oldSheet.height + len(images)*spriteHeight), color='white')
newSheet.paste(oldSheet, (0,0))

for i, imageName in enumerate(images):
    newSheet.paste(Image.open(imageName), (leftStripes,oldSheet.height + i*spriteHeight))

draw = ImageDraw.Draw(newSheet)
for i in range(leftStripes+1):
    draw.line([(i,0),(i,newSheet.height-1)], fill=oldSheet.getpixel((i,0)))
    
newSheet.save(newName)

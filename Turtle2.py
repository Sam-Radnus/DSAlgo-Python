from images import Image
def blackAndWhite(image):
    y = image.getHeight()
    x = image.getWidth()
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for i in range(y):
        for j in range(x):
            (r, g, b) = image.getPixel(j, i)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(j, i, blackPixel)
            else:
                image.setPixel(j, i, whitePixel)

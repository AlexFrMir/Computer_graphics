import array


class FHDRaster:
    def __init__(self, name, width, height, maxval):
        # PPM header
        self.name = name
        self.width = width
        self.height = height
        self.maxval = maxval
        self.ppm_header = f'P6 {self.width} {self.height} {self.maxval}\n'

        # PPM image data  (filled with blue)
        self.image = array.array('B', [0, 0, 0] * self.width * self.height)

#    def drawline(self, x1, x2, y1, y2, r, g, b):
#        for y in range(y1, y2):
#            for x in range(x1, x2):
#                index = 3 * (y * self.width + x)
#                self.image[index] = r
#                self.image[index + 1] = g
#                self.image[index + 2] = b
#        print(self.image)
#        # Save the PPM image as a binary file
#        with open(self.name + '.ppm', 'wb') as f:
#            f.write(bytearray(self.ppm_header, 'ascii'))
#            self.image.tofile(f)

    def drawline(self, x1, y1, x2, y2, r, g, b):
        m = (y2 - y1) / (x2 - x1)
        be = y1 - (m * x1)
        dx = x2 - x1
        dy = y2 - y1
        p = 2 * dy - dx

        print("p",  p)
        updateup = 2 * dy
        updateright = 2 * dy - 2 * dx
        self.setpixel(x1, y1, int(r), int(g), int(b))
        self.setpixel(x2, y2, r, g, b)
        y = m * x1 + be
        for x in range(x1+1, x2):
            if p < 0:
                y = y + 1
                p += updateup
            else:
                p += updateright

                print("p", p)
            updateup = 2 * dy
            self.setpixel(int(x), int(y), int(r), int(g), int(b))

    def setpixel(self, x, y, r, g, b):
        index = 3 * (y * self.width + x)
        self.image[index] = r
        self.image[index + 1] = g
        self.image[index + 2] = b
        with open(self.name + '.ppm', 'wb') as f:
            f.write(bytearray(self.ppm_header, 'ascii'))
            self.image.tofile(f)


if __name__ == '__main__':
    raster = FHDRaster("lines", 1920, 1080, 255)
    raster.drawline(1, 1, 2, 3, 255, 255, 255)
    print("hello world ")

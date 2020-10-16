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

    def drawandseparatieline(self, x1, y1, x2, y2, n_divide, r, g, b):
        print("Separating line with points (", x1, ", ", y1, ") -> (", x2, ", ", y2, ")")
        flag_opt1 = False
        flag_opt2 = False
        flag_opt3 = False
        if x1 != x2 and y1 != y2:
            y_temp = (y2-y1) / n_divide
            x_temp = (x2-x1) / n_divide
            flag_opt1 = True
        elif x1 != x2 and y1 == y2:
            x_temp = (x2-x1) / n_divide
            y_temp = 0
            flag_opt2 = True
        elif x1 == x2 and y1 != y2:
            x_temp = 0
            y_temp = (y2-y1) / n_divide
            flag_opt3 = True
        x1_t = x1
        y1_t = y1
        for num in range(1, n_divide + 1):
            if flag_opt1:
                self.drawline(round(x1_t), round(y1_t), round(x1_t + x_temp) - 1, round(y1_t + y_temp) - 1, r, g, b)
                x1_t += x_temp
                y1_t += y_temp
            elif flag_opt2:
                self.drawline(round(x1_t), round(y1_t), round(x1_t + x_temp) - 1, round(y1_t), r, g, b)
                x1_t += x_temp
            elif flag_opt3:
                self.drawline(round(x1_t), round(y1_t), round(x1_t), round(y1_t + y_temp) - 1, r, g, b)
                y1_t += y_temp

    def drawline(self, x1, y1, x2, y2, r, g, b):
        print("Drawing line with points (", x1, ", ", y1, ") -> (", x2, ", ", y2, ")")
        m = (y2 - y1) / (x2 - x1)
        be = y1 - (m * x1)
        self.setpixel(x1, y1, r, g, b)
        self.setpixel(x2, y2, r, g, b)
        y = m * x1 + be
        for x in range(x1 + 1, x2):
            y = y + m
            self.setpixel(x, round(y), r, g, b)

    def setpixel(self, x, y, r, g, b):
        index = 3 * (y * self.width + x)
        self.image[index] = r
        self.image[index + 1] = g
        self.image[index + 2] = b
        with open(self.name + '.ppm', 'wb') as f:
            f.write(bytearray(self.ppm_header, 'ascii'))
            self.image.tofile(f)


def menu():
    images = []
    recur = True
    #    image_name = input("Ingrese el nombre de la imagen: ")
    #    image_width = input("Ingrese el ancho de la imagen: ")
    #    image_height = input("Ingrese la altura de la imagen: ")
    image_name = "nuevo"
    image_width = 1920
    image_height = 1080
    images.append(FHDRaster(image_name, int(image_width), int(image_height), 255))
    print(images)
    while recur:
        print("1. Ingresar pixel.")
        print("2. Ingresar linea.")
        print("3. Ingresar linea segmentada.")
        print("0. Salir")
        option = input("Opción: ")
        if int(option) == 1:
            images[0].setpixel(int(input("Ingrese el valor de x: ")), int(input("Ingrese el valor de y: ")),
                               int(input("Ingrese el valor de r: ")), int(input("Ingrese el valor de g: ")),
                               int(input("Ingrese el valor de b: ")))
        elif int(option) == 2:
            images[0].drawline(int(input("Ingrese el valor de x1: ")), int(input("Ingrese el valor de y1: ")),
                               int(input("Ingrese el valor de x2: ")), int(input("Ingrese el valor de y2: ")),
                               int(input("Ingrese el valor de r: ")), int(input("Ingrese el valor de g: ")),
                               int(input("Ingrese el valor de b: ")))
        elif int(option) == 3:
            images[0].drawandseparatieline(int(input("Ingrese el valor de x1: ")),
                                           int(input("Ingrese el valor de y1: ")),
                                           int(input("Ingrese el valor de x2: ")),
                                           int(input("Ingrese el valor de y2: ")),
                                           int(input("Ingrese el número de secciones de la línea: ")),
                                           int(input("Ingrese el valor de r: ")),
                                           int(input("Ingrese el valor de g: ")), int(input("Ingrese el valor de b: ")))
        elif int(option) == 0:
            recur = False
        pass


if __name__ == '__main__':
    #    raster = FHDRaster("linesDDA", 1920, 1080, 255)
    #    raster.drawandseparatieline(0, 0, 1000, 400, 5, 255, 255, 255)
    menu()

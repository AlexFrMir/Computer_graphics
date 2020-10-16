import array

## PPM header
width = 1920
height = 1080
maxval = 255
ppm_header = f'P6 {width} {height} {maxval}\n'

# PPM image data  (filled with blue)
image = array.array('B',[0,0,0] * width * height)
print(image[1])
#for y in range(1,1000):
#	for x in range(1,1000):
#		if x == y or x == y+1 or x == y-1:
#			index = 3*(y*width+x)
#			print(index)
#			image[index] = 255
#			image[index+1] = 255
#			image[index+2] = 255
#			pass
#		pass
#	pass

#Save the PPM image as a binary file 
with open('blue_example.ppm', 'wb') as f:
	f.write(bytearray(ppm_header, 'ascii'))
	image.tofile(f)
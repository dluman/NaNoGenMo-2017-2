from PIL import Image
import numpy

def encodetransparency(img):
	x = numpy.array(img)
	r,g,b,a = numpy.rollaxis(x,axis=-1)
	r[a==0] = 255
	g[a==0] = 255
	b[a==0] = 255
	x = numpy.dstack([r,g,b,a])
	img = Image.fromarray(x,'RGBA')
	return img

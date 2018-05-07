from PIL import Image, ImageDraw, ImageFont
import random, setPNG

class ATCMap():

	@staticmethod
	def makeMap(plane, map):
		w,h = map.size
		plane_x = random.randint(0,w)
		plane_y = random.randint(0,h)
		draw = ImageDraw.Draw(map)
		font = ImageFont.truetype('type/arial.ttf',15)
		draw.text((plane_x+10,plane_y+10), plane.name, font=font, fill=(0,0,0,255))
		plane.img = setPNG.encodetransparency(plane.img)
		map.paste(plane.img,(plane_x,plane_y),plane.img)
		return map

class locatePlane():

	img = None

	def __init__(self, plane):
		self.img = Image.open('img/SG-ATC-Plane.png')
		self.img = self.img.rotate(plane.bearing)

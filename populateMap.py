from PIL import Image, ImageDraw, ImageFont
import random, setPNG, logOps, getOverlap

class ATCMap():

	@staticmethod
	def makeMap(plane, map):
		prop = {}
		prop[plane.name] = {}
		w,h = map.size
		x,y = (random.randint(0,w), random.randint(0,h))
		prop[plane.name]['plane'] = [(x,y),
					     (x+plane.img.size[0],y+plane.img.size[1])]
		font = ImageFont.truetype('/root/NGM-2017-02/type/arial.ttf',15)
		draw = ImageDraw.Draw(map)
		prop[plane.name]['plane_s'] = [(x+10,y+40),
                                               (x + font.getsize(plane.squawk)[0] + 10,
                                                y + font.getsize(plane.squawk)[1] + 40)]
		prop[plane.name]['plane_n'] = [(x+10,y+20),
                                               (x + font.getsize(plane.name)[0] + 10,
                                                y + font.getsize(plane.name)[1] + 20)]
		collision = getOverlap.test(prop)
		if collision == False:
			logOps.log(prop)
			#TROUBLESHOOTING BOX COLLISION
			#draw.rectangle( (prop[plane.name]['plane'][0],
                        #                 prop[plane.name]['plane'][1]),
                        #                 fill=(0,0,0,75)
                        #              )
			#draw.rectangle( (prop[plane.name]['plane_s'][0],
                        #                 prop[plane.name]['plane_s'][1]),
                        #                 fill=(0,0,0,75)
                        #               )
			#draw.rectangle( (prop[plane.name]['plane_n'][0],
                        #                 prop[plane.name]['plane_n'][1]),
                        #                 fill=(0,0,0,75)
                        #               )
			#TROUBLESHOOTING BOX COLLIISION
			draw.text((x+10,y+20), plane.name, font=font, fill=(0,0,0,255))
			draw.text((x+10,y+40), plane.squawk, font=font, fill=(0,0,0,255))
			plane.img = setPNG.encodetransparency(plane.img)
			map.paste(plane.img,(x,y),plane.img)
		return map, collision

class locatePlane():

	img = None

	def __init__(self, plane):
		self.img = Image.open('/root/NGM-2017-02/img/SG-ATC-Plane.png')
		self.img = self.img.rotate(plane.bearing)

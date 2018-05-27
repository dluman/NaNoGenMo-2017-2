from PIL import Image
from makePlane import Plane
import populateMap
import random
import logOps

logOps.clear()

def addPlane():
	planeObjects = []
	is_overprint = False
	map = Image.open('img/SG-ATC.png')
	planes = random.randint(0,15)
	for i in range(planes):
		plane = Plane()
		plane.img = populateMap.locatePlane(plane).img
		map, is_overprint = populateMap.ATCMap().makeMap(plane,map)
		if is_overprint == False:
			print "[PLANE]\t\t%s\t\tPLOT\t\tSAYS:%s"%(plane.name,plane.squawk)
			planeObjects.append(plane)
	hash = random.getrandbits(128)
	map.save('maps/'+str(hash)+'.png')
	return planeObjects

planes = addPlane()
for plane in planes:
	with open('text.log','aw') as f:
		f.write(plane.name + ' ' + plane.squawk + '\r\n')

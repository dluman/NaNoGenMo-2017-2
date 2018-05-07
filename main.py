from PIL import Image
from makePlane import Plane
import populateMap
import textToSpeech
import random

def addPlane():
	planeObjects = []
	map = Image.open('img/SG-ATC.png')
	planes = random.randint(1,10)
	for i in range(planes):
		plane = Plane()
		plane.img = populateMap.locatePlane(plane).img
		map = populateMap.ATCMap().makeMap(plane,map)
		print "[PLANE]\t%s\tPLOT"%plane.name
		planeObjects.append(plane)
	map.save('maps/test.png')
	return planeObjects

def getAudio(filename):
	transcript = textToSpeech.decode('audio/'+filename)
	return transcript

planes = addPlane()
transcript = getAudio('0000.wav')
print transcript

import random

class Plane():

	name = None
	bearing = None
	captain = None
	origin = None
	destination = None
	img = None

	def __init__(self):
		self.name = self.createName()
		self.bearing = self.setBearing()
		self.captain = self.createCaptain()
		self.origin = self.setOrigin()
		self.destination = self.setDestination()

	def createName(self):
		airlines = {'TAA':'Trans American Airlines','AIA':'Atlantic International Airlines',
			    'WA':'Windsor Airlines','AA':'Ajira Airways','OA':'Oceanic Airlines','JA':'JetAir',
			    'GA':'Gamma Air','CA':'Conglomerated Airlines','OLA':'Olive Airways'}
		airline = random.choice(airlines.keys())
		id = random.randint(101,1024)
		return '%s-%s' % (airline,str(id))

	def setBearing(self):
		return random.randint(10,270)

	def createCaptain(self):
		pass

	def setOrigin(self):
		pass

	def setDestination(self):
		pass

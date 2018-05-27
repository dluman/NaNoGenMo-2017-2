from PIL import Image, ImageDraw, ImageFont

import json,os

def log(planes):
	HOLDER = []
	data = read()
	if len(data) > 0:
		for d in data:
			HOLDER.append(d)
	HOLDER.append(planes)
	with open("captains.log","w") as f:
		json.dump(HOLDER,f)

def clear():
	if os.path.exists("captains.log"):
		os.remove("captains.log")

def read():
	planes = ''
	if(os.path.exists("captains.log")):
		with open("captains.log","r") as f:
			planes = json.load(f)
	return planes

from PIL import Image

import logOps

class Rect:

	def __init__(self,p1,p2):
		self.left = min(p1[0],p2[0])
		self.right = max(p1[0],p2[0])
		self.bottom = max(p1[1],p2[1])
		self.top = min(p1[1],p2[1])

def origin(points):
	return points[0]

def extrema(points):
	return points[1]

def test(plane):
	def overprint(d1_min,d1_max,d2_min,d2_max):
		return (d1_min <= d2_max) and (d2_min <= d1_max)
	planes = logOps.read()
	if len(planes) >= 0:
		for name in plane:
			print name
			is_overprint = False
			for key in plane[name]:
				k0 = origin(plane[name][key])
				k1 = extrema(plane[name][key])
				k_rect = Rect(k0,k1)
				for crafts in planes:
					for craft in crafts:
						for pt in crafts[craft]:
							p0 = origin(crafts[craft][pt])
							p1 = extrema(crafts[craft][pt])
							p_rect = Rect(p0,p1)
							is_overprint = overprint(p_rect.left, p_rect.right, k_rect.left, k_rect.right) and overprint(p_rect.top, p_rect.bottom, k_rect.top, k_rect.bottom)
							if is_overprint == True: return is_overprint
			if k_rect.right >=795 or k_rect.bottom >= 612: return True
	return is_overprint
